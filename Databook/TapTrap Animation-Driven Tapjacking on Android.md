---
Alternatives Considered: false
author: Philipp Beer and Marco Squarcina and Sebastian Roth and Martina Lindorfer
author_tags:
  - Philipp Beer
  - Marco Squarcina
  - Sebastian Roth
  - Martina Lindorfer
base: "[[Databook.base]]"
DBLP Ref: DBLP:conf/uss/BeerSRL25
Direct Stakeholders: []
Emerging Themes: []
Ethics Depth:
Ethics Location: []
Ethics section: "User Study\r

  \r

  Our institution’s ethics committee reviewed the user study conducted in this work. We outline the core concerns of the study and the measures we took to mitigate them.\r

  \r

  Recruitment Partiality. Participants were, among other channels, recruited from courses offered at our institution.\r

  To mitigate the potential concern that users might feel ob ligated to participate, we emphasized that participation was entirely voluntary and provided no academic advantage. Additionally, recruitment was conducted by two authors of this paper who were not affiliated with any of the courses where recruitment took place, to ensure impartiality and minimize any perceived pressure to participate.\r

  \r

  Participant’s Feelings of Deception. Participants who do not identify the attack during the study might feel deceived or con fused. To mitigate this, we included a final debriefing session where participants played the game a third time. During this session, we explicitly demonstrated the attack mechanism and explained where and how the attacks occurred. This ensured that participants left the study with a clear understanding of the attack and its implications.\r

  \r

  Responsible Disclosure In October 2024, we reported the TapTrap attack to the Android Security Team. The report was intially acknowledged but later marked as a duplicate of an existing issue, to which we were not granted access to. The security team stated that the vulnerability would be addressed in a future release, but provided us with no timeline or further information in this re gard. As of June 2025, the vulnerability remains unpatched.3 We also disclosed the vulnerability to the affected browser vendors, including Google Chrome, Mozilla Firefox, Microsoft Edge, and Brave. Both Edge and Brave acknowl edged the issue but deferred responsibility to Chrome, as their browsers are based on the Chromium engine. Chrome fixed the issue in version 135, assigned CVE-2025-3067, and awarded us a bug bounty of $10K, while Mozilla addressed it in Firefox 136 with CVE-2025-1939. Both browser vendors followed our recommendations and mitigated the attack by relying on the onEnterAnimationComplete method.\r

  In November 2024, we separately reported the off-by-one error in the animation duration restriction to the Android Security Team. This report was marked as “WontFix’, explaining that it “does not affect the security of the Android platform”.\r

  While the issue may not be critical in isolation, it effectively doubles the attack window for TapTrap, thereby increasing the likelihood of a successful attack."
Framework Used: []
Indirect Stakeholders: []
key_quotes: ""
Menlo.Beneficience: false
Menlo.Justice: false
Menlo.RespectForLawAndPublicInterest: false
Menlo.RespectForPersons: false
notes: ""
pages: 3317--3335
Research Domain:
  - Software Security & Development Lifecycle
Research_Type: []
Risk Benefit Analysis: false
Status: Ethics Section Extracted
Subdomain:
  - Web and Mobile Security
title: "TapTrap: Animation-Driven Tapjacking on Android"
url: https://www.usenix.org/conference/usenixsecurity25/presentation/beer
Usenix.DataPrivacy: false
Usenix.HarmMitigation: false
Usenix.HumanSubjects: false
Usenix.LiveTesting: false
Usenix.ResearcherSafety: false
Usenix.StakeholderImpact: false
Usenix.ToSViolation: false
Usenix.VulnDisclosure: false
coded_date: 2026-09-11
---
