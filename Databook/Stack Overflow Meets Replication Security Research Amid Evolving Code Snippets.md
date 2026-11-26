---
Alternatives Considered: false
author: Alfusainey Jallow and Sven Bugiel
author_tags:
  - Alfusainey Jallow
  - Sven Bugiel
base: "[[Databook.base]]"
DBLP Ref: DBLP:conf/uss/JallowB25
Direct Stakeholders: []
Emerging Themes: []
Ethics Depth:
Ethics Location: []
Ethics section: "Reproducibility and Reliability. We tried to consider the implications of our findings for the broader field. Where our replication studies produced different results from the original study, we tried to discuss the possible reasons for these differences and their impact on the original findings. We aim to identify the potential causes for diverging results in a systematic way before our replication study in §3 and §4.\r

  Originality and Plagiarism. We acknowledge the original studies we replicated. We avoid plagiarism by properly crediting the original authors and citing their work appropriately.\r

  Respect for Original Research. We tried to be respectful of the original researchers’ work. Critiques or discussions regarding the original study are phrased constructively and based on the data and findings.\r

  Consent for the Use of Original Data. All data and code artifacts of the prior studies were either publicly available (on request) or re-implemented based on the published results. We credited the original researchers appropriately if their artifacts were reused, and our systematization in Section 3 highlights which artifacts were available.\r

  Communication with Original Researchers. We engaged with the original researchers, especially when we could not reproduce the original results and when artifacts were un available or seemingly flawed. This was intended to help ensure that any discrepancies are thoroughly understood and addressed in a collaborative manner.\r

  Responsible Disclosure and Report Findings. Some of the replicated studies [25, 84] aim at discovering vulnerable code snippets. Replicating their methodology on a newer Stack Overflow data set can result in discovering additional snippets with weaknesses. While discovered vulnerabilities in other code bases (e.g., production or open-source software) should be responsibly disclosed to vendors/developers, there are no guidelines about disclosure for publicly posted code snippets. While the technical option exists to add a comment2 on each post with a vulnerable snippet, we found this to be an ethical dilemma. First, the vulnerability does not affect Stack Overflow but only developers that copy such snippets [3] Joern: The bug hunter’s workbench. [Online]. Available: into their code bases. Thus, the disclosure might not reach the affected parties. Second, the employed methodologies only discover weaknesses, but without a concrete explanation of the vulnerability and the corresponding fix, a comment would not benefit the community. Third, without careful consideration of the context of the snippet, commenting on weaknesses can easily create noise and even be considered offensive/use less (e.g., if the original question asked about an explanation of a vulnerability, i.e., the vulnerability was posted on pur pose). Without being able to address the second and third concerns at scale, such auto-commenting of weaknesses would also violate the Stack Overflow code of conduct.3 We further consulted the Stack Exchange Meta discourse4 about how vulnerabilities in code snippets should be reported. The meta-discussions mirror, to some extent, our concerns. For example, that mass commenting will create noise5 and that such discoveries should be accompanied by code fixes6. The community also discussed other measures, such as introducing a “security” or “caution” flag to posts with vulnerabilities or outdated security measures.7 However, the community also agrees on the sentiment that while code snippets could be copied & pasted, Stack Overflow is a teaching platform for developers to learn how to solve their specific problems and that authored code should be owned, hence, not just pasted and in stead, the solutions on the platform should be scrutinized and lead to further education and ultimately custom solutions.8 Since it is currently impossible to make comments/edits of the required quality, we did not create fixes for newly discovered posts with weaknesses for the above-stated reasons. We note that neither Zhang et al. [84] nor Fischer et al. [25] mentioned any attempted disclosure on Stack Overflow—Fischer et al., however, in follow-up work [27], built a browser plugin to warn Stack Overflow users of insecure snippets."
Framework Used: []
Indirect Stakeholders: []
key_quotes: ""
Menlo.Beneficience: false
Menlo.Justice: false
Menlo.RespectForLawAndPublicInterest: false
Menlo.RespectForPersons: false
notes: ""
pages: 2809--2828
Research Domain:
  - Software Security & Development Lifecycle
Research_Type: []
Risk Benefit Analysis: false
Status: Ethics Section Extracted
Subdomain:
  - Software Security and Usable Security
title: "Stack Overflow Meets Replication: Security Research Amid Evolving Code Snippets"
url: https://www.usenix.org/conference/usenixsecurity25/presentation/jallow
Usenix.DataPrivacy: false
Usenix.HarmMitigation: false
Usenix.HumanSubjects: false
Usenix.LiveTesting: false
Usenix.ResearcherSafety: false
Usenix.StakeholderImpact: false
Usenix.ToSViolation: false
Usenix.VulnDisclosure: false
coded_date: 2026-09-11
---
