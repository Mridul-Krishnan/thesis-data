---
Alternatives Considered: false
author: Bowen Hu and Kuo Wang and Chip{-}Hong Chang
author_tags:
  - Bowen Hu
  - Kuo Wang
  - Chip{-}Hong Chang
base: "[[Databook.base]]"
DBLP Ref: DBLP:conf/uss/HuWC25
Direct Stakeholders: []
Emerging Themes: []
Ethics Depth:
Ethics Location: []
Ethics section: "Disclosure: This NIR face authentication vulnerability was discovered by surprise and sidetracked from our original re search intent to explore polarization imaging for liveness detection against 3D face spoofing attacks. An immediate social impact arises for users relying on the default Windows Hello facial authentication: if their NIR or VIS images (or associated video samples) are compromised, the vulnerability detailed in this work can be exploited. Consequently, upon confirming the effectiveness of the attack on September 25, 2024, we immediately notified the security departments of Microsoft (MSRC), HP (HP PSRT), Dell (DELL PSIRT), and Lenovo (LENOVO PSIRT). We received their respective case numbers (MSRC 91421, HP-PSRT-IR 5182, DELL VRT-24281, LEN-174330) in prompt replies.\r

  We subsequently collaborated with Microsoft MSRC to further examine the “enhanced anti-spoofing” feature, which, when enabled, can resist our Red Bleed attack presented in this paper. This information was also shared with the other three companies of which their products were used for our investigation. All parties inquired about our disclosure time line, and upon being informed of our intention to submit this research to a leading security conference in January, we did not receive any objection about this submission.\r

  We provided complete technical details in a report to each vendor and addressed their questions. After verifying our findings, HP, Dell, and Lenovo deferred to Microsoft MSRC to coordinate and implement a comprehensive solution. In the communication with MSRC on January 18, 2025, they con firmed our described behavior. At Microsoft’s request, we shared our submitted conference paper. In their latest cor respondence on January 20, 2025, Microsoft indicated that they would fully address this vulnerability in the June 2025 update. In accordance with responsible disclosure practices, we have agreed to withhold public release of this research until Microsoft has fully mitigated the issue. Microsoft man aged to address this vulnerability earlier than expected with the CVE-2025-26644 published and the patch released in the KB5055523 security update for all in-service Windows versions on April 8, 2025.\r

  Data Collection and Privacy: In the data collection process for this study, 22 volunteers participated. These volunteers provided explicit, written consent authorizing the academic use of their facial biometric data. All participants involved in conducting the evaluation of these vulnerabilities were fully briefed on the study’s objectives and potential risks. For the privacy and ethical concerns, we deleted the registration of each individual volunteer immediately after the evaluation in his/her presence. The volunteers’ biometric data will not appear in the public domain except for one volunteer who has signed the agreement explicitly. Moreover, we have signed established ethical guidelines.\r

  Negative Outcomes: Although Microsoft remediated this vulnerability in the Windows update on April 8, 2025, many deployed devices, particularly air-gapped devices, experience delayed patching. Since this vulnerability requires no internet connection to exploit, we strongly recommend all potentially affected users immediately upgrade to the latest system version.\r

  There are also traditional biometrics relying on the NIR imaging, such as iris and palmprint [16,46,106]. In the absence of more robust anti-spoofing (liveness detection) measures, or only elementary spatial-temporal strategies are employed, these systems are similarly susceptible to the Red Bleed attack based on the same principal assumption of their security. The vulnerabilities exposed in this study may be inherently difficult to remediate in these existing biometric systems. Publication may render existing devices susceptible to exploits, with potential real-world consequences. We strongly urge affected vendors to issue public security advisories, implement proactive mitigation measures, and accelerate the phase-out of vulnerable devices.\r

  Positive Outcomes: This work clearly identified the root cause of an intrinsic vulnerability of NIR-based biometric authentication that allows for possible fortification to be developed. The disclosure of this long-lasting security myth can raise awareness and increase the vigilance on the use of legacy plain vanilla NIR-based biometric authentication before malicious actors discover this attack method, which may result in greater harms if the finding is kept private. We anticipate that this work will inspire the development of more secure anti-spoofing methodologies, thereby enhancing the security posture of future biometric systems."
Framework Used: []
Indirect Stakeholders: []
kanban_order: 38
key_quotes: ""
Menlo.Beneficience: false
Menlo.Justice: false
Menlo.RespectForLawAndPublicInterest: false
Menlo.RespectForPersons: false
notes: ""
pages: 7877--7896
Research Domain:
  - System Security & Threat Detection
Research_Type: []
Risk Benefit Analysis: false
Status: Ethics Section Extracted
Subdomain:
  - Authentication
title: "Red Bleed: {A} Pragmatic Near-Infrared Presentation Attack on Facial Biometric Authentication Systems"
url: https://www.usenix.org/conference/usenixsecurity25/presentation/hu-bowen
Usenix.DataPrivacy: false
Usenix.HarmMitigation: false
Usenix.HumanSubjects: false
Usenix.LiveTesting: false
Usenix.ResearcherSafety: false
Usenix.StakeholderImpact: false
Usenix.ToSViolation: false
Usenix.VulnDisclosure: false
coded_date: 2026-08-28
---
