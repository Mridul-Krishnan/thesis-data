---
Alternatives Considered: false
author: Florian Draschbacher and Lukas Maar and Mathias Oberhuber and Stefan Mangard
author_tags:
  - Florian Draschbacher
  - Lukas Maar
  - Mathias Oberhuber
  - Stefan Mangard
base: "[[Databook.base]]"
DBLP Ref: DBLP:conf/uss/DraschbacherMOM25
Direct Stakeholders: []
Emerging Themes: []
Ethics Depth:
Ethics Location: []
Ethics section: We responsibly disclosed all identified vulnerabilities to affected vendors. In addition to the 16 Android issues mentioned in Section 1, we also disclosed our findings regarding susceptibility of iOS devices to CHOICEJACKING attacks to Apple. We filed our reports between June and July of 2024, and have since been assisting vendors in reproducing the issues on their side and integrating suitable mitigations. Samsung assigned us moderate severity CVE-2024-20900 for the attack principle and rolled out first improvements to their USB mode selection implementation. Apple added user authentication prompts for USB connections in iOS 17.5, but is yet to integrate this mitigation into iOS 18. Xiaomi, Huawei, Vivo and Honor confirmed our findings and are still working on corresponding patches to their Android variants. Google assigned us high severity CVE-2024-43085 for the underlying flaws that caused MTP to be exposed on locked Oppo and Honor devices. A corresponding fix has been rolled out in the November 2024 Android Security Bulletin (ASB). They are also working on fixes for the reported design flaws in upstream AOSP. All evaluations were carried out in a lab environment, on dedicated research devices. We anticipate that the publication of our work will positively impact USB security of mobile platforms and help raise user awareness for USB-based threats.
Framework Used: []
Indirect Stakeholders: []
kanban_order: 15
key_quotes: ""
Menlo.Beneficience: false
Menlo.Justice: false
Menlo.RespectForLawAndPublicInterest: false
Menlo.RespectForPersons: false
notes: ""
pages: 4363--4379
Research Domain:
  - System Security & Threat Detection
Research_Type: []
Risk Benefit Analysis: false
Status: Ethics Section Extracted
Subdomain:
  - System Security
  - Mobile Platforms
title: "ChoiceJacking: Compromising Mobile Devices through Malicious Chargers like a Decade ago"
url: https://www.usenix.org/conference/usenixsecurity25/presentation/draschbacher
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
