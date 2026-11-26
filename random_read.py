"""
Randomly select eligible papers for reading based on their research domain and status.
"""

from __future__ import annotations

import random
import re
from collections import defaultdict
from pathlib import Path


FOLDER_PATH = Path("./Databook")

DOMAIN_QUOTAS = {
    "Blockchain & Distributed Ledger Security": 0,
    "Cryptography & Formal Verification": 0,
    "Hardware & Embedded Systems Security": 0,
    "Large Language Models (LLM)": 0,
    "Machine Learning & AI (non-LLM)": 0,
    "Network Security & Infrastructure": 0,
    "Privacy (Data Security & Analytics)": 0,
    "Software Security & Development Lifecycle": 0,
    "System Security & Threat Detection": 0,
    "Usable Security & Privacy": 0,
}

# Only papers with one of these current Status values are eligible for selection.
ELIGIBLE_STATUSES = {"Ethics Section Extracted"}

TARGET_STATUS = "Reading"
RANDOM_SEED = None
DRY_RUN = True


# ---------------- YAML frontmatter helpers ----------------

FRONTMATTER_PATTERN = re.compile(
    r"^(---\s*\r?\n)(.*?)(\r?\n---\s*\r?\n)",
    flags=re.DOTALL,
)


def get_frontmatter_value(frontmatter: str, key: str) -> str | None:
    """Read a simple YAML scalar value such as `Status: todo`."""
    match = re.search(
        rf"(?mi)^{re.escape(key)}\s*:\s*[\"']?([^#\r\n\"']+?)[\"']?\s*$",
        frontmatter,
    )
    return match.group(1).strip() if match else None


def replace_frontmatter_value(frontmatter: str, key: str, value: str) -> str:
    """Replace an existing simple YAML scalar, or append it if absent."""
    pattern = re.compile(rf"(?m)^({re.escape(key)}\s*:\s*)([^\r\n]*)$")

    if pattern.search(frontmatter):
        return pattern.sub(rf"\g<1>{value}", frontmatter, count=1)

    if not frontmatter.endswith(("\n", "\r\n")):
        frontmatter += "\n"

    return f"{frontmatter}{key}: {value}\n"


def update_status(path: Path, new_status: str) -> None:
    """Update the Status field while preserving the rest of the Markdown file."""
    content = path.read_text(encoding="utf-8")
    match = FRONTMATTER_PATTERN.match(content)

    if not match:
        raise ValueError(f"No YAML frontmatter found: {path}")

    opening, frontmatter, closing = match.groups()
    updated_frontmatter = replace_frontmatter_value(
        frontmatter,
        key="Status",
        value=new_status,
    )

    updated_content = opening + updated_frontmatter + closing + content[match.end() :]
    path.write_text(updated_content, encoding="utf-8")


def normalize_domain(domain: str) -> str:
    """
    Normalize domain strings so they match the keys in DOMAIN_QUOTAS.
    - Strip leading '- ' if present
    - Strip surrounding whitespace
    """
    if not domain:
        return domain
    d = domain.strip()
    if d.startswith("- "):
        d = d[2:].strip()
    return d


# ---------------- Selection logic ----------------


def collect_eligible_papers(folder: Path) -> dict[str, list[Path]]:
    """Group eligible Markdown papers by their Research Domain."""
    papers_by_domain: dict[str, list[Path]] = defaultdict(list)

    for path in folder.rglob("*.md"):
        content = path.read_text(encoding="utf-8")

        match = FRONTMATTER_PATTERN.match(content)
        if not match:
            print(f"Skipping (no YAML frontmatter): {path.name}")
            continue

        frontmatter = match.group(2)
        domain_raw = get_frontmatter_value(frontmatter, "Research Domain")
        status = get_frontmatter_value(frontmatter, "Status")

        if not domain_raw:
            print(f"Skipping (missing Research Domain): {path.name}")
            continue

        domain = normalize_domain(domain_raw)
        normalized_status = status.strip().lower() if status else ""

        if normalized_status == TARGET_STATUS.lower():
            continue

        if ELIGIBLE_STATUSES is not None:
            allowed = {item.lower() for item in ELIGIBLE_STATUSES}
            if normalized_status not in allowed:
                continue

        papers_by_domain[domain].append(path)

    return dict(papers_by_domain)


def select_papers(
    papers_by_domain: dict[str, list[Path]],
    quotas: dict[str, int],
) -> dict[str, list[Path]]:
    """Randomly select up to the requested number of files for each domain."""
    selected: dict[str, list[Path]] = {}

    for domain, requested_count in quotas.items():
        candidates = papers_by_domain.get(domain, [])

        if not candidates:
            print(f"No eligible papers found for domain: {domain}")
            selected[domain] = []
            continue

        count = min(requested_count, len(candidates))

        if count < requested_count:
            print(
                f"{domain}: requested {requested_count}, "
                f"but only {len(candidates)} eligible paper(s) available."
            )

        selected[domain] = random.sample(candidates, count)

    return selected


def main() -> None:
    if not FOLDER_PATH.is_dir():
        raise NotADirectoryError(f"Folder does not exist: {FOLDER_PATH}")

    if RANDOM_SEED is not None:
        random.seed(RANDOM_SEED)

    papers_by_domain = collect_eligible_papers(FOLDER_PATH)
    selected_papers = select_papers(papers_by_domain, DOMAIN_QUOTAS)

    print("\nSelected papers:")
    for domain, paths in selected_papers.items():
        print(f"\n{domain} ({len(paths)} selected):")
        for path in paths:
            print(f"  - {path.relative_to(FOLDER_PATH)}")

    if DRY_RUN:
        print("\nDRY_RUN=True: no files were modified.")
        return

    for paths in selected_papers.values():
        for path in paths:
            update_status(path, TARGET_STATUS)

    print(f"\nUpdated selected papers to Status: {TARGET_STATUS}")


if __name__ == "__main__":
    main()
