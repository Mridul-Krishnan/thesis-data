---
Alternatives Considered: false
author: Jiawen Zhang and Kejia Chen and Lipeng He and Jian Lou and Dan Li and Zunlei Feng and Mingli Song and Jian Liu and Kui Ren and Xiaohu Yang
author_tags:
  - Jiawen Zhang
  - Kejia Chen
  - Lipeng He
  - Jian Lou
  - Dan Li
  - Zunlei Feng
  - Mingli Song
  - Jian Liu
  - Kui Ren
  - Xiaohu Yang
base: "[[Databook.base]]"
DBLP Ref: DBLP:conf/uss/00050H0LFS00025
Direct Stakeholders: []
Emerging Themes: []
Ethics Depth:
Ethics Location: []
Ethics section: "The main contribution of this work is the identification and mitigation of safety risks posed by the widely applied inference efficiency improvement techniques of activation approximation, rather than the introduction of a jailbreak attack. The safety vulnerabilities identified in this paper arise from various mainstream activation approximation techniques that have been extensively studied in the academic literature and are commonly implemented in practice. Through comprehensive safety evaluations and analyses, we propose an enhanced alignment method, QuadA (detailed in Section 4), which enables LLM developers to build models resilient to these activation approximations, thereby restoring safety capabilities when employing these techniques.\r

  The main misuse risk involves LLM-based service providers intentionally exploiting activation approximations to circumvent safety measures. However, this requires de tailed knowledge of model internals, deliberate modifications to inference procedures, and tolerance for utility degradation.\r

  A more pressing concern is the inadvertent safety degradation already occurring in deployed LLM-based services that use activation approximations without recognizing their safety implications. Our research addresses this gap by offering both diagnostic insights and effective mitigation strategies.\r

  Through this work, we aim to help the community under stand the safety implications of common deployment optimizations and adopt defensive measures using the QuadA method, ensuring that inference efficiency improvements do not inadvertently undermine safety alignment. Finally, throughout our research, we have taken ethical considerations into account to uphold responsible and ethical practices. 1) We ensure the well-being of our team members who may be exposed to harmful content during safety evaluations by establishing protocols to manage mental stress and providing psychological support if needed. 2) We confine our safety tests to our own computational resources to avoid impacting others. When the use of the GPT API is necessary, we con duct all testing under our own account, ensuring no effect on other users. 3) In accordance with the Coordinated Vulnerability Disclosure protocol, we have communicated our safety evaluation findings to all affected organizations, including Meta, Microsoft, Alibaba Qwen, and Mistral AI, before submitting our revision. Specifically, we informed them via email about the potential safety vulnerabilities in their open-source LLMs resulting from the application of various activation approximation techniques."
Framework Used: []
Indirect Stakeholders: []
key_quotes: ""
Menlo.Beneficience: false
Menlo.Justice: false
Menlo.RespectForLawAndPublicInterest: false
Menlo.RespectForPersons: false
notes: ""
pages: 339--358
Research Domain:
  - Large Language Models (LLM)
Research_Type: []
Risk Benefit Analysis: false
Status: Ethics Section Extracted
Subdomain:
  - LLM Security
title: "Activation Approximations Can Incur Safety Vulnerabilities in Aligned LLMs: Comprehensive Analysis and Defense"
url: https://www.usenix.org/conference/usenixsecurity25/presentation/zhang-jiawen
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
