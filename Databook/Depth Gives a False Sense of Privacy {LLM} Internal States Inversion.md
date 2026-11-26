---
Alternatives Considered: false
author: Tian Dong and Yan Meng and Shaofeng Li and Guoxing Chen and Zhen Liu and Haojin Zhu
author_tags:
  - Tian Dong
  - Yan Meng
  - Shaofeng Li
  - Guoxing Chen
  - Zhen Liu
  - Haojin Zhu
base: "[[Databook.base]]"
DBLP Ref: DBLP:conf/uss/Dong00C0Z25
Direct Stakeholders: []
Emerging Themes: []
Ethics Depth:
Ethics Location: []
Ethics section: "Our attacks exploit ISs of models to invert nearly original sensitive input, posing significant threats to user privacy and data security. As our research do not involve human participants and only use public medical dialogue, Mentalhealth and coding datasets, the IRB of authors’ intuition, after our consultation, determined that our research does not require further review. We acknowledge that exemption from IRB review may not fully address all ethical considerations, and have therefore taken the following steps.\r

  Ensuring no harm is caused to stakeholders. The potential stakeholders include LLM user and LLM service provider and broader privacy community. To mitigate potential harms to individuals, by following existing privacy work, we only select public datasets that are highly-downloaded and appropriately anonymized. In addition, we also manually checked all datasets used in our research to ensure there is no sensitive information (e.g., PII) exposed in our research. We did not attack real-world collaborative inference systems, so no individual privacy is leaked by our research. As for the models, we only used opensource models including Llama, Qwenand T5 in our work for compliance with model-use license.\r

  Responsible disclose to service providers. We also share our findings with main cloud LLM service providers that might deploy collaborative inference including OpenAI, Meta AI and Qwen. We recognize that this cannot perfectly mitigate privacy risks, because our attacks, if known to the public, may still be misused by the actual collaborative inference server or IS auditor to recover the user inputs. However, we believe the benefits of publicizing our attacks outweight the potential harm. As our work demonstrates the potential privacy risks of LLMISs, it will draw increased attention to, not only the ISs inversion threat, but also the general privacy concerns sur rounding LLM service systems. This will encourage the LLM practitioners to proactively implement well-established solutions like confidential virtual machine within their systems to offer better privacy protection."
Framework Used: []
Indirect Stakeholders: []
key_quotes: ""
Menlo.Beneficience: false
Menlo.Justice: false
Menlo.RespectForLawAndPublicInterest: false
Menlo.RespectForPersons: false
notes: ""
pages: 1629--1648
Research Domain:
  - Large Language Models (LLM)
Research_Type: []
Risk Benefit Analysis: false
Status: Ethics Section Extracted
Subdomain:
  - LLM Privacy
title: "Depth Gives a False Sense of Privacy: {LLM} Internal States Inversion"
url: https://www.usenix.org/conference/usenixsecurity25/presentation/dong-tian
Usenix.DataPrivacy: false
Usenix.HarmMitigation: false
Usenix.HumanSubjects: false
Usenix.LiveTesting: false
Usenix.ResearcherSafety: false
Usenix.StakeholderImpact: false
Usenix.ToSViolation: false
Usenix.VulnDisclosure: false
coded_date: 2026-09-07
---
