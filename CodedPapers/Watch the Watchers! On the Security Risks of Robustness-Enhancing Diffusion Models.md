---
Alternatives Considered: false
author: Changjiang Li and Ren Pang and Bochuan Cao and Jinghui Chen and Fenglong Ma and Shouling Ji and Ting Wang
author_tags:
  - Changjiang Li
  - Ren Pang
  - Bochuan Cao
  - Jinghui Chen
  - Fenglong Ma
  - Shouling Ji
  - Ting Wang
base: "[[Databook.base]]"
coded_date: 2026-05-29
DBLP Ref: DBLP:conf/uss/LiPCCMJ025
Direct Stakeholders:
  - Software Maintainers
Emerging Themes:
  - Stakeholder Identification
Ethics Depth:
  - Detailed
Ethics Location:
  - Main Body
Ethics section: This study investigates the vulnerabilities in diffusion models applied to enhance the robustness of AI systems. While these models have demonstrated promise as defensive tools—particularly in purifying adversarial examples and certifying adversarial robustness—their own susceptibility to attacks remains underexplored. This work reveals criti cal weaknesses in these models, showing how they can be compromised in ways that not only diminish their protective capabilities but also risk creating a false sense of security among stakeholders. Stakeholder Considerations. This work has implications for diffusion model developers, users, and the broader security community. While our findings may affect trust in diffusion models for critical systems, exposing these vulnerabilities enables the development of stronger defenses and ultimately more secure systems. Responsible Disclosure. We examine security vulnerabilities in diffusion models when used as defensive tools, particularly for adversarial purification and robustness certification. Since these defensive applications remain in the research phase rather than deployed systems, we present our findings as preventive guidance for the research community before real-world deployment. Potential Harms and Benefits. Our findings can have dual effects. In the short term, they may temporarily weaken con fidence in diffusion models as defensive tools, potentially leading to their underutilization and exposing AI systems to unmitigated risks. In the long term, by illuminating such weaknesses, this work promotes a deeper understanding of the limitations of robustness-enhancing diffusion models and facilitates the development of more resilient solutions, ulti mately benefiting the security ecosystem. Mitigation of Negative Outcomes and Future Research. This work also outlines several potential countermeasures (e.g., detection of suspicious inputs based on classification entropy) to mitigate the identified vulnerabilities. The preliminary results suggest the promise of these countermeasures, which serve as a roadmap for both future research and practical security enhancement. In addition, we are committed to further advancing this research, aiming to develop more effective defenses that strengthen diffusion models for deployment in security-critical environments.
Framework Used:
  - USENIX Guidelines
Indirect Stakeholders:
  - End Users
kanban_order: 0
key_quotes: ""
Menlo.Beneficience: true
Menlo.Justice: false
Menlo.RespectForLawAndPublicInterest: false
Menlo.RespectForPersons: false
notes: The paper introduces DIFF2, a novel attack against defensive diffusion models. The ethics section is comprehensive, with a subsection for risk-benefit analysis, consideration for stakeholders and responsible disclosure. It appears to have addressed the points raised in the USENIX ethical guidelines, and recognises the ethical responsibility of a researching a possible vulnerability.
pages: 997--1016
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
title: Watch the Watchers! On the Security Risks of Robustness-Enhancing Diffusion Models
url: https://www.usenix.org/conference/usenixsecurity25/presentation/li-changjiang
Usenix.DataPrivacy: false
Usenix.HarmMitigation: true
Usenix.HumanSubjects: false
Usenix.LiveTesting: false
Usenix.ResearcherSafety: false
Usenix.StakeholderImpact: true
Usenix.ToSViolation: false
Usenix.VulnDisclosure: true
---
