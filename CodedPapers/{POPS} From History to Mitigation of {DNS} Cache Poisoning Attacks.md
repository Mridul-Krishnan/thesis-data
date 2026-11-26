---
Alternatives Considered: false
author: Yehuda Afek and Harel Berger and Anat Bremler{-}Barr
author_tags:
  - Yehuda Afek
  - Harel Berger
  - Anat Bremler{-}Barr
base: "[[Databook.base]]"
coded_date: 2026-05-12T17:10:00
DBLP Ref: DBLP:conf/uss/AfekBB25
Direct Stakeholders:
  - System Operators
Emerging Themes: []
Ethics Depth: Minimal
Ethics Location:
  - Main Body
Ethics section: We evaluated POPS for FP on real data obtained from a published dataset on the Internet [83]. We carefully considered the ethical implications of our analysis and ensured that user privacy was protected. To prevent any harm from using user data in DNS queries, we only retained the responses received by the resolver from DNS authoritative servers, discarding the rest of the data. As a result, no IP addresses or personally identifiable information (PII) from users were used at any stage of the research. All the experiments of POPS were conducted in a controlled laboratory environment, with a dedicated server.
Framework Used:
  - None Explicit
Indirect Stakeholders:
  - End Users
  - Broader Public
key_quotes: ""
Menlo.Beneficience: true
Menlo.Justice: true
Menlo.RespectForLawAndPublicInterest: false
Menlo.RespectForPersons: false
notes: The paper proposes a system, POPS, for mitigation of various DNS cache poisoning attacks. The system being a defensive doesn’t call for a detailed ethical analysis. Existing vulnerabilities are discussed but nothing new is disclosed. The stakeholders are implicitly referred (DNS server operators and the attacker). The ethical section addresses data privacy of the users from the obtained publicly available dataset is addressed.  A usability analysis would be useful.
pages: 3537--3556
Research Domain:
  - Network Security & Infrastructure
Research_Type:
  - System
  - Vuln Research
Risk Benefit Analysis: false
Status: Data coded
Subdomain:
  - Network Security
  - Routing and DoS
title: "{POPS:} From History to Mitigation of {DNS} Cache Poisoning Attacks"
url: https://www.usenix.org/conference/usenixsecurity25/presentation/afek
Usenix.DataPrivacy: true
Usenix.HarmMitigation: true
Usenix.HumanSubjects: false
Usenix.LiveTesting: false
Usenix.ResearcherSafety: false
Usenix.StakeholderImpact: false
Usenix.ToSViolation: false
Usenix.VulnDisclosure: false
---
