"""Ethics-reporting analysis for USENIX Security '25 papers stored as Obsidian/Databook .md files.

Two toggleable analyses:
  * coded  : full Menlo/USENIX coding scheme on hand-coded papers (CODED_DIR)
  * corpus : text-only methods on every paper in the databook (DATABOOK_DIR)
"""

from __future__ import annotations
import os
import argparse
import logging
import re
import warnings
from itertools import combinations
from pathlib import Path

import numpy as np
import pandas as pd
import yaml

from move_papers import copy_coded_papers
# ----------------------------------------------------------------------------
# CONFIGURATION: edit these (CLI flags override them when supplied)
# ----------------------------------------------------------------------------
CODED_DIR = Path("./CodedPapers")  # hand-coded papers (full Menlo/USENIX coding)
DATABOOK_DIR = Path("./Databook")  # full corpus: coded + uncoded papers
OUTPUT_DIR = Path(
    "analysis_output"
)  # results go to <OUTPUT_DIR>/coded and <OUTPUT_DIR>/corpus

RUN_CODED_ANALYSIS = True  # subset analysis on CODED_DIR
RUN_CORPUS_ANALYSIS = True  # corpus-wide analysis on DATABOOK_DIR
CODED_STATUS = (
    "Data coded"  # Status value marking a finished paper; None/"" = include all
)
MAKE_HEATMAPS = True
LDA_TOPICS = 4
BOILERPLATE_THRESHOLD = 0.6
# ----------------------------------------------------------------------------

logger = logging.getLogger("ethics_analysis")
warnings.filterwarnings(
    "ignore", message="This pattern is interpreted as a regular expression"
)

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)

MENLO = [
    "Menlo.Beneficience",
    "Menlo.RespectForPersons",
    "Menlo.Justice",
    "Menlo.RespectForLawAndPublicInterest",
]
USENIX = [
    "Usenix.VulnDisclosure",
    "Usenix.HumanSubjects",
    "Usenix.DataPrivacy",
    "Usenix.StakeholderImpact",
    "Usenix.HarmMitigation",
    "Usenix.ToSViolation",
    "Usenix.LiveTesting",
    "Usenix.ResearcherSafety",
]
QUALITY_BOOL = ["Risk Benefit Analysis", "Alternatives Considered"]
BOOL_CODES = MENLO + USENIX + QUALITY_BOOL
LIST_FIELDS = [
    "Research Domain",
    "Research_Type",
    "Ethics Location",
    "Framework Used",
    "Direct Stakeholders",
    "Indirect Stakeholders",
    "Emerging Themes",
]
DEPTH_ORDER = ["None", "Minimal", "Brief", "Detailed"]
DEPTH_MAP = {d: i for i, d in enumerate(DEPTH_ORDER)}
ETHICS_TEXT_KEY = "Ethics section"

KEYWORDS = {
    "IRB / ethics board": r"\b(?:irb|institutional review board|ethics (?:review )?(?:board|committee)|erb|(?:ethic\w*|irb) approv\w*|approved by (?:our|the) (?:irb|ethics|institution\w*)|irb[- ]exempt|exempt (?:from|by) (?:the )?(?:irb|review))\b",
    "Informed consent": r"\b(?:informed consent|consent(?:ed|ing)?|opt[- ]?(?:in|out))\b",
    "Responsible disclosure": r"\b(?:responsibl[ey] disclos\w*|vulnerability disclosure|coordinated (?:vulnerability )?disclosure|cvd|disclosed (?:the |these |our )?(?:vulnerabilit\w*|findings?|issues?)|notified (?:the )?(?:vendors?|developers?|maintainers?)|bug bount\w*|cve-\d{4})\b",
    "Menlo Report": r"\bmenlo\b",
    "Belmont Report": r"\bbelmont\b",
    "GDPR / law": r"\b(?:gdpr|ccpa|hipaa|cfaa|dmca|data protection (?:law|act|regulation|authorit\w*)|computer fraud|general data protection)\b",
    "Legal (broad)": r"\b(?:laws?|legal(?:ly)?|lawful\w*|legislation|regulations?|copyright\w*|jurisdiction\w*|compliance|compl(?:y|ied|ies|ying) with)\b",
    "Privacy / PII": r"\b(?:privacy|pii|personal(?:ly)? identifiable|personal data|sensitive data|anonymi[sz]\w*|pseudonymi[sz]\w*|de-?identif\w*)\b",
    "Harm / risk": r"\b(?:harm\w*|risk\w*|abuse|misuse)\b",
    "Terms of Service": r"\b(?:terms of (?:service|use)|terms and conditions|tos|robots\.txt|acceptable use|user agreement)\b",
    "Stakeholder": r"\bstakeholders?\b",
    "Public data": r"\b(?:publicly[- ]available|public data|open[- ]source|open data|public (?:dataset|repositor\w*))\b",
    "No concerns claim": r"\b(?:no ethical (?:concerns?|issues?)|does not (?:raise|pose) (?:any )?ethical|did not (?:raise|pose) (?:any )?ethical|no (?:human|participants?) (?:subjects?|involved))\b",
    "Human subjects": r"\b(?:participants?|respondents?|interviewees?|user study|surveys?|interviews?|recruit\w*|crowd ?work\w*|mturk|mechanical turk|prolific|compensat\w*|human subjects?)\b",
    "Respect for persons": r"\b(?:autonom\w*|dignity|voluntar(?:y|ily)|withdraw\w*|debrief\w*|right to (?:refuse|decline|withdraw))\b",
    "Harm mitigation": r"\b(?:mitigat\w*|safeguard\w*|minimi[sz]\w*|precaution\w*|rate[- ]limit\w*|throttl\w*|secure(?:ly)? (?:stor\w*|delet\w*)|delet\w*|encrypt\w*|access[- ]controlled|we (?:did not|never|refrain\w*|avoid\w*))\b",
    "Live testing": r"\b(?:in the wild|live (?:system|service|website|server|network|deployment|test\w*)s?|production (?:system|service|environment|server)s?|real[- ]world (?:system|deployment|device|website)s?|internet[- ]wide|zmap|masscan|active(?:ly)? (?:scan\w*|prob\w*)|scann(?:ed|ing))\b",
    "Researcher safety": r"\b(?:researcher safety|well-?being|psychological|distress\w*|traumat\w*|harass\w*|disturbing|explicit|graphic content|csam)\b",
    "Benefit / justification": r"\b(?:benefits?|outweigh\w*|net (?:positive|benefit)|public interest|societal|greater good|justif\w*)\b",
    "Justice / vulnerable groups": r"\b(?:justice|fair(?:ly|ness)?|equit\w*|bias\w*|vulnerable (?:population|group|user|communit)\w*|marginali[sz]\w*|minors?|children|underrepresented)\b",
    "Risk-benefit analysis": r"\b(?:risk[- ]benefit|benefits? (?:and|vs\.?|versus) risks?|risks? (?:and|vs\.?|versus) benefits?|weigh\w*|balanc\w*)\b",
    "Alternatives considered": r"\b(?:alternatives?|less (?:invasive|intrusive)|instead of|considered (?:other|alternative)|other (?:approach|method)s?)\b",
}


