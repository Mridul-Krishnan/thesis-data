---
Alternatives Considered: false
author: Shuai Cheng and Shu Meng and Haitao Xu and Haoran Zhang and Shuai Hao and Chuan Yue and Wenrui Ma and Meng Han and Fan Zhang and Zhao Li
author_tags:
  - Shuai Cheng
  - Shu Meng
  - Haitao Xu
  - Haoran Zhang
  - Shuai Hao
  - Chuan Yue
  - Wenrui Ma
  - Meng Han
  - Fan Zhang
  - Zhao Li
base: "[[Databook.base]]"
DBLP Ref: DBLP:conf/uss/ChengM0ZHYMHZL25
Direct Stakeholders: []
Emerging Themes: []
Ethics Depth:
Ethics Location: []
Ethics section: "This research acknowledges the potential extraction of genuine personal data from publicly available LLMs, presenting ethical challenges concerning privacy infringement, accidental disclosure, and potential misuse for harmful purposes. We present the ethical considerations, encompassing the study’s justification, identified risks, and implemented safeguards to address these concerns.\r

  Key Stakeholders. Our research involves four key stake holder groups: (1) individuals whose personal data may reside in LLM training sets (protected through rigorous anonymization and prompt data deletion); (2) LLM developers (who benefit from security vulnerability disclosures despite initial reputational impacts); (3) the academic research community (whose work in AI safety and privacy preservation may ad vance through these findings); and (4) potential malicious actors (whose ability to exploit identified vulnerabilities is constrained through careful disclosure practices that omit technical implementation details).\r

  Risk Mitigation and Disclosure Considerations. To up hold stringent ethical standards, we implemented comprehensive safeguards including aggregated result reporting, permanent PII erasure, and exclusion of sensitive data from public repositories. These IRB-approved protocols ensure compliance with non-human research requirements, supplemented by periodic ethical reviews to address emerging concerns.\r

  Our responsible disclosure framework balances security enhancement with risk prevention, presenting findings to maximize defensive utility while omitting exploitable technical specifics. This includes proactive collaboration with major LLM providers (OpenAI, Anthropic), who verified existing protections through compliance audits while endorsing full publication of results.\r

  Discussion of Alternative Approaches. In this study, we evaluated alternative approaches for assessing LLM security without exposing PII or enabling the generation of sensitive content. While synthetic datasets and anonymized text were explored as privacy-preserving options, they failed to adequately measure models’ actual PII memorization capabilities. Controlled experimentation emerged as the only viable method for comprehensively evaluating these risks. The critical security insights obtained- particularly in identifying vulnerabilities and developing defenses- warranted this approach when conducted with rigorous protective measures.\r

  Team Wellbeing. We implemented comprehensive wellbeing protocols to support our research team throughout this ethically complex study. Recognizing the psychological demands of working with sensitive data, we established robust mental health resources and maintained an open culture encouraging ongoing ethical discourse and continuous feedback."
Framework Used: []
Indirect Stakeholders: []
key_quotes: ""
Menlo.Beneficience: false
Menlo.Justice: false
Menlo.RespectForLawAndPublicInterest: false
Menlo.RespectForPersons: false
notes: ""
pages: 8155--8173
Research Domain:
  - Large Language Models (LLM)
Research_Type: []
Risk Benefit Analysis: false
Status: Ethics Section Extracted
Subdomain:
  - Vulnerabilities in LLMs
  - Privacy Safety and Defense
title: Effective {PII} Extraction from LLMs through Augmented Few-Shot Learning
url: https://www.usenix.org/conference/usenixsecurity25/presentation/cheng-shuai
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
