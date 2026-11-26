---
Alternatives Considered: false
author: Nima Naderloui and Shenao Yan and Binghui Wang and Jie Fu and Wendy Hui Wang and Weiran Liu and Yuan Hong
author_tags:
  - Nima Naderloui
  - Shenao Yan
  - Binghui Wang
  - Jie Fu
  - Wendy Hui Wang
  - Weiran Liu
  - Yuan Hong
base: "[[Databook.base]]"
DBLP Ref: DBLP:conf/uss/NaderlouiYW0WL025
Direct Stakeholders: []
Emerging Themes: []
Ethics Depth:
Ethics Location: []
Ethics section: In accordance with the USENIX Security ethics guidelines, we have thoroughly considered the ethical implications of our work. RULI is a framework designed to evaluate the privacy risks and efficacy of unlearning methods. It alerts researchers and practitioners to carefully evaluate unlearning methods that promote the development of more effective unlearning strategies. By exposing empirical risks, RULI raises awareness of potential privacy issues that may be overlooked in current unlearning methods before deployment in practice. We acknowledge the potential for misuse, as RULI (its attack part) could be employed by malicious actors to attack real-world models that claim to have unlearned specific data. However, we believe the research benefits outweigh these risks. Our findings offer practical mitigation strategies (in the Appendix). One approach is to improve unlearning designs by accounting for variation in memorization and privacy risks across samples, rather than treating all samples equally. This may require estimating and ranking the privacy risk of individual samples, which, while potentially costly, is feasible in systems designed with privacy in mind. Another mitigation strategy is to restrict the types of queries users can perform, such as limiting access to logit outputs or confidence scores, to reduce the potential for exploitation. All experiments in our study were conducted using opensource datasets and models. The privacy attacks were simulated solely for the purpose of evaluation, and no real-world, confidential, or sensitive data were used. No individuals or organizations are impacted by these experiments. As such, Institutional Review Board (IRB) approval was not required.
Framework Used: []
Indirect Stakeholders: []
kanban_order: 31
key_quotes: ""
Menlo.Beneficience: false
Menlo.Justice: false
Menlo.RespectForLawAndPublicInterest: false
Menlo.RespectForPersons: false
notes: ""
pages: 5545--5564
Research Domain:
  - Machine Learning & AI (non-LLM)
Research_Type: []
Risk Benefit Analysis: false
Status: Ethics Section Extracted
Subdomain:
  - ML and AI Privacy
title: "Rectifying Privacy and Efficacy Measurements in Machine Unlearning: {A} New Inference Attack Perspective"
url: https://www.usenix.org/conference/usenixsecurity25/presentation/naderloui
Usenix.DataPrivacy: false
Usenix.HarmMitigation: false
Usenix.HumanSubjects: false
Usenix.LiveTesting: false
Usenix.ResearcherSafety: false
Usenix.StakeholderImpact: false
Usenix.ToSViolation: false
Usenix.VulnDisclosure: false
coded_date: 2026-08-27
---
