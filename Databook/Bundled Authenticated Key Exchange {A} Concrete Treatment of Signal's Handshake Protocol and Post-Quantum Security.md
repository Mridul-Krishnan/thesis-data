---
Alternatives Considered: false
author: Keitaro Hashimoto and Shuichi Katsumata and Thom Wiggers
author_tags:
  - Keitaro Hashimoto
  - Shuichi Katsumata
  - Thom Wiggers
base: "[[Databook.base]]"
DBLP Ref: DBLP:conf/uss/HashimotoKW25
Direct Stakeholders: []
Emerging Themes: []
Ethics Depth:
Ethics Location: []
Ethics section: "In this work, we set out to analyze the security of implemented and deployed cryptographic protocols. The security of Signal’s handshake protocol is relied on by very large numbers of users, which makes better understanding the security of Signal’s handshake protocol and proposals for new security protocols with better security guarantees highly relevant. We based our analysis on publicly available documentation and open-source implementations of Signal’s protocols.\r

  Risks and Risk Mitigation. As part of analyzing the security of Signal’s X3DH and PQXDH protocols, it was a possibility that we might find new security flaws that could be used in real-world attacks on users of Signal. As prior work has thoroughly investigated the security of both of these protocols, we deemed this risk exceedingly unlikely. During the development of this work, we were in constant discussion with Signal’s developers; if any significant issues had been found, we would have coordinated with them on how to best protect Signal’s users, both of the Signal app itself, and other users of Signal including Facebook Messenger, WhatsApp, and others.\r

  Although we found that certain features of the deployed Signal handshake protocol made analysis more difficult, and Signal have indicated that they will be making changes in response to our findings, these changes only increase the robustness of the protocol and do not affect security or privacy of Signal’s users or other applications that use the X3DH or PQXDH protocols.\r

  If we would have had findings that affected the security of users, we would have followed standard responsible disclosure practices with suitable embargo periods before disclosure.\r

  Benefits. Signal is in the process of a transition towards full post-quantum security. We aim to contribute to this discussion by providing new models and results that can help developers using Signal’s handshake protocol evaluate how to proceed with this transition. We view that these benefits are well worth the (in our view, negligible) risks. The work was done while in open communication with Signal developers. They have received and reviewed our findings before submission."
Framework Used: []
Indirect Stakeholders: []
key_quotes: ""
Menlo.Beneficience: false
Menlo.Justice: false
Menlo.RespectForLawAndPublicInterest: false
Menlo.RespectForPersons: false
notes: ""
pages: 6777--6796
Research Domain:
  - Cryptography & Formal Verification
Research_Type: []
Risk Benefit Analysis: false
Status: Ethics Section Extracted
Subdomain:
  - Crypto
  - Systems and Protocols
title: "Bundled Authenticated Key Exchange: {A} Concrete Treatment of Signal's Handshake Protocol and Post-Quantum Security"
url: https://www.usenix.org/conference/usenixsecurity25/presentation/hashimoto-key-exchange
Usenix.DataPrivacy: false
Usenix.HarmMitigation: false
Usenix.HumanSubjects: false
Usenix.LiveTesting: false
Usenix.ResearcherSafety: false
Usenix.StakeholderImpact: false
Usenix.ToSViolation: false
Usenix.VulnDisclosure: false
coded_date: 2026-09-07
---