# ----------------------------------------------------------------------------
# Loading and preparation
# ----------------------------------------------------------------------------
def parse_frontmatter(content: str) -> dict:
    """Parse the YAML frontmatter block from a Databook .md file, if present."""
    m = FRONTMATTER_RE.match(content)
    if not m:
        return {}
    try:
        return yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError as e:
        logger.warning("Could not parse YAML frontmatter (%s)", e)
        return {}


def _as_list(v) -> list:
    if v is None:
        return []
    return [str(x).strip() for x in v] if isinstance(v, list) else [str(v).strip()]


def _as_bool(v) -> float:
    """Return 1.0 / 0.0, or NaN when the field is missing or not boolean-like."""
    if isinstance(v, list):
        v = v[0] if len(v) == 1 else None
    if isinstance(v, bool):
        return float(v)
    if isinstance(v, str) and v.strip().lower() in {"true", "false"}:
        return float(v.strip().lower() == "true")
    return np.nan


def _as_scalar(v):
    """Return a single string from a scalar or list-valued field (first item wins)."""
    if isinstance(v, list):
        if len(v) > 1:
            logger.warning("Multiple values where one expected: %s (using first)", v)
        v = v[0] if v else None
    return None if v is None else str(v).strip()


def _norm_depth(v):
    """Normalise depth labels: 'Minimal (1 sentence)' / 'brief' -> 'Minimal' / 'Brief'."""
    s = _as_scalar(v)
    if not s:
        return None
    key = s.split("(")[0].strip().lower()
    return {d.lower(): d for d in DEPTH_ORDER}.get(key, s)


def load_papers(directory: Path, status: str | None = None) -> pd.DataFrame:
    """Load every .md file in `directory` into a DataFrame (one row per paper)."""

    if not os.path.exists(directory):
        copy_coded_papers()
    
    rows, skipped = [], 0
    files = sorted(Path(directory).glob("*.md"))
    logger.info("Found %d markdown files in %s", len(files), directory)
    for f in files:
        fm = parse_frontmatter(f.read_text(encoding="utf-8", errors="replace"))
        if not fm:
            skipped += 1
            logger.warning("No frontmatter: %s", f.name)
            continue
        if status and fm.get("Status") != status:
            skipped += 1
            logger.debug("Skipping %s (Status=%s)", f.name, fm.get("Status"))
            continue
        ethics_text = fm.get(ETHICS_TEXT_KEY) or ""
        if isinstance(ethics_text, list):
            ethics_text = " ".join(map(str, ethics_text))
        row = {
            "file": f.name,
            "title": _as_scalar(fm.get("title")),
            "coded_date": fm.get("coded_date"),
            "Status": _as_scalar(fm.get("Status")),
            "Ethics Depth": _norm_depth(fm.get("Ethics Depth")),
            ETHICS_TEXT_KEY: str(ethics_text),
            "notes": str(fm.get("notes") or ""),
            "key_quotes": str(fm.get("key_quotes") or ""),
        }
        for k in LIST_FIELDS:
            row[k] = _as_list(fm.get(k))
        for k in BOOL_CODES:
            row[k] = _as_bool(fm.get(k))
        rows.append(row)
    df = pd.DataFrame(rows)
    logger.info("Loaded %d papers (%d skipped)", len(df), skipped)
    return df


