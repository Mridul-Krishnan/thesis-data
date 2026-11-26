---
Alternatives Considered: false
author: Yushu Zhang and Yuanyuan Sun and Shuren Qi and Zhongyun Hua and Wenying Wen and Yuming Fang
author_tags:
  - Yushu Zhang
  - Yuanyuan Sun
  - Shuren Qi
  - Zhongyun Hua
  - Wenying Wen
  - Yuming Fang
base: "[[Databook.base]]"
coded_date: 2026-02-12T18:01:00
DBLP Ref: DBLP:conf/uss/0001SQHWF25
Direct Stakeholders:
  - System Operators
Emerging Themes:
  - Adversarial Vuln to NN
Ethics Depth: Detailed
Ethics Location:
  - Main Body
Ethics section: |-
  Perceptual hashing is a crucial tool for regulating image con
  tent that violates basic human rights. Our study reveals poten
  tial vulnerabilities of such hashing techniques, exploring the feasibility for escaping or triggering regulation. Intuitively,
  • The pHash, PDQ, PhotoDNA, and NeuralHash models.
  there is an ethical risk that our attack methods could be mis
  used by malicious actors. On the other hand, the security
  community has long argued that openness and adversarial
  scrutiny are essential for ensuring the correct operation of sys
  tems, maintaining that “security by obscurity” is a fragile and
  ineffective approach to protecting high-value systems. This is
  because, without disclosing these vulnerabilities, the indus
  try is often reluctant to invest in improvements. Therefore,
  the benefits of conducting this analysis to enhance security
  and resilience outweigh the potential risks associated with
  disclosing our findings.
  To minimize potential ethical risks, we have implemented
  the following measures.
  • Technical countermeasures. From our findings, we of
  fer possible technical countermeasures: 1) fundamentally
  improving the representation robustness, 2) introduc
  ing more complexity into the system, and 3) developing
  perturbation detectors as data preprocessing. We will
  disclose our vulnerability findings, technical counter
  measures, and source code to the relevant stakeholders,
  e.g., Apple, Facebook, and Microsoft, with the hope of
  collaborating on more robust E2EE-PHM systems.
  • Remediation period. We set a remediation period for
  responsible disclosure practices. During this period, we
  will contact the relevant stakeholders with all necessary
  materials to repair the E2EE-PHM vulnerabilities, be
  fore an adversary gains the attack capability. During
  this period, our paper itself contains no sufficient imple
  mentation details, and the source code is only available
  to identified reviewers. After this period, we are will
  ing to disclose the source code completely so that other
  researchers can validate and build upon it.
  • Wellbeing for team members. Although our research
  focuses on the regulation of image content that violates
  basic human rights, we did not use any illegal images,
  such as child pornography, terrorism, drugs, and violent
  crime, during the study. This is because harmless images
  are equivalent to illegal images in terms of their E2EE
  PHM processing. Therefore, our study does not pose any
  psychological harm to team members
Framework Used:
  - USENIX Guidelines
Indirect Stakeholders:
  - Broader Public
key_quotes: |-
  “ Intuitively,
  • The pHash, PDQ, PhotoDNA, and NeuralHash models.
  there is an ethical risk that our attack methods could be mis
  used by malicious actors. On the other hand, the security
  community has long argued that openness and adversarial
  scrutiny are essential for ensuring the correct operation of sys
  tems, maintaining that “security by obscurity” is a fragile and
  ineffective approach to protecting high-value systems. This is
  because, without disclosing these vulnerabilities, the indus
  try is often reluctant to invest in improvements. Therefore,
  the benefits of conducting this analysis to enhance security
  and resilience outweigh the potential risks associated with
  disclosing our findings.”
Menlo.Beneficience: true
Menlo.Justice: true
Menlo.RespectForLawAndPublicInterest: true
Menlo.RespectForPersons: true
notes: |-
  “ Possible Countermeasures and Recommendations for Social Good” is another section in the paper which discusses possible mitigation so the ATKSCOPES tool, including using the tool to create more training samples for Adversarial Training.
  In Ethics section the authors address setting a Remediation period for responsible disclosure, during which stakeholders are informed and provided with materials to mitigate the discussed vulnerabilities. The source code and implementation details are not available publicly until then
pages: 5913--5930
Research Domain:
  - Privacy (Data Security & Analytics)
Research_Type:
  - System
  - Theory
Risk Benefit Analysis: true
Status: Data coded
Subdomain:
  - Privacy
  - Consent Compliance and Provable Privacy
title: "Atkscopes: Multiresolution Adversarial Perturbation as a Unified Attack on Perceptual Hashing and Beyond"
url: https://www.usenix.org/conference/usenixsecurity25/presentation/zhang-yushu
Usenix.DataPrivacy: false
Usenix.HarmMitigation: true
Usenix.HumanSubjects: false
Usenix.LiveTesting: false
Usenix.ResearcherSafety: true
Usenix.StakeholderImpact: true
Usenix.ToSViolation: false
Usenix.VulnDisclosure: true
---
