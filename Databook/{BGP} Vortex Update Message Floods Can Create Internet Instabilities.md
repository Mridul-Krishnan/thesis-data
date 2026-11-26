---
Alternatives Considered: false
author: Felix St{\"{o}}ger and Henry Birge{-}Lee and Giacomo Giuliari and Jordi Subir{\`{a}} Nieto and Adrian Perrig
author_tags:
  - Felix St{\"{o}}ger
  - Henry Birge{-}Lee
  - Giacomo Giuliari
  - Jordi Subir{\`{a}} Nieto
  - Adrian Perrig
base: "[[Databook.base]]"
DBLP Ref: DBLP:conf/uss/StogerBGNP25
Direct Stakeholders: []
Emerging Themes: []
Ethics Depth:
Ethics Location: []
Ethics section: "The research conducted in this paper has followed strict ethical guidelines both in our experiments and disclosure. We follow responsible disclosure practices and are coordinating with a National Cyber Security Centre (NCSC) to inform affected stakeholders and aid in the deployment of appropriate mitigation strategies for BGP Vortex. The NCSC is proficient in globally orchestrating ethical disclosures in the area of computer networking. A manuscript describing the BGP Vortex attack and mitigations will be shared globally by the NCSC with partner institutions, which further disseminate the information within their jurisdiction. Furthermore, we are actively engaging with networking communities such as RIPE and NANOG to ensure that operators at leading ISPs are made aware of the attack and how to mitigate it. The majority of our experiments were conducted either through simulation or in isolated laboratory environments, ensuring no impact on external systems or the Internet. The only exception involves the BGP community probes detailed in Section 4.2: Ethically Probing Vulnerability of Tier-1ASes, which required interaction with the live routing infrastructure. To maintain the stability and integrity of the global routing system, we tested BGP communities individually—rather than concurrently—to verify that indeed they could be used in 3626 34th USENIX Security Symposium USENIX Association the wild. We tested the NOPEER communities individually, confirming their behavior one-by-one. The local preference lowering communities were tested in combination, which was necessary to demonstrate that the final routing configuration is dependent on BGP update ordering. Still, the combination of the three local preference lowering communities is not sufficient to trigger persistent instability. This controlled order-dependent equilibrium, if combined with the separately verified NOPEER communities, proves that a BGP Vortex could exist in the wild. In summary, our careful experimental procedures ensured that while we could validate our theoretical findings, we did not risk disrupting the broader Internet infrastructure. Our ethical disclosure through the NCSC ensures that the most affected stakeholders receive timely support in implementing appropriate defenses."
Framework Used: []
Indirect Stakeholders: []
kanban_order: 0
key_quotes: ""
Menlo.Beneficience: false
Menlo.Justice: false
Menlo.RespectForLawAndPublicInterest: false
Menlo.RespectForPersons: false
notes: ""
pages: 3613--3629
Research Domain:
  - Network Security & Infrastructure
Research_Type: []
Risk Benefit Analysis: false
Status:
  - Ethics Section Extracted
Subdomain:
  - Network Security
  - Routing and DoS
title: "{BGP} Vortex: Update Message Floods Can Create Internet Instabilities"
url: https://www.usenix.org/conference/usenixsecurity25/presentation/stoeger
Usenix.DataPrivacy: false
Usenix.HarmMitigation: false
Usenix.HumanSubjects: false
Usenix.LiveTesting: false
Usenix.ResearcherSafety: false
Usenix.StakeholderImpact: false
Usenix.ToSViolation: false
Usenix.VulnDisclosure: false
---