def enrich(df: pd.DataFrame) -> pd.DataFrame:
    """Add derived columns: word/sentence counts, depth score, code totals, primary domain."""
    df = df.copy()
    txt = df[ETHICS_TEXT_KEY].astype(str)
    df["ethics_words"] = txt.str.split().str.len()
    df["ethics_sentences"] = txt.apply(
        lambda t: len([s for s in re.split(r"(?<=[.!?])\s+", t.strip()) if s])
    )
    df["depth_score"] = df["Ethics Depth"].map(DEPTH_MAP)
    df["menlo_count"] = df[MENLO].sum(axis=1, skipna=True)
    df["usenix_count"] = df[USENIX].sum(axis=1, skipna=True)
    df["total_codes"] = df["menlo_count"] + df["usenix_count"]
    df["primary_domain"] = df["Research Domain"].apply(
        lambda x: x[0] if x else "Unassigned"
    )
    df["has_ethics_text"] = df["ethics_words"] > 1
    return df


def explode(df: pd.DataFrame, col: str) -> pd.DataFrame:
    """One row per (paper, value) for a multi-valued column."""
    out = df.explode(col, ignore_index=True)
    out[col] = out[col].fillna("Unassigned")
    return out


def validate(df: pd.DataFrame) -> pd.DataFrame:
    """Report missing/inconsistent fields so coding gaps are visible before analysis."""
    checks = {
        "missing_depth": df["Ethics Depth"].isna(),
        "unknown_depth_label": df["Ethics Depth"].notna()
        & ~df["Ethics Depth"].isin(DEPTH_ORDER),
        "missing_domain": df["Research Domain"].str.len() == 0,
        "missing_type": df["Research_Type"].str.len() == 0,
        "missing_location": df["Ethics Location"].str.len() == 0,
        "empty_ethics_text": ~df["has_ethics_text"],
        "missing_menlo_code": df[MENLO].isna().any(axis=1),
        "missing_usenix_code": df[USENIX].isna().any(axis=1),
        "depth_none_but_text": (df["Ethics Depth"] == "None") & df["ethics_words"] > 1,
        "depth_detailed_but_short": (df["Ethics Depth"] == "Detailed")
        & (df["ethics_words"] < 150),
        "missing_framework": df["Framework Used"].str.len() == 0
    }
    rep = pd.DataFrame(checks)
    rep.insert(0, "file", df["file"])
    for k in checks:
        n = int(rep[k].sum())
        (logger.warning if n else logger.info)("Validation %-26s %d paper(s)", k, n)
    return rep[rep.drop(columns="file").any(axis=1)].set_index("file")


def sample_balance(df: pd.DataFrame) -> pd.DataFrame:
    """Papers per domain (sampling balance for the stratified claims)."""
    t = (
        explode(df, "Research Domain")["Research Domain"]
        .value_counts()
        .rename("papers")
        .to_frame()
    )
    logger.info("Papers per domain:\n%s", t.to_string())
    return t


# ----------------------------------------------------------------------------
# Coded-subset analyses
# ----------------------------------------------------------------------------
def prevalence(df: pd.DataFrame, codes: list[str], by: str | None) -> pd.DataFrame:
    """% of papers with each code (overall, or per group of a multi-valued column)."""
    short = {c: c.split(".")[-1] for c in codes}
    if by is None:
        res = (
            (df[codes].mean() * 100).rename(index=short).round(1).to_frame("pct_papers")
        )
        res["n_true"] = df[codes].sum().rename(index=short).astype(int)
        return res
    e = explode(df, by)
    res = (e.groupby(by)[codes].mean() * 100).rename(columns=short).round(1)
    res.insert(0, "n", e.groupby(by).size())
    return res


def depth_location_framework(df: pd.DataFrame) -> dict[str, pd.DataFrame]:
    """RQ1 / RQ2: depth, location, frameworks, length and stakeholders."""
    out = {}
    out["depth_overall"] = (
        df["Ethics Depth"]
        .value_counts()
        .reindex(DEPTH_ORDER)
        .fillna(0)
        .astype(int)
        .to_frame("n").transpose()
    )
    for by, tag in [("Research Domain", "domain"), ("Research_Type", "type")]:
        e = explode(df, by)
        out[f"depth_by_{tag}"] = pd.crosstab(e[by], e["Ethics Depth"]).reindex(
            columns=DEPTH_ORDER, fill_value=0
        )
        out[f"depth_by_{tag}"]["Papers"] = out[f"depth_by_{tag}"].sum(axis=1)
        out[f"length_by_{tag}"] = e.groupby(by)["ethics_words"].describe().round(1)
    for col, name in [
        ("Ethics Location", "location"),
        ("Framework Used", "framework"),
        ("Direct Stakeholders", "stakeholders_direct"),
        ("Indirect Stakeholders", "stakeholders_indirect"),
        ("Emerging Themes", "emerging_themes"),
    ]:
        out[name] = explode(df, col)[col].value_counts().to_frame("n")
    out["length_overall"] = (
        df["ethics_words"].describe().round(1).to_frame("ethics_words").transpose()
    )
    out["location"] = out["location"].transpose()
    out["framework"] = out["framework"].transpose()
    logger.info("Depth distribution:\n%s", out["depth_overall"].to_string())
    logger.info(
        "Ethics length (words): mean=%.1f median=%.1f",
        df["ethics_words"].mean(),
        df["ethics_words"].median(),
    )
    return out


