---
Alternatives Considered: false
author: Jason Kim and Jalen Chuang and Daniel Genkin and Yuval Yarom
author_tags:
  - Jason Kim
  - Jalen Chuang
  - Daniel Genkin
  - Yuval Yarom
base: "[[Databook.base]]"
DBLP Ref: DBLP:conf/uss/0007CGY25
Direct Stakeholders: []
Emerging Themes: []
Ethics Depth:
Ethics Location: []
Ethics section: "We describe our adherence to ethics guidelines while evaluating our attacks in Sections 5 and 6 and responsible disclosure.\r

  Ethical Testing of Attacks. We own all devices used in our experiments, and these devices are free of any sensitive user data or personal information. These devices are only accessible to lab members, and are not exposed to unauthorized users.\r

  For online accounts, all of the accounts involved in our attacks are dummy accounts that we own, and are ensured not to con tain any sensitive information. To reduce the risk to unrelated parties, we host the code for the attack on Safari (Section 5) on a local web server that is not publicly accessible.\r

  To overcome Site Isolation [47], the code of the attack on Chrome (Section 6) has to be hosted in the same eTLD+1 do main as the target domain (cf. Section 6.3), which in our case is a dummy Square storefront that does not sell anything. To protect unrelated users that inadvertently visit our storefront, we modify the attack code to check for a specific cookie value and disable the attack if the value is not found. Consequently, running the attack requires opening Chrome’s developer tools and manually adding a cookie, and thus we ensure it will not run on innocuous machines. Finally, we took down this storefront immediately after finishing our evaluation.\r

  Product Security Team on September 3, 2024 upon completing the initial version of the writeup. Apple has acknowledged our writeup, and after an internal investigation, communicated that they plan to address this in an upcoming security update without sharing further details."
Framework Used: []
Indirect Stakeholders: []
key_quotes: ""
Menlo.Beneficience: false
Menlo.Justice: false
Menlo.RespectForLawAndPublicInterest: false
Menlo.RespectForPersons: false
notes: ""
pages: 2595--2614
Research Domain:
  - Hardware & Embedded Systems Security
Research_Type: []
Risk Benefit Analysis: false
Status: Ethics Section Extracted
Subdomain:
  - Hardware Security
  - Microarchitectures
title: "{FLOP:} Breaking the Apple {M3} {CPU} via False Load Output Predictions"
url: https://www.usenix.org/conference/usenixsecurity25/presentation/kim-jason
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
