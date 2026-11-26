---
Alternatives Considered: false
author: George Pavlides and Anna Clee and Ioana Boureanu and Tom Chothia
author_tags:
  - George Pavlides
  - Anna Clee
  - Ioana Boureanu
  - Tom Chothia
base: "[[Databook.base]]"
DBLP Ref: DBLP:conf/uss/PavlidesCBC25
Direct Stakeholders:
  - System Operators
  - Software Maintainers
Emerging Themes:
  - Call to Action/Report to Owner
  - Stakeholder Identification
Ethics Depth:
  - Detailed
Ethics Location:
  - Main Body
Ethics section: "Attacks, Reproducibility and Ethics. In terms of EMV readers, we used:– several Square Terminals, under UK firmware. We used them for contactless EMV payments, both offline and online. Offline, in the UK, the Square Terminal is supposed to accept contactlessly only GooglePay and ApplePay38.– one online SumUp Air39 configured for Romania, one on line SumUp Air configured for the UK, one online SumUp Solo configured for the UK and one online Square Reader configured for the UK. As such, they deal with PIN-checking for contactless cards differently. All plastic cards, mobile devices and readers/PoS we used are not comprised and registered to us (i.e., we do not victimise retailers or the general public). We use no personal data, or sensitive data, other than ours. We present 10 attacks and 2 “problems”. Some of them stem from similar problems (e.g., poor checking of a Visa field called “SDAD”), some are unrelated to this (e.g., on GooglePay’s transport mode), some are on plastic cards, some on mobile, they have different victims, levels of complexity, etc. To appreciate these aspects earlier on, we refer the reader to Figure 5, to an overview table of all our attacks. Statement by Parties Involved in the Responsible Disclosure. The only EMV party involved who gave us a statement to include is Square. This is as follows: “At Square, protecting the security of our seller community is our highest priority. We recognize the important contributions that the security research community can make when it comes to finding potential bugs and we have offered a bug bounty program to the security research community since 2014. We have collaborated with this research team since their discovery and responsible disclosure of their initial findings via our bug bounty program outlined in the following paper. This collaboration involved replicating the issue using the conditions detailed by the team (see Section 4) and working closely with the research team in the testing phase of the security update we designed for this condition. We can confirm that a security update for the researchers’ initial disclosure has since been deployed to all susceptible Square devices. And while we remain actively engaged with our network partners on the security of the payments ecosystem, we do not believe the additional findings represent an increased risk to sellers and buyers transacting with offline payments at this time. We would like to thank these researchers for their vigilance in identifying and responsibly disclosing their findings, as well as their collaboration in testing the security update we developed for their initial disclosure”."
Framework Used:
  - Custom
Indirect Stakeholders:
  - Broader Public
  - End Users
kanban_order: 0
key_quotes: '"The use of ad-hoc, proprietary extensions means that EMV loses the security it gained through carefully designing the protocols in the core specification."'
Menlo.Beneficience: true
Menlo.Justice: true
Menlo.RespectForLawAndPublicInterest: true
Menlo.RespectForPersons: false
notes: The paper evaluates EMV specifications and extensions across various bodies and regions .They uncover vulnerabilities and attack vectors that arise due to these variations that don't align or have gaps between them. Fig 5 summarizes the stakeholder identification (various victims and owners) with a focus on the attack vectors. There is thorough process followed for responsible disclosure with a stakeholder's response included in the ethics section. Data privacy is maintained as the researchers only use their personal data. The paper also discusses fixes and has tracked the state of fixes/mitigation in the "Who can fix / Fixed or not" column in Fig 5. Overall the papers is in itself comprehensive of the research and broadly covers its effects including the ethical ones.
pages: 7977--7996
Research Domain:
  - Cryptography & Formal Verification
Research_Type:
  - Vuln Research
Risk Benefit Analysis: true
Status: Data coded
Subdomain:
  - System Security
  - Securing Systems and Protocols
title: "More is Less: Extra Features in Contactless Payments Break Security"
url: https://www.usenix.org/conference/usenixsecurity25/presentation/pavlides
Usenix.DataPrivacy: true
Usenix.HarmMitigation: true
Usenix.HumanSubjects: false
Usenix.LiveTesting: false
Usenix.ResearcherSafety: false
Usenix.StakeholderImpact: true
Usenix.ToSViolation: false
Usenix.VulnDisclosure: true
coded_date: 2026-06-02
---
