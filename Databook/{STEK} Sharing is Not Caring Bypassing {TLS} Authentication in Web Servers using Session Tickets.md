---
Alternatives Considered: false
author: Sven Hebrok and Tim Leonhard Storm and Felix Matthias Cramer and Maximilian Radoy and Juraj Somorovsky
author_tags:
  - Sven Hebrok
  - Tim Leonhard Storm
  - Felix Matthias Cramer
  - Maximilian Radoy
  - Juraj Somorovsky
base: "[[Databook.base]]"
DBLP Ref: DBLP:conf/uss/HebrokSCRS25
Direct Stakeholders: []
Emerging Themes: []
Ethics Depth:
Ethics Location: []
Ethics section: "Ethical Scan Guidelines. For our network-wide research scans, we strictly adhere to established ethical guidelines to ensure that our research is responsible and respectful of the broader internet community [16]. We maintain a block list of IP ranges that have requested to be excluded from our research activities. We set up reverse DNS entries and pro vide an information website on our scanning VM including contact details and information about opting out, allowing network operators to easily identify our scanning activities and understand their purpose. Our scans were registered with our ISP, any abuse reports were forwarded to and handled by us in a timely manner. To minimize the impact on networks, our scanning activities are designed to be of low intensity and are spread over time. This prevents network disruption or congestion. Additionally, only valid TLS traffic is generated.\r

  By adhering to these ethical guidelines, we aim to conduct our research in a manner that is both scientifically valuable and considerate of the rights and responsibilities of network operators.\r

  Responsible Disclosure. We have disclosed all identified vulnerabilities to the respective developers and/or organizations. CVEs were assigned for the findings in Apache (CVE 2025-23048) and nginx (CVE-2025-23419). LiteSpeed has fixed the issue, and Caddy has disabled session tickets when using client authentication. Fastly binds the tickets to the certificate, and Cloudflare, as a preliminary fix, disabled session tickets when using client authentication. We are in the dis closure process with the remaining identified vendors. We have communicated our intention to publish these findings, including the planned publication date, ensuring that all stake holders are informed and have sufficient time to implement fixes."
Framework Used: []
Indirect Stakeholders: []
key_quotes: ""
Menlo.Beneficience: false
Menlo.Justice: false
Menlo.RespectForLawAndPublicInterest: false
Menlo.RespectForPersons: false
notes: ""
pages: 8017--8034
Research Domain:
  - Cryptography & Formal Verification
Research_Type: []
Risk Benefit Analysis: false
Status: Ethics Section Extracted
Subdomain:
  - System Security
  - Securing Systems and Protocols
title: "{STEK} Sharing is Not Caring: Bypassing {TLS} Authentication in Web Servers using Session Tickets"
url: https://www.usenix.org/conference/usenixsecurity25/presentation/hebrok
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
