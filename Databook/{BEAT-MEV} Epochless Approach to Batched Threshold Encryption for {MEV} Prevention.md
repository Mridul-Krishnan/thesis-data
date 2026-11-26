---
Alternatives Considered: false
author: Jan Bormet and Sebastian Faust and Hussien Othman and Ziyan Qu
author_tags:
  - Jan Bormet
  - Sebastian Faust
  - Hussien Othman
  - Ziyan Qu
base: "[[Databook.base]]"
DBLP Ref: DBLP:conf/uss/BormetFOQ25
Direct Stakeholders:
  - Software Maintainers
Emerging Themes:
  - Mitigation
Ethics Depth:
  - Detailed
Ethics Location:
  - Main Body
Ethics section: "While our research does not involve human subjects or access public data, we recognize the potential impacts of our work on blockchain users, developers, and the broader public. We have engaged in a thorough ethical analysis consistent with the guidelines provided by USENIX Security and the principles delineated in The Menlo Report [3].\r

  Our research contributes positively to blockchain industry by mitigating the MEV problem, enhancing user privacy, and reducing financial risks. This helps to support security and fairness in blockchain, benefiting all the users. We are aware that some individuals or entities have been exploiting MEV for financial gain, and our work may disrupt their activities.\r

  However, since MEV is commonly regarded as malicious and profiting from it is unethical, and that some MEV such as front-running caused direct harm to users, we believe that our work is justified and ethical.\r

  With detailed security proof and discussion on potential attacks and mitigations, we ensure that our work is robust and secure, and that our work will not introduce new vulnerabilities to the blockchain systems. While transactions in the mem pool are encrypted, we strengthen the privacy of users. Given the fact that transactions written to the blockchain will eventually be public, we preserve the transparency of blockchain, and do not introduce new potential financial crimes. Our re search methodology does not use any personal data or proprietary information, and our implementation is completely open-source. All the drawbacks and potential risks of related works introduced in our work have been discussed or dis closed in literature, thus we do not introduce new risks to the community."
Framework Used:
  - Custom
  - USENIX Guidelines
  - Menlo
Indirect Stakeholders:
  - End Users
  - Adversaries
key_quotes: ""
Menlo.Beneficience: true
Menlo.Justice: true
Menlo.RespectForLawAndPublicInterest: false
Menlo.RespectForPersons: false
notes: The paper covers improvement of tool proposed in a previous USENIX paper, BTE, by an epochless approach. The ethics section covers a risk benefit analysis, identifies the impact on adversaries and refers to the dedicated Attacks and Mitigation section earlier in the paper. While a defensive tool doesn't need alternatives considered, the paper does refer to alternative methods to address MEV prevention in related works.
pages: 3457--3476
Research Domain:
  - Cryptography & Formal Verification
Research_Type:
  - System
  - Theory
Risk Benefit Analysis: true
Status: Data coded
Subdomain:
  - Crypto
  - Private Information Retrieval and Computation
title: "{BEAT-MEV:} Epochless Approach to Batched Threshold Encryption for {MEV} Prevention"
url: https://www.usenix.org/conference/usenixsecurity25/presentation/bormet
Usenix.DataPrivacy: true
Usenix.HarmMitigation: true
Usenix.HumanSubjects: false
Usenix.LiveTesting: false
Usenix.ResearcherSafety: false
Usenix.StakeholderImpact: false
Usenix.ToSViolation: false
Usenix.VulnDisclosure: false
coded_date: 2026-11-01
kanban_order: 8
---
