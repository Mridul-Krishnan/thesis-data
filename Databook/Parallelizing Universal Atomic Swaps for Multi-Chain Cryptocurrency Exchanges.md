---
Alternatives Considered: false
author: Danlei Xiao and Chuan Zhang and Haotian Deng and Jinwen Liang and Licheng Wang and Liehuang Zhu
author_tags:
  - Danlei Xiao
  - Chuan Zhang
  - Haotian Deng
  - Jinwen Liang
  - Licheng Wang
  - Liehuang Zhu
base: "[[Databook.base]]"
DBLP Ref: DBLP:conf/uss/Xiao0DLWZ25
Direct Stakeholders: []
Emerging Themes: []
Ethics Depth:
Ethics Location: []
Ethics section: "In developing and evaluating ParaSwap, we carefully considered the ethical implications for all stakeholders in the blockchain ecosystem, including blockchain users, developers, researchers, and the broader community. Our analysis follows ethical principles outlined in The Menlo Report and USENIX Security ’25 Ethics guidelines, ensuring that our work benefits users while minimizing potential risks.\r

  Beneficence (Benefits vs. Harms) • Benefits: ParaSwap parallelizes universal atomic swaps for cryptocurrency exchanges among multiple parties across multiple blockchains and minimizes the signifi cant time cost from O(n) caused by the serial process to O(1). The framework avoids the risk of asset theft and ensures atomicity by preventing partial execution of transactions with a uniform refund time used to avoid asset deadlock in parallel, offering significant benefits to legitimate users, especially in decentralized finance (DeFi) environments.\r

  • Potential Harms: In our work, malicious miners may manipulate transaction ordering over normal users to engage in illicit activities (i.e., MEV extraction). How ever, this is an inherent challenge in blockchain technology, and existing atomic swap schemes, such as [29, 30, 42, 44], including ours, have risks associated with MEVextraction. Similar to previous related works, our work focuses on atomic swaps between participants who exchange their assets, and the MEV extraction issues are out of the study scope. Moreover, there are substantial and well-developed MEV countermeasures, such as Flashbots [8], SUAVE [9], MEV-Boost [12], and Skip Protocol [14]. Further ethical discussion on MEV is given in Appendix C.\r

  Respect for Persons. We ensured that the research respects the autonomy of all individuals involved by: (i) All protocol details of ParaSwap are transparent and publicly documented.\r

  (ii) We have not collected or analyzed any private user data during the development and evaluation of ParaSwap. Users maintain full control over their assets and transaction privacy.\r

  Justice. ParaSwap design ensures fairness by: (i) ParaSwap is designed to be accessible to all blockchain users, regardless of their technical sophistication. (ii) The protocol distributes computational costs fairly between parties, ensuring that no single participant bears an undue burden.\r

  Respect for Law and Public Interest. In developing ParaSwap, we took into account legal considerations and public interest: (i) The protocol design fully complies with existing blockchain and cryptocurrency regulations, ensuring it adheres to legal frameworks and user protection laws.\r

  (ii) The implementation uses well-established cryptographic primitives and follows security best practices, ensuring the protocol’s robustness against attacks.\r

  Implementation and Testing Ethics. We conducted all experimental evaluations ethically by: (i) Our experimental evaluation was conducted using only test networks and simulated environments. We did not interact with or impact any live blockchain systems or real user assets. (ii) Ensuring that the results are reproducible and verifiable by making the full implementation and evaluation scripts publicly available. (iii) Gas cost measurements were conducted on controlled test networks to avoid impacting real-world networks.\r

  Disclosure and Documentation. We adhere to responsible disclosure by: (i) Our work specification and security proofs are fully documented. (ii) All code will be released as open source upon publication. (iii) Any discovered vulnerabilities will follow standard disclosure procedures.\r

  Terms of Service. Our experiments do not violate any terms of service.\r

  Wellbeing for Team Members. Our research activities do not have the potential to negatively impact team members.\r

  And we do not crawl morally questionable websites from a network.\r

  Deception. Participants are fully informed of the purposes and risks (among other things) of participating in experiments.\r

  Experiments with Live Systems Without Informed Con sent. Our work does not involve experiments with live systems.\r

  We believe that ParaSwap makes a positive contribution to blockchain technology by improving the efficiency of cross chain cryptocurrency exchanges while taking into account potential risks. We encourage further community engagement to explore challenges in efficiency, overhead, and security in the domain of cross-chain cryptocurrency exchanges with ethical considerations."
Framework Used: []
Indirect Stakeholders: []
key_quotes: ""
Menlo.Beneficience: false
Menlo.Justice: false
Menlo.RespectForLawAndPublicInterest: false
Menlo.RespectForPersons: false
notes: ""
pages: 4073--4092
Research Domain:
  - Blockchain & Distributed Ledger Security
Research_Type: []
Risk Benefit Analysis: false
Status: Ethics Section Extracted
Subdomain:
  - Blockchain Security Attacks and Defenses
  - Infrastructure Protocol Design and Governance
title: Parallelizing Universal Atomic Swaps for Multi-Chain Cryptocurrency Exchanges
url: https://www.usenix.org/conference/usenixsecurity25/presentation/xiao-danlei
Usenix.DataPrivacy: false
Usenix.HarmMitigation: false
Usenix.HumanSubjects: false
Usenix.LiveTesting: false
Usenix.ResearcherSafety: false
Usenix.StakeholderImpact: false
Usenix.ToSViolation: false
Usenix.VulnDisclosure: false
coded_date: 2026-09-08
---
