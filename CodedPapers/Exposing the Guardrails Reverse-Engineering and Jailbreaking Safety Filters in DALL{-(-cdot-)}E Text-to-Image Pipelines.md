---
Alternatives Considered: false
author: Corban Villa and Muhammad Shujaat Mirza and Christina P{\"{o}}pper
author_tags:
  - Corban Villa
  - Muhammad Shujaat Mirza
  - Christina P{\"{o}}pper
base: "[[Databook.base]]"
DBLP Ref: DBLP:conf/uss/VillaMP25
Direct Stakeholders:
  - Research Team
  - Software Maintainers
Emerging Themes:
  - Mitigation
Ethics Depth:
  - Brief
Ethics Location:
  - Main Body
Ethics section: "We do not cause harm to the T2I systems as we are using them as a regular user within the existing rate limits. The nature of this work, however, introduces the potential exposure to harmful content through both text-based prompts and images generated. In order to minimize this potential harm, the authors of this work are the only ones subject to interacting with these artifacts. In addition, automation is employed when possible to minimize the extent and scale of interaction with harmful content. This methodology is consistent with previous work [36, 50]. While we do propose a number of novel attacks for T2I systems, we also introduce a number of countermeasures that mitigate these new vulnerabilities. We intend this work to provide a robust basis for safety guardrails to build upon, providing an increased degree of safety. Responsible Disclosure: The vulnerability discovered in the DALL·E 3 interface was disclosed to OpenAI on October 19th, 2024, and acknowledged on October 22nd, 2024. To minimize the potential for misuse, this paper has been preemptively shared with OpenAI prior to its publication."
Framework Used:
  - None Explicit
Indirect Stakeholders:
  - Adversaries
  - Broader Public
kanban_order: 5
key_quotes: ""
Menlo.Beneficience: false
Menlo.Justice: false
Menlo.RespectForLawAndPublicInterest: true
Menlo.RespectForPersons: false
notes: The ethics section is brief, however it covers vuln disclosure and addresses the risk vs benefits by highlighting the countermeasures to improve the robustness of the railguards. Mitigations to the attacks introduced are discussed in the Countermeasures section.
pages: 897--916
Research Domain:
  - Machine Learning & AI (non-LLM)
Research_Type:
  - Vuln Research
  - Theory
Risk Benefit Analysis: true
Status: Data coded
Subdomain:
  - ML and AI Security
  - Images
title: "Exposing the Guardrails: Reverse-Engineering and Jailbreaking Safety Filters in DALL{\\(\\cdot\\)}E Text-to-Image Pipelines"
url: https://www.usenix.org/conference/usenixsecurity25/presentation/villa
Usenix.DataPrivacy: false
Usenix.HarmMitigation: true
Usenix.HumanSubjects: false
Usenix.LiveTesting: true
Usenix.ResearcherSafety: false
Usenix.StakeholderImpact: false
Usenix.ToSViolation: false
Usenix.VulnDisclosure: true
coded_date: 2026-11-01
---