def phi_matrix(df: pd.DataFrame, codes: list[str]) -> pd.DataFrame:
    """Pairwise phi coefficient (Pearson on binary codes)."""
    m = df[codes].dropna().corr().round(2)
    m.index = m.columns = [c.split(".")[-1] for c in codes]
    return m


def cooccurrence_pairs(df: pd.DataFrame, codes: list[str]) -> pd.DataFrame:
    """Joint counts, Jaccard and phi for every code pair."""
    x = df[codes].dropna().astype(int)
    rows = []
    for a, b in combinations(codes, 2):
        both = int(((x[a] == 1) & (x[b] == 1)).sum())
        either = int(((x[a] == 1) | (x[b] == 1)).sum())
        rows.append(
            {
                "code_a": a.split(".")[-1],
                "code_b": b.split(".")[-1],
                "both": both,
                "jaccard": round(both / either, 2) if either else np.nan,
                "phi": round(x[a].corr(x[b]), 2),
            }
        )
    return pd.DataFrame(rows).sort_values("phi", ascending=False)


def depth_vs_coverage(df: pd.DataFrame) -> pd.DataFrame:
    """Spearman correlations between length / depth / number of codes (padding vs. substance)."""
    from scipy.stats import spearmanr

    rows = []
    for a, b in [
        ("ethics_words", "total_codes"),
        ("depth_score", "total_codes"),
        ("depth_score", "ethics_words"),
        ("ethics_words", "menlo_count"),
    ]:
        s = df[[a, b]].dropna()
        if len(s) > 3 and s[a].nunique() > 1 and s[b].nunique() > 1:
            rho, p = spearmanr(s[a], s[b])
            rows.append(
                {
                    "x": a,
                    "y": b,
                    "spearman_rho": round(rho, 3),
                    "p_value": round(p, 4),
                }
            )
    res = pd.DataFrame(rows)
    logger.info("Depth/length vs. coverage:\n%s", res.to_string(index=False))
    return res


def domain_differences(
    df: pd.DataFrame, codes: list[str], by: str = "primary_domain"
) -> pd.DataFrame:
    """Chi-square per code across groups (single-label grouping keeps observations independent)."""
    from scipy.stats import chi2_contingency

    rows = []
    for c in codes:
        ct = pd.crosstab(*[df[[by, c]].dropna()[k] for k in (by, c)])
        if ct.shape[0] < 2 or ct.shape[1] < 2:
            continue
        chi2, p, dof, exp = chi2_contingency(ct)
        rows.append(
            {
                "code": c.split(".")[-1],
                "groups": ct.shape[0],
                "chi2": round(chi2, 2),
                "dof": dof,
                "p_value": round(p, 4),
                "low_expected_cells_pct": round((exp < 5).mean() * 100, 1),
            }
        )
    res = pd.DataFrame(rows)
    if not res.empty:
        res = res.sort_values("p_value")
    logger.info(
        "Group differences by %s (small n is unreliable; see low_expected_cells_pct):\n%s",
        by,
        res.to_string(index=False),
    )
    return res


def cohen_kappa(a, b) -> float:
    """Cohen's kappa for two label vectors."""
    a, b = np.asarray(a), np.asarray(b)
    po = (a == b).mean()
    pe = sum(
        (a == l).mean() * (b == l).mean() for l in np.unique(np.concatenate([a, b]))
    )
    return 1.0 if pe == 1 else (po - pe) / (1 - pe)


