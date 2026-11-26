---
Alternatives Considered: true
author: Jiate Li and Binghui Wang
author_tags:
  - Jiate Li
  - Binghui Wang
base: "[[Databook.base]]"
DBLP Ref: DBLP:conf/uss/LiW25
Direct Stakeholders:
  - Research Team
  - Software Maintainers
Emerging Themes:
  - Stakeholder Identification
Ethics Depth:
  - Detailed
Ethics Location:
  - Main Body
Ethics section: "This research strictly adheres to ethical guidelines and responsibilities, ensuring compliance with established standards. 1) Identification of Stakeholders Researchers: Those advancing the field by building upon this work, focusing on both defending GNNs against adversarial attacks and exploring trustworthy GNNs (e.g., against training-time poisoning attacks and both training- and test time backdoor attacks) in general. Developers and Practitioners of AI Systems: Individuals and organizations implementing or applying provably robust GNNs in real-world graph-related applications such as fraud detection in social networks, web, online auction networks, intrusion detection, and software vulnerability detection. End-users: People interacting with GNN-powered systems, including users of social networks, recommender systems, or financial platforms. Society at Large: Individuals impacted by ethical considerations and risks associated with deploying AI technologies, especially in domains leveraging GNNs (e.g., social networks, healthcare, finance). 2) Potential Risks for Stakeholders and Mitigations For Researchers. Potential Risk: Adversaries may develop novel attacks that surpass the guaranteed bounds of the considered threat model (e.g., perturbations beyond the certified perturbation size). Mitigation: With larger perturbations on graph data, those perturbed graphs might have significant differences with normal graphs. Therefore, researchers can lever age detection methods, such as structural-similarity based methods, to identify the perturbed graphs. Researchers can also collaborate with ethics experts to ensure that the research aligns with best practices for responsible AI development. For Developers and Practitioners. Potential Risk: The pro posed defense method may not generalize well to other graph learning applications that are different from the considered applications. Mitigation: Comprehensive empirical validation across diverse graph datasets and real-world scenarios ensures robustness. Clear communication of limitations will help developers manage risks effectively. For End-users. Potential Risk: Robust GNN mechanisms might inadvertently compromise data privacy or produce biased outcomes. Mitigation: Incorporating privacy-preserving (such as differential privacy and cryptographic methods) and fair training techniques enhances data security and fairness. For Society. Potential Risk: Misuse of robust GNNs in critical domains (e.g., healthcare, finance) could exacerbate social inequities, privacy breaches, or manipulation of vulnerable populations. Mitigation: Balancing AI security advancements with societal considerations (including fairness, transparency, and accountability) mitigates potential harm. Ethical implications for vulnerable populations will be addressed, prioritizing societal well-being. 3) Considerations Motivating Ethical-Related Decisions Research Goal: The primary objective is to enhance the robustness of GNNs against adversarial attacks while minimizing potential harm to stakeholders. Defense strategies are designed to be both practical and ethical. Benefits and Harms: Benefits: Improved robustness of GNN systems reduces risks of adversarial manipulation and protecting users. Harms: Potential empowerment of malicious actors and overestimating the effectiveness of defense methods. Rights: We are particularly concerned with privacy rights, as adversarial attacks can sometimes expose sensitive data or violate individuals’ privacy. Our defense strategies aim to mitigate such risks, promoting the ethical use of GNNs while safeguarding individuals’ rights. 4) Awareness of Ethical Perspectives We are aware that different members of the research community may hold differing views on the ethical implications of trustworthy AI. Some may prioritize transparency in revealing attack strategies to help build better defenses, while others may argue that such knowledge could be misused. In line with the principles of responsible AI research, we have opted to emphasize defense over offense, focusing on methods that mitigate risk without creating new avenues for harm."
Framework Used:
  - Custom
Indirect Stakeholders:
  - End Users
  - Broader Public
kanban_order: 9
key_quotes: ""
Menlo.Beneficience: true
Menlo.Justice: true
Menlo.RespectForLawAndPublicInterest: true
Menlo.RespectForPersons: true
notes: The ethics section includes stakeholder identification, as well as risks and mitigations for them. It is a defensive tool for GNNs, and does not discover any new vulnerability. The "Awareness if Ethical Perspectives" section covers alternatives considered from an ethical sense. Overall, the ethics section is very comprehensive and considers the paper from many angles. While there is no usability analysis, the "Discussion and Limitations" section does cover the possible usecases where their tool performs or underperforms.
pages: 7251--7270
Research Domain:
  - Machine Learning & AI (non-LLM)
Research_Type:
  - System
  - Theory
Risk Benefit Analysis: true
Status: Data coded
Subdomain:
  - ML and AI Security
  - Robustness
title: "AGNNCert: Defending Graph Neural Networks against Arbitrary Perturbations with Deterministic Certification"
url: https://www.usenix.org/conference/usenixsecurity25/presentation/li-jiate
Usenix.DataPrivacy: false
Usenix.HarmMitigation: true
Usenix.HumanSubjects: false
Usenix.LiveTesting: false
Usenix.ResearcherSafety: false
Usenix.StakeholderImpact: true
Usenix.ToSViolation: false
Usenix.VulnDisclosure: false
coded_date: 2026-09-30
---
