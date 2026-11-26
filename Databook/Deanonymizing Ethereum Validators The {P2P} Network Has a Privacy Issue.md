---
Alternatives Considered: false
author: Lioba Heimbach and Yann Vonlanthen and Juan Villacis and Lucianna Kiffer and Roger Wattenhofer
author_tags:
  - Lioba Heimbach
  - Yann Vonlanthen
  - Juan Villacis
  - Lucianna Kiffer
  - Roger Wattenhofer
base: "[[Databook.base]]"
DBLP Ref: DBLP:conf/uss/HeimbachVVKW25
Direct Stakeholders: []
Emerging Themes: []
Ethics Depth:
Ethics Location: []
Ethics section: "Our research aims to explore the lack of privacy for Ethereum validators. As this research involves critical infrastructure and the identification of organizational entities that may not wish to be identified, we followed rigorous ethical guidelines in accordance with the principles outlined in the Menlo Re port [5]. Below, we assess key stakeholders and detail how each principle was addressed throughout the course of this study.\r

  Respect for Persons. The principle of respect for persons requires that individuals’ autonomy and privacy are protected, and informed consent is obtained whenever necessary. Validators are logical entities identified through pseudonyms, which by design should make it so that they cannot be linked to humans. Nonetheless, we ensured that no identifiable information about any entities running Ethereum validators was exposed. We minimized the use of identifiable data, by us ing it purely to verify the validity of our results. Moreover, the analysis was done using publicly available data from the Ethereum P2P protocols.\r

  Beneficience. We systematically assess risks by identify ing key stakeholders, in order to maximize probable benefits while minimizing probable harm. First, staking entities that run Ethereum validators might suffer monetary harm, if an attacker were to exploit the vulnerability we expose. In order to minimize the likelihood of this scenario, we publish neither our code nor the deanonymized validator dataset (see Section 13). We further reached out to some larger entities, run standard Ethereum clients to collect data. In particular, we avoided rewriting client code to make deanonymization more efficient, as this might have caused additional load on current Ethereum nodes. Instead, our clients most likely had a net positive impact, by contributing in forwarding P2P messages for the duration of our experiment.\r

  The risk that malicious actors benefit from our disclosure is also counter-balanced by the mitigation strategies we put forward. Due to the improved understanding of privacy leaks, we can provide tools and mitigation strategies for Ethereum validators to minimize the efficacy of potential attacks.\r

  The Ethereum Foundation could itself be harmed, as their reputation as stewards of the ecosystem might be questioned.\r

  To mitigate such negative consequences, we have been in contact with the Ethereum Foundation from the very start of the project. Once our study was finished, we further disclosed our findings through the bug bounty program. We made sure to keep the entire project confidential until we got the written approval to publish our results.\r

  We believe that the Ethereum community can benefit from the insights we are able to gain from the results of our deanonymization. Many aspects, such as geographical decentralization, could not be studied before. This improved under standing can further strengthen the security of the Ethereum blockchain.\r

  Finally, while the lack of anonymity was noted before, re searchers and engineers can benefit from the improved perspective we offer and can work on building a more robust and private gossiping mechanism for the future.\r

  Justice. The benefits (and risks) of research should be fairly distributed. We did not single out specific individuals or organizations, and our work was conducted with the intent of benefiting the broader Ethereum community. To this end, we run RAINBOW nodes across multiple locations.\r

  Respect for Law and Public Interest. In line with the principle of respect for law and public interest, we conducted our research in compliance with legal and regulatory frameworks surrounding blockchain technology and data privacy. No actions were taken to exploit the vulnerabilities found; instead, our research was conducted with the aim of improving the Ethereum network’s security and privacy features."
Framework Used:
  - Menlo
Indirect Stakeholders: []
key_quotes: ""
Menlo.Beneficience: false
Menlo.Justice: false
Menlo.RespectForLawAndPublicInterest: false
Menlo.RespectForPersons: false
notes: ""
pages: 1319--1338
Research Domain:
  - Blockchain & Distributed Ledger Security
Research_Type: []
Risk Benefit Analysis: false
Status: Ethics Section Extracted
Subdomain:
  - Blockchain Security Attacks and Defenses
title: "Deanonymizing Ethereum Validators: The {P2P} Network Has a Privacy Issue"
url: https://www.usenix.org/conference/usenixsecurity25/presentation/heimbach
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
