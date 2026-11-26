---
Alternatives Considered: false
author: Xiang Li and Ying Meng and Junming Chen and Lannan Luo and Qiang Zeng
author_tags:
  - Xiang Li
  - Ying Meng
  - Junming Chen
  - Lannan Luo
  - Qiang Zeng
base: "[[Databook.base]]"
DBLP Ref: DBLP:conf/uss/LiMCL025
Direct Stakeholders: []
Emerging Themes: []
Ethics Depth:
Ethics Location: []
Ethics section: "Our paper proposes a novel inference-stage backdoor attack, ONEFLIP, which injects a backdoor into a full-precision model via a single bit flip. This work aims to advance the understanding of model vulnerabilities and support the development of more robust machine learning systems. However, we acknowledge the potential security risks of such research.\r

  ONEFLIP may threaten stakeholders such as MLaaS providers on multi-tenant platforms and their users. A successful attack could compromise models of MLaaS, damage the reputation of their providers and users, and pose public safety risks in applications like autonomous driving or medical imaging. We carefully evaluated the likelihood of real-world harm from ONEFLIP and identified several factors that mitigate its prac tical threat level. First, ONEFLIP assumes white-box access, meaning the attacker must obtain the target model, while many companies keep their models confidential. Second, the attacker-controlled process must reside on the same physi cal machine as the target model, which may be difficult to achieve. Overall, we conclude that while the theoretical risks are non-negligible, the practical risk remains low, and the potential benefit of exposing previously unknown vulnerabilities outweighs these concerns. All experiments of the study were conducted on publicly available datasets and models within a private execution environment. Additionally, we note that Rowhammer is a publicly known hardware vulnerability; our work does not introduce new attack vectors at the hardware level, and thus, no additional disclosure is warranted."
Framework Used: []
Indirect Stakeholders: []
kanban_order: 35
key_quotes: ""
Menlo.Beneficience: false
Menlo.Justice: false
Menlo.RespectForLawAndPublicInterest: false
Menlo.RespectForPersons: false
notes: ""
pages: 6319--6337
Research Domain:
  - Machine Learning & AI (non-LLM)
Research_Type: []
Risk Benefit Analysis: false
Status: Ethics Section Extracted
Subdomain:
  - ML and AI Security
  - Backdoors Poisoning Unlearning
title: "Rowhammer-Based Trojan Injection: One Bit Flip Is Sufficient for Backdooring DNNs"
url: https://www.usenix.org/conference/usenixsecurity25/presentation/li-xiang
Usenix.DataPrivacy: false
Usenix.HarmMitigation: false
Usenix.HumanSubjects: false
Usenix.LiveTesting: false
Usenix.ResearcherSafety: false
Usenix.StakeholderImpact: false
Usenix.ToSViolation: false
Usenix.VulnDisclosure: false
coded_date: 2026-08-28
---
