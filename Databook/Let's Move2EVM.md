---
Alternatives Considered: false
author: Lorenzo Benetollo and Andreas Lackner and Matteo Maffei and Markus Scherer
author_tags:
  - Lorenzo Benetollo
  - Andreas Lackner
  - Matteo Maffei
  - Markus Scherer
base: "[[Databook.base]]"
coded_date: 2026-05-22
DBLP Ref: DBLP:conf/uss/BenetolloLMS25
Direct Stakeholders:
  - Software Maintainers
  - System Operators
Emerging Themes: []
Ethics Depth: Brief
Ethics Location:
  - Main Body
Ethics section: The research conducted for this paper did not involve human subjects. Consequently, no human subjects were deceived in particular or harmed in general. Our evaluation data is based on publicly available data and was retrieved using publicly available interfaces. When scraping public data, we made sure not to overload the scraped system by employing reasonable intervals between the single queries. The presented approach is purely defensive in nature and thus does not present a negative potential by itself. We, however, discuss that not using our approach (i.e., using the existing compiler) might expose users to vulnerabilities (without presenting concrete vulnerabilities found “in the wild” or trying to find out how prevalent these vulnerabilities are). From a technical perspective, we deem the question of prevalence, which by itself would be a considerable task, out of scope. From an ethical standpoint, scanning the blockchain for vulnerable contracts would not mitigate this paper’s potential negative impact, as Ethereum’s anonymity prevents disclosure of any findings to relevant stakeholders. Additionally, we want to stress that the vulnerable compiler is still marked as “experimental” and its application in security-critical domains is likely limited. To the best of our knowledge, among the major adopters of the Move language, only the publicly available repository of Aptos [8] contains the vulnerable compiler referenced in this paper. In light of the archival of the original repository, we consider Aptos to be the primary stakeholder for the responsible disclosure of this issue. The Aptos team was notified of the findings and subsequently informed us that they are not aware of any production deployments using the compiler. Consequently, to the best of our knowledge, no additional stakeholders require notification. Shortly after our disclosure, Aptos removed the compiler from their repository [27]. The authors of this paper did, in all conscience, not break the laws of any relevant jurisdiction while conducting the research presented here.
Framework Used:
  - Custom
Indirect Stakeholders:
  - End Users
kanban_order: 0
key_quotes: ""
Menlo.Beneficience: false
Menlo.Justice: true
Menlo.RespectForLawAndPublicInterest: true
Menlo.RespectForPersons: false
notes: "The papers processes an  an Inlined-Reference-Monitor-(IRM)-based\r

  protection layer as an extension to the Move-2-EVN compiler. It would act as an additional layer of harm mitigation and monitoring and is a purely defensive extension. The Ethics section addresses stakeholder impact and data privacy. Also addressing the vulnerable compiler used in the paper. As with tools in general, a usability analysis would be conducive."
pages: 1339--1355
Research Domain:
  - Blockchain & Distributed Ledger Security
Research_Type:
  - System
Risk Benefit Analysis: true
Status: Data coded
Subdomain:
  - Blockchain Security Attacks and Defenses
title: Let's Move2EVM
url: https://www.usenix.org/conference/usenixsecurity25/presentation/benetollo
Usenix.DataPrivacy: true
Usenix.HarmMitigation: true
Usenix.HumanSubjects: false
Usenix.LiveTesting: false
Usenix.ResearcherSafety: false
Usenix.StakeholderImpact: true
Usenix.ToSViolation: false
Usenix.VulnDisclosure: true
---
