---
Alternatives Considered: false
author: Kotaiba Alachkar and Dirk Gaastra and Eduardo Barbaro and Michel van Eeten and Yury Zhauniarovich
author_tags:
  - Kotaiba Alachkar
  - Dirk Gaastra
  - Eduardo Barbaro
  - Michel van Eeten
  - Yury Zhauniarovich
base: "[[Databook.base]]"
DBLP Ref: DBLP:conf/uss/AlachkarGBEZ25
Direct Stakeholders:
  - System Operators
  - Software Maintainers
Emerging Themes:
  - Mitigation
Ethics Depth:
  - Detailed
Ethics Location:
  - Main Body
Ethics section: We conducted this research with a commitment to ethical standards. During the work on this project, we discovered a vulnerability that was reported to the respective vendor, adhering to responsible disclosure practices. On January 9, 2025, we received an acknowledgment from the vendor, along with a bounty award. However, since the issue remains unresolved, we have opted not to elaborate on the details. We are committed to ensuring that the vendor has adequate time to address the vulnerability before we provide further details on the discovered issue. Regarding EDR repurposing, it is important to clarify that this is not a vulnerability in the traditional sense; rather, it is a weakness in the way EDR systems can be used to perform malicious activities. The systems function as designed, but their capabilities can be misused in specific contexts. This highlights a security concern, especially for organizations that use multiple EDR solutions simultaneously. Raising awareness of this potential misuse is crucial, and we believe it is in the public interest to bring attention to this issue. Following the reviewers’ recommendations, on December 21, 2024, we reported our findings to the vendors of the EDR systems analyzed in this study. We included a preliminary version of our manuscript, offered to share our expertise, and invited them to provide their input on the matter. At the time of the preparation of the camera-ready version of this paper (January 27, 2025), we have received responses from two vendors acknowledging the issue. One vendor has assessed the issue as low severity, indicating that it does not require immediate servicing. The second vendor is currently investigating various mitigation strategies. Since the responsible disclosure period has not yet concluded, we have withheld the details about the vendors and our interactions with them. Adhering to high ethical standards, we have also placed our work under embargo, giving the vendors sufficient time to investigate the issue and implement appropriate mitigations. We are sure that all enterprises should be aware about this weakness and take countermeasures to mitigate the risk of its execution, using, for instance, the defense mechanisms proposed in this work. Moreover, to our opinion, the attention of the security community to this issue might drive the OS and EDR vendors to collaborate and add functionality mitigating this risk.
Framework Used:
  - Custom
Indirect Stakeholders:
  - End Users
  - Private Institutions
kanban_order: V0
key_quotes: ""
Menlo.Beneficience: true
Menlo.Justice: false
Menlo.RespectForLawAndPublicInterest: true
Menlo.RespectForPersons: false
notes: There is a dedicated section covering Defenses. The ethics section covers a risk benefit analysis and discusses vendor involvement thoroughly.
pages: 587--605
Research Domain:
  - System Security & Threat Detection
Research_Type:
  - System
  - Vuln Research
  - Theory
Risk Benefit Analysis: true
Status: Data coded
Subdomain:
  - System Security
  - Threat Detection Exploitation and Adaptive Defenses
title: "EvilEDR: Repurposing {EDR} as an Offensive Tool"
url: https://www.usenix.org/conference/usenixsecurity25/presentation/alachkar
Usenix.DataPrivacy: false
Usenix.HarmMitigation: true
Usenix.HumanSubjects: false
Usenix.LiveTesting: false
Usenix.ResearcherSafety: false
Usenix.StakeholderImpact: true
Usenix.ToSViolation: false
Usenix.VulnDisclosure: true
coded_date: 2026-11-02
---
