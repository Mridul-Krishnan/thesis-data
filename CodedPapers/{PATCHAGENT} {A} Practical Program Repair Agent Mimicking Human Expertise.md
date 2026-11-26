---
Alternatives Considered: false
author: Zheng Yu and Ziyi Guo and Yuhang Wu and Jiahao Yu and Meng Xu and Dongliang Mu and Yan Chen and Xinyu Xing
author_tags:
  - Zheng Yu
  - Ziyi Guo
  - Yuhang Wu
  - Jiahao Yu
  - Meng Xu
  - Dongliang Mu
  - Yan Chen
  - Xinyu Xing
base: "[[Databook.base]]"
coded_date: 2026-02-20T15:47:00
DBLP Ref: DBLP:conf/uss/0003G00XM0025
Direct Stakeholders:
  - Software Maintainers
Emerging Themes:
  - LLM Ethics
Ethics Depth: Minimal
Ethics Location:
  - Main Body
Ethics section: In developing PATCHAGENT, an LLM-based agent designed to repair software vulnerabilities, we took careful consideration of ethical guidelines and compliance standards. The system was developed and tested in a controlled environment, specifically on a private server, ensuring that no unauthorized data or external systems (other than the LLM service providers) were involved in the process. At the dataset level, we collect the cases from open-source projects, which ensures the transparency and accessibility of all test cases. The primary function of PATCHAGENT is to enhance software security by automatically repairing vulnerabilities, which inherently aligns with ethical goals of improving cybersecurity and protecting users from potential harm. We ensured that the agent operates within a defined scope, with no capability to perform actions outside its intended purpose, thus minimizing any risk of unintended consequences. Throughout the development and experimentation phases, all activities adhered to established ethical standards and legal requirements, confirming that our work does not violate any regulations or ethical principles.
Framework Used:
  - None Explicit
Indirect Stakeholders:
  - End Users
key_quotes: In this paper, we introduce PatchAgent, a novel LLM-based APR tool that seamlessly integrates fault localization, patch generation, and validation within a single autonomous agent. PatchAgent employs a language server, a patch verifier, and interaction optimization techniques to mimic human-like reasoning during vulnerability repair. Evaluated on a dataset of 178 real-world vulnerabilities, PatchAgent successfully repairs over 90% of the cases, outperforming state-of-the-art APR tools where applicable. Our ablation study further offers insights into how various interaction optimizations contribute to PatchAgent's effectiveness.
Menlo.Beneficience: true
Menlo.Justice: false
Menlo.RespectForLawAndPublicInterest: true
Menlo.RespectForPersons: false
notes: As the tool works with patched vuln/exploits and experiments ensured that the testing and usage of the LLM services were in a controlled environment, no additional stakeholder are required to be addressed. The tool requires the existence of at least one PoC test case in order to proceed, so a human component is involved still at the start of the APR and doesn’t rely solely on the LLM for any new information. A sample comparison is done between vanilla LLM and Human expert to identify the gaps, and optimisations are made to address them, the author acknowledges that further optimization components would be required as more gaps between PATCHAGENT and Human experts are identified.
pages: 4381--4400
Research Domain:
  - Software Security & Development Lifecycle
Research_Type:
  - System
  - Theory
Risk Benefit Analysis: false
Status: Data coded
Subdomain:
  - Software Security
  - Patching and Repair
title: "{PATCHAGENT:} {A} Practical Program Repair Agent Mimicking Human Expertise"
url: https://www.usenix.org/conference/usenixsecurity25/presentation/yu-zheng
Usenix.DataPrivacy: false
Usenix.HarmMitigation: false
Usenix.HumanSubjects: false
Usenix.LiveTesting: false
Usenix.ResearcherSafety: false
Usenix.StakeholderImpact: false
Usenix.ToSViolation: false
Usenix.VulnDisclosure: false
---
