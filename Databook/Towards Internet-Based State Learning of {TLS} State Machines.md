---
Alternatives Considered: false
author: Marcel Maehren and Nurullah Erinola and Robert Merget and J{\"{o}}rg Schwenk and Juraj Somorovsky
author_tags:
  - Marcel Maehren
  - Nurullah Erinola
  - Robert Merget
  - J{\"{o}}rg Schwenk
  - Juraj Somorovsky
base: "[[Databook.base]]"
DBLP Ref: DBLP:conf/uss/MaehrenEMSS25
Direct Stakeholders: []
Emerging Themes: []
Ethics Depth:
Ethics Location: []
Ethics section: Since obtaining a state machine representation requires many connections to a server, we configured our implementation to pause for at least 1.5 seconds after each connection. We further only scan each host with a single thread and do not utilize messages specifically aimed to cause buffer overflows, trigger known crashes of TLS libraries or to test for attacks that may result in the leakage of private keys or user data (e.g. we did not include alphabet symbols triggering buffer boundary violations, for example, for the Heartbleed attack [16]). We limited our study to hosts participating in bug-bounty programs as these are expected to be more resilient against non-conforming packets. When we detect that a peer does not respond to our queries for a prolonged time while our Internet connection appears healthy, we stop scanning the host to respect possible blacklisting. We provided a web page on our scanning IP that informed about the purpose of our scans and provided a contact address to request an opt-out. The test vectors we employed to detect padding oracle and Bleichenbacher vulnerabilities are not suited to extract keys of other TLS sessions or to obtain any user data. Regarding the publication of anonymized state machines (see below), we believe that the potential insights gained from further studies outweigh any potential risks. If the state machines hint towards vulnerabilities not considered in the scope of this paper, a malicious actor would first have to derive queries suitable to identify a host on the Internet. Responsible Disclosure We responsibly disclosed the identified padding oracle and transcript integrity vulnerabilities to the respective domain owners/software vendors and provided support to test for reported issues.
Framework Used: []
Indirect Stakeholders: []
kanban_order: 29
key_quotes: ""
Menlo.Beneficience: false
Menlo.Justice: false
Menlo.RespectForLawAndPublicInterest: false
Menlo.RespectForPersons: false
notes: ""
pages: 7097--7116
Research Domain:
  - Network Security & Infrastructure
Research_Type: []
Risk Benefit Analysis: false
Status: Ethics Section Extracted
Subdomain:
  - Network Security
  - Internet and Beyond
title: Towards Internet-Based State Learning of {TLS} State Machines
url: https://www.usenix.org/conference/usenixsecurity25/presentation/maehren
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