# ----------------------------------------------------------------------------
# Text analyses (usable on coded subset and full corpus)
# ----------------------------------------------------------------------------
def keyword_screen(
    df: pd.DataFrame, by: str = "Research Domain"
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Regex keyword hits per paper and % of papers per group mentioning each concept."""
    txt = df[ETHICS_TEXT_KEY].astype(str).str.lower().reset_index(drop=True)
    hits = pd.DataFrame(
        {k: txt.str.contains(p, regex=True).astype(int) for k, p in KEYWORDS.items()}
    )
    hits.insert(0, "file", df["file"].values)
    tmp = pd.concat(
        [df[["file", by]].reset_index(drop=True), hits.drop(columns="file")], axis=1
    )
    per_group = (explode(tmp, by).groupby(by)[list(KEYWORDS)].mean() * 100).round(1)
    logger.info(
        "Keyword prevalence (overall %% of papers):\n%s",
        (hits[list(KEYWORDS)].mean() * 100).round(1).to_string(),
    )
    return hits, per_group


def keyword_vs_manual(df: pd.DataFrame, hits: pd.DataFrame) -> pd.DataFrame:
    """Validate regex proxies against manual codes (agreement + Cohen's kappa)."""
    pairs = [
        ("Responsible disclosure", "Usenix.VulnDisclosure"),
        ("Human subjects", "Usenix.HumanSubjects"),
        ("Privacy / PII", "Usenix.DataPrivacy"),
        ("Stakeholder", "Usenix.StakeholderImpact"),
        ("Harm mitigation", "Usenix.HarmMitigation"),
        ("Terms of Service", "Usenix.ToSViolation"),
        ("Live testing", "Usenix.LiveTesting"),
        ("Researcher safety", "Usenix.ResearcherSafety"),
        ("Benefit / justification", "Menlo.Beneficience"),
        ("Informed consent", "Menlo.RespectForPersons"),
        ("Respect for persons", "Menlo.RespectForPersons"),
        ("Justice / vulnerable groups", "Menlo.Justice"),
        ("GDPR / law", "Menlo.RespectForLawAndPublicInterest"),
        ("Legal (broad)", "Menlo.RespectForLawAndPublicInterest"),
        ("Risk-benefit analysis", "Risk Benefit Analysis"),
        ("Alternatives considered", "Alternatives Considered"),
    ]
    rows = []
    for kw, code in pairs:
        a, b = hits[kw].values, df[code].values
        ok = ~np.isnan(b)
        a, b = a[ok].astype(int), b[ok].astype(int)
        if len(a):
            rows.append(
                {
                    "keyword": kw,
                    "manual_code": code.split(".")[-1],
                    "agreement_pct": round((a == b).mean() * 100, 1),
                    "cohen_kappa": round(cohen_kappa(a, b), 3),
                }
            )
    res = pd.DataFrame(rows).sort_values("cohen_kappa", ascending=False)
    logger.info("Regex proxy vs. manual coding:\n%s", res.to_string(index=False))
    return res


def tfidf_terms(
    df: pd.DataFrame, by: str = "primary_domain", top: int = 10
) -> pd.DataFrame:
    """Most distinctive terms per group using TF-IDF over concatenated ethics text."""
    from sklearn.feature_extraction.text import TfidfVectorizer

    g = df[df["has_ethics_text"]].groupby(by)[ETHICS_TEXT_KEY].apply(" ".join)
    if len(g) < 2:
        logger.warning("Need >= 2 groups for TF-IDF; skipping")
        return pd.DataFrame()
    vec = TfidfVectorizer(stop_words="english", ngram_range=(1, 2), max_df=0.8)
    X = vec.fit_transform(g.values)
    terms = np.array(vec.get_feature_names_out())
    return pd.DataFrame(
        {
            grp: terms[np.argsort(X[i].toarray().ravel())[::-1][:top]]
            for i, grp in enumerate(g.index)
        }
    )


def topic_model(df: pd.DataFrame, k: int = LDA_TOPICS, top: int = 8) -> pd.DataFrame:
    """LDA topics over ethics text (exploratory; most meaningful on the full corpus)."""
    from sklearn.decomposition import LatentDirichletAllocation
    from sklearn.feature_extraction.text import CountVectorizer

    docs = df.loc[df["has_ethics_text"], ETHICS_TEXT_KEY]
    if len(docs) < 10:
        logger.warning("Too few documents (%d) for LDA; skipping", len(docs))
        return pd.DataFrame()
    vec = CountVectorizer(stop_words="english", min_df=2, max_df=0.9)
    X = vec.fit_transform(docs)
    lda = LatentDirichletAllocation(n_components=k, random_state=42).fit(X)
    terms = np.array(vec.get_feature_names_out())
    return pd.DataFrame(
        {
            f"topic_{i + 1}": terms[np.argsort(c)[::-1][:top]]
            for i, c in enumerate(lda.components_)
        }
    )


def boilerplate_scores(
    df: pd.DataFrame, threshold: float = BOILERPLATE_THRESHOLD
) -> pd.DataFrame:
    """Flag likely boilerplate: high max TF-IDF cosine similarity to another paper's text, or low lexical diversity."""
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity

    d = df[df["has_ethics_text"]].reset_index(drop=True)
    if len(d) < 3:
        return pd.DataFrame()
    S = cosine_similarity(
        TfidfVectorizer(stop_words="english").fit_transform(d[ETHICS_TEXT_KEY])
    )
    np.fill_diagonal(S, 0)
    toks = d[ETHICS_TEXT_KEY].str.lower().str.findall(r"\w+")
    out = pd.DataFrame(
        {
            "file": d["file"],
            "max_similarity": S.max(axis=1).round(2),
            "most_similar_to": d["file"].values[S.argmax(axis=1)],
            "type_token_ratio": toks.apply(
                lambda t: round(len(set(t)) / len(t), 2) if t else np.nan
            ),
            "words": d["ethics_words"],
        }
    )
    out["likely_boilerplate"] = out["max_similarity"] >= threshold
    # Remove duplicates based on repeated pairs of files
    out = out.loc[
        ~out[["file", "most_similar_to"]].apply(frozenset, axis=1).duplicated()
    ]
    logger.info(
        "Boilerplate candidates (similarity >= %.2f): %d",
        threshold,
        int(out["likely_boilerplate"].sum()),
    )
    out = out[out["likely_boilerplate"]==True]
    return out.sort_values("max_similarity", ascending=False).set_index("file")


# ----------------------------------------------------------------------------
# Corpus-only analyses
# ----------------------------------------------------------------------------
def corpus_overview(df: pd.DataFrame) -> dict[str, pd.DataFrame]:
    """Ethics-section presence and length per domain across the full corpus."""
    e = explode(df, "Research Domain")
    g = e.groupby("Research Domain")
    present = e[e["has_ethics_text"]].groupby("Research Domain")["ethics_words"]
    overview = pd.DataFrame(
        {
            "papers": g.size(),
            "median_words_if_present": present.median(),
            "mean_words_if_present": present.mean().round(1),
            "coded_papers": g["Status"].apply(lambda x: int((x == CODED_STATUS).sum()))
            if CODED_STATUS
            else np.nan,
        }
    )
    logger.info(
        "Corpus: %d papers, %d (%.1f%%) with extracted ethics text\n%s",
        len(df),
        int(df["has_ethics_text"].sum()),
        df["has_ethics_text"].mean() * 100,
        overview.to_string(),
    )
    bins = pd.cut(
        e["ethics_words"],
        [-1, 0, 50, 150, 400, np.inf],
        labels=["none", "1-50", "51-150", "151-400", "400+"],
    )
    return {
        "corpus_by_domain": overview,
        "length_by_domain": present.describe().round(1),
        "length_overall": e["ethics_words"].describe().round(1),
        "length_bins_by_domain": pd.crosstab(e["Research Domain"], bins),
    }


def representativeness(df: pd.DataFrame) -> pd.DataFrame:
    """Compare coded vs. uncoded papers on ethics-text length and domain mix."""
    from scipy.stats import mannwhitneyu

    if not CODED_STATUS:
        return pd.DataFrame()
    coded = df["Status"] == CODED_STATUS
    a = df.loc[coded & df["has_ethics_text"], "ethics_words"]
    b = df.loc[~coded & df["has_ethics_text"], "ethics_words"]
    rows = []
    if len(a) > 2 and len(b) > 2:
        _, p = mannwhitneyu(a, b)
        rows.append(
            {
                "metric": "Words (Mann-Whitney U)",
                "coded": a.median(),
                "uncoded": b.median(),
                "p_value": round(p, 4),
            }
        )
        logger.info(
            "Coded vs. uncoded length: median %.0f vs %.0f words (p=%.4f)",
            a.median(),
            b.median(),
            p,
        )
    
    e = explode(df.assign(is_coded=coded), "Research Domain")
    dom = (
        pd.crosstab(e["Research Domain"], e["is_coded"], normalize="columns")
        .mul(100)
        .round(1)
    )
    dom.columns = ["coded_pct" if c else "uncoded_pct" for c in dom.columns]
    logger.info("Domain mix, coded vs. uncoded (%%):\n%s", dom.to_string())
    return pd.concat(
        [
            pd.DataFrame(rows),
            dom.reset_index().rename(columns={"Research Domain": "metric"}),
        ],
        ignore_index=True,
    )

def research_type_vs_domain(df: pd.DataFrame) -> pd.DataFrame:
    """% of papers in each domain that carry each research type (multi-label, rows can exceed 100)."""
    e = explode(explode(df, "Research_Type"), "Research Domain")
    counts = pd.crosstab(e["Research Domain"], e["Research_Type"])
    papers = explode(df, "Research Domain").groupby("Research Domain").size()
    pct = counts.div(papers.reindex(counts.index), axis=0).mul(100).round(1)
    pct = pct.drop(index="Unassigned", columns="Unassigned", errors="ignore")
    pct.insert(0, "n", papers.reindex(pct.index))
    return pct

# ---- add to analyze_ethics.py (after enrich/explode) ----
TYPE_EXPECTED = {
    "Human Subjects": ["Usenix.HumanSubjects", "Usenix.DataPrivacy",
                       "Menlo.RespectForPersons"],
    "Vuln Research":  ["Usenix.VulnDisclosure", "Usenix.HarmMitigation",
                       "Risk Benefit Analysis"],
    "Measurement":    ["Usenix.DataPrivacy", "Usenix.LiveTesting",
                       "Usenix.HarmMitigation"],
    "System":         ["Usenix.StakeholderImpact", "Usenix.HarmMitigation"],
    "Theory":         [],
    "SoK":            [],
}


def score_papers(df: pd.DataFrame) -> pd.DataFrame:
    """Completeness score per (paper, type); higher = fuller reporting.

    score = depth (0-3) + risk-benefit + alternatives + framework named
            + share of type-expected codes covered (0-1)
    Measures extent/coverage, not the quality of ethical reasoning.
    """
    e = explode(df, "Research_Type").copy()

    def expected_share(row):
        codes = TYPE_EXPECTED.get(row["Research_Type"], [])
        if not codes:
            return 0.0
        return float(np.nansum([row[c] for c in codes])) / len(codes)

    e["expected_cov"] = e.apply(expected_share, axis=1)
    e["has_framework"] = e["Framework Used"].apply(lambda x: float(len(x) > 0))
    e["score"] = (
        e["depth_score"].fillna(0)
        + e["Risk Benefit Analysis"].fillna(0)
        + e["Alternatives Considered"].fillna(0)
        + e["has_framework"]
        + e["expected_cov"]
    )
    return e


def rank_by_type(df: pd.DataFrame, top_n: int = 5) -> pd.DataFrame:
    """Top-N papers per research type, with other types and domain shown."""
    e = score_papers(df)
    e["also_types"] = e.apply(
        lambda r: ", ".join(t for t in df.loc[df["file"] == r["file"],
                            "Research_Type"].iloc[0] if t != r["Research_Type"]),
        axis=1,
    )
    e["key"] = e["file"].str.replace(r"\.md$", "", regex=True)
    cols = ["Research_Type", "key", "primary_domain", "Ethics Depth",
            "ethics_words", "total_codes", "score", "also_types"]
    out = (
        e.sort_values(["Research_Type", "score", "ethics_words"],
                      ascending=[True, False, False])
         .groupby("Research_Type", sort=False)
         .head(top_n)[cols]
         .reset_index(drop=True)
    )
    out["rank"] = out.groupby("Research_Type").cumcount() + 1
    return out


def overlap_table(df: pd.DataFrame, show: bool = True) -> pd.DataFrame:
    """Type x type co-occurrence counts; diagonal = papers per type."""
    types = sorted({t for ts in df["Research_Type"] for t in ts})
    m = pd.DataFrame(0, index=types, columns=types, dtype=int)
    for ts in df["Research_Type"]:
        for a in ts:
            for b in ts:
                m.loc[a, b] += 1
    if show:
        n_multi = int((df["Research_Type"].str.len() > 1).sum())
        print(f"\nType overlap (diagonal = papers per type); "
              f"{n_multi}/{len(df)} papers carry >1 type\n")
        print(m.to_string())
        combos = df["Research_Type"].apply(lambda ts: " + ".join(sorted(ts)))
        print("\nMost common type combinations:")
        print(combos.value_counts().head(10).to_string())
    return m

def theory_split(df):
    t = df[df["Research_Type"].apply(lambda x: "Theory" in x)].copy()
    def grp(x):
        s = set(x)
        if s & {"Human Subjects", "Measurement"}: return "Theory + HS/Measurement"
        if "Vuln Research" in s:                  return "Theory + Vuln Research"
        return "Theory + System only"
    t["group"] = t["Research_Type"].apply(grp)
    return pd.crosstab(t["group"], t["Ethics Depth"]).reindex(
        columns=DEPTH_ORDER, fill_value=0)

# ----------------------------------------------------------------------------
# Output helpers and runners
# ----------------------------------------------------------------------------
def heatmap(table: pd.DataFrame, path: Path, title: str) -> None:
    """Save an annotated heatmap (skipped if disabled or matplotlib is unavailable)."""
    if not MAKE_HEATMAPS:
        return
    try:
        import matplotlib

        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        logger.warning("matplotlib not installed; skipping %s", path.name)
        return
    data = table.drop(columns=["n"], errors="ignore")
    fig, ax = plt.subplots(figsize=(1.2 * data.shape[1] + 3, 0.6 * data.shape[0] + 2))
    im = ax.imshow(
        data.values.astype(float), cmap="Blues", vmin=0, vmax=100, aspect="auto"
    )
    ax.set_xticks(range(data.shape[1]), data.columns, rotation=45, ha="right")
    ax.set_yticks(range(data.shape[0]), data.index)
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            ax.text(
                j, i, f"{data.values[i, j]:.0f}", ha="center", va="center", fontsize=8
            )
    ax.set_title(title)
    fig.colorbar(im, label="% of papers")
    fig.tight_layout()
    fig.savefig(path, dpi=200)
    plt.close(fig)


def save(tables: dict[str, pd.DataFrame], outdir: Path) -> None:
    n = 0
    for name, t in tables.items():
        if t is not None and not t.empty:
            t.to_csv(outdir / f"{name}.csv")
            n += 1
    logger.info("Wrote %d tables to %s", n, outdir)


def _slim(df: pd.DataFrame) -> pd.DataFrame:
    return df.drop(columns=[ETHICS_TEXT_KEY, "notes", "key_quotes"]).set_index("file")


def run_coded(outdir: Path, save_file: bool = True) -> pd.DataFrame | None:
    """Subset analysis: full coding scheme on the hand-coded papers."""
    outdir.mkdir(parents=True, exist_ok=True)
    df = enrich(load_papers(CODED_DIR, CODED_STATUS or None))
    if df.empty:
        logger.error("No coded papers loaded from %s", CODED_DIR)
        return None
    t: dict[str, pd.DataFrame] = {
        "validation_issues": validate(df),
        "sample_balance": sample_balance(df),
    }
    t["menlo_overall"] = prevalence(df, MENLO, None).transpose()
    t["usenix_overall"] = prevalence(df, USENIX, None)
    t["quality_overall"] = prevalence(df, QUALITY_BOOL, None)
    for by, tag in [("Research Domain", "domain"), ("Research_Type", "type")]:
        t[f"menlo_by_{tag}"] = prevalence(df, MENLO, by)
        t[f"usenix_by_{tag}"] = prevalence(df, USENIX, by)
        t[f"quality_by_{tag}"] = prevalence(df, QUALITY_BOOL, by)
        heatmap(
            t[f"menlo_by_{tag}"],
            outdir / f"menlo_by_{tag}.png",
            f"Menlo coverage by {tag}",
        )
        heatmap(
            t[f"usenix_by_{tag}"],
            outdir / f"usenix_by_{tag}.png",
            f"USENIX coverage by {tag}",
        )
    t.update(depth_location_framework(df))
    t["menlo_phi"] = phi_matrix(df, MENLO)
    t["code_pairs"] = cooccurrence_pairs(df, MENLO + USENIX)
    t["depth_vs_coverage"] = depth_vs_coverage(df)
    fe = explode(df, "Framework Used")
    t["framework_by_depth"] = (
    pd.crosstab(fe["Framework Used"], fe["Ethics Depth"], values=fe["ethics_words"], aggfunc="count")
    .reindex(columns=DEPTH_ORDER, fill_value=0)
    .drop(index="Unassigned", errors="ignore")
    ).fillna(0)
    t["group_tests_menlo"] = domain_differences(df, MENLO)
    t["group_tests_usenix"] = domain_differences(df, USENIX)
    hits, t["keyword_by_domain"] = keyword_screen(df)
    t["keyword_hits"] = hits.set_index("file")
    t["keyword_vs_manual"] = keyword_vs_manual(df, hits)
    t["tfidf_by_domain"] = tfidf_terms(df)
    t["lda_topics"] = topic_model(df)
    t["boilerplate"] = boilerplate_scores(df)
    t["papers_enriched"] = _slim(df)
    t["type_vs_domain"] = research_type_vs_domain(df)
    t["ranking_by_type"] = rank_by_type(df, top_n=5)
    t["overlap_by_type"] = overlap_table(df)
    t["theory_split"] = theory_split(df)
    if save_file:
        save(t, outdir)
    return df, t


def run_corpus(outdir: Path, coded_df: pd.DataFrame | None, save_file: bool = True) -> None:
    """Corpus-wide analysis on the databook: text-only methods that need no manual codes."""
    outdir.mkdir(parents=True, exist_ok=True)
    df = enrich(load_papers(DATABOOK_DIR))
    if df.empty:
        logger.error("No papers loaded from %s", DATABOOK_DIR)
        return
    dup = int(df["title"].duplicated().sum())
    if dup:
        logger.warning("%d duplicate titles in databook", dup)
    t: dict[str, pd.DataFrame] = {"sample_balance": sample_balance(df)}
    t.update(corpus_overview(df))
    t["representativeness"] = representativeness(df)
    rep = t["representativeness"]
    if not rep.empty:
        is_test = rep["metric"].str.contains("Words|pct_with", regex=True)
        t["representativeness_tests"] = rep[is_test].set_index("metric")[["coded", "uncoded", "p_value"]]
        t["representativeness_domains"] = (
            rep[~is_test].set_index("metric")[["coded_pct", "uncoded_pct"]]
        )
    text_df = df[df["has_ethics_text"]].reset_index(drop=True)
    hits, t["keyword_by_domain"] = keyword_screen(text_df)
    t["keyword_hits"] = hits.set_index("file")
    kw = hits.drop(columns="file")
    t["keyword_overall"] = pd.DataFrame({
        "pct_papers": (kw.mean() * 100).round(1),
        "n": kw.sum().astype(int),
    })
    t["tfidf_by_domain"] = tfidf_terms(text_df)
    t["lda_topics"] = topic_model(text_df)
    t["boilerplate"] = boilerplate_scores(text_df)
    t["papers_enriched"] = _slim(df)
    t["length_summary"] = (df.loc[df["has_ethics_text"], "ethics_words"].describe().round(1).to_frame("ethics_words")).transpose()
    if save_file:
        save(t, outdir)
    return df,t

def main() -> None:
    global \
        CODED_DIR, \
        DATABOOK_DIR, \
        OUTPUT_DIR, \
        RUN_CODED_ANALYSIS, \
        RUN_CORPUS_ANALYSIS, \
        CODED_STATUS
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("--coded-dir", type=Path)
    ap.add_argument("--databook-dir", type=Path)
    ap.add_argument("--out", type=Path)
    ap.add_argument("--status", help="Status value marking coded papers ('' = all)")
    ap.add_argument("--skip-coded", action="store_true")
    ap.add_argument("--skip-corpus", action="store_true")
    ap.add_argument("-v", "--verbose", action="store_true")
    ap.add_argument("--no-save", action="store_true")
    a = ap.parse_args()
    CODED_DIR, DATABOOK_DIR = a.coded_dir or CODED_DIR, a.databook_dir or DATABOOK_DIR
    OUTPUT_DIR = a.out or OUTPUT_DIR
    CODED_STATUS = CODED_STATUS if a.status is None else (a.status or None)
    RUN_CODED_ANALYSIS &= not a.skip_coded
    RUN_CORPUS_ANALYSIS &= not a.skip_corpus
    save_file = not a.no_save
    logging.basicConfig(
        level=logging.DEBUG if a.verbose else logging.INFO,
        format="%(asctime)s %(levelname)-7s %(name)s: %(message)s",
        datefmt="%H:%M:%S",
    )
    coded_df = None
    if RUN_CODED_ANALYSIS:
        coded_df, _ = run_coded(Path(OUTPUT_DIR) / "coded", save_file=save_file)
    elif RUN_CORPUS_ANALYSIS and Path(CODED_DIR).exists():
        coded_df = enrich(load_papers(CODED_DIR, CODED_STATUS or None))
    if RUN_CORPUS_ANALYSIS:
        run_corpus(Path(OUTPUT_DIR) / "corpus", coded_df, save_file=save_file)
if __name__ == "__main__":
    main()
