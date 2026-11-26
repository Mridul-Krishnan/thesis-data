---
Alternatives Considered: false
author: Andr{\'{e}}s F{\'{a}}brega and Samuel Breckenridge and Armin Namavari and Thomas Ristenpart
author_tags:
  - Andr{\'{e}}s F{\'{a}}brega
  - Samuel Breckenridge
  - Armin Namavari
  - Thomas Ristenpart
base: "[[Databook.base]]"
DBLP Ref: DBLP:conf/uss/FabregaBNR25
Direct Stakeholders: []
Emerging Themes: []
Ethics Depth:
Ethics Location: []
Ethics section: "In our work, we propose principled mitigations for injection attacks on E2EE applications, and evaluate their performance using workloads that reflect real-world use scenarios. Below, we describe the ethical considerations raised by our work.\r

  Privacy of experimental workloads. The usernames and passwords for the input data come from SecLists and the Uncompressed database size (MB) URLs come from Tranco,as we discuss in Section 7. SecLists is a testing tool for security applications that includes public datasets. Tranco maintains a list of top-ranked websites. Given that these data sources are public and widely available, our usage of them to generate workloads does not put users at risk of security or privacy breaches. In addition, we used a large language model to generate synthetic message data for our WhatsApp workloads. By doing so, we avoid compromising the privacy of real user messages.\r

  Addressing unresolved vulnerabilities. Many existing E2EE applications have either partial or, in some cases,no mitigations for the injection attacks that we address in this paper.\r

  However, these attacks have been established in prior work, and are public knowledge. Although mentioning them can in crease awareness of their existence, we do so in a constructive way and provide a concrete solution to protect against them.\r

  We are also reaching out to affected platforms to make them aware of the mitigations we propose."
Framework Used: []
Indirect Stakeholders: []
key_quotes: ""
Menlo.Beneficience: false
Menlo.Justice: false
Menlo.RespectForLawAndPublicInterest: false
Menlo.RespectForPersons: false
notes: ""
pages: 2965--2984
Research Domain:
  - Software Security & Development Lifecycle
Research_Type: []
Risk Benefit Analysis: false
Status: Ethics Section Extracted
Subdomain:
  - Software Security and Usable Security
title: Mitigating Injection Attacks against {E2EE} Applications via View-Based Partitioning
url: https://www.usenix.org/conference/usenixsecurity25/presentation/fabrega-partitioning
Usenix.DataPrivacy: false
Usenix.HarmMitigation: false
Usenix.HumanSubjects: false
Usenix.LiveTesting: false
Usenix.ResearcherSafety: false
Usenix.StakeholderImpact: false
Usenix.ToSViolation: false
Usenix.VulnDisclosure: false
coded_date: 2026-09-08
---
