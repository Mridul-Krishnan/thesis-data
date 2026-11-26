---
Alternatives Considered: false
author: Yumingzhi Pan and Zhen Ling and Yue Zhang and Hongze Wang and Guangchi Liu and Junzhou Luo and Xinwen Fu
author_tags:
  - Yumingzhi Pan
  - Zhen Ling
  - Yue Zhang
  - Hongze Wang
  - Guangchi Liu
  - Junzhou Luo
  - Xinwen Fu
base: "[[Databook.base]]"
DBLP Ref: DBLP:conf/uss/Pan00WLLF25
Direct Stakeholders: []
Emerging Themes: []
Ethics Depth:
  - Detailed
Ethics Location: []
Ethics section: "In this paper, we collected Tor exit traffic and used an LLM to identify IoT device traffic, aiming to gain insights into IoT attacks from the Tor exit perspective and designing efficient and effective intrusion detection strategies that can be deployed at Tor exit nodes for public safety, comparable to IDS on the Internet. Since Tor is an anonymity system and its users expect privacy, we placed significant thoughts and consideration into the design of our research study and our methods, not breaching personally identifiable information or content tied to users. Given the hypothesis that adversaries were using the Tor network to cause harm, we considered it imperative to study such adversarial uses toward an ultimate goal of preventing the victimization of others in the future, and help build trust in Tor protecting benign users. However, we also felt that it was essential to respect the privacy of the users of Tor. Thus, we designed our research methods with ethical considerations in mind.\r

  Our research adhered to the principles outlined in the Menlo Report [4] and we took the following steps to ensure that our experiments were conducted ethically: institutional review board (IRB) approval, responsible disclosure, data protection and use of anonymity provided by Tor. We also reflect on our practice and give suggestions for similar future research.\r

  Institutional Review Board (IRB) Approval: Our re search plan underwent and passed the ethical review process at our university. Based on the feedback from our university, “the proposed activity is not human subjects research as de fined by DHHS or FDAregulations. The research is limited to anonymous data being used for a systems analysis this would not require IRB purview.” Responsible Disclosure: We contacted manufacturers and responsibly disclosed the vulnerabilities identified in this pa per. For vulnerabilities CVE-2024-3272, CVE-2024-3273, and CVE-2024-3274, the vendor confirmed that the products are end-of-life and advised that they “ should be retired and replaced.” Regarding CVE-2024-4021 and CVE-2024-4022, the vendor acknowledged the issues and plans to implement fixes by the end of 2024.\r

  Data Protection: We took extensive measures to minimize any potential harm that might arise from our data collection efforts, including the following: (i) We minimized the data collection to the greatest extent possible. Aiming not to disrupt benign users’ use of Tor, we filtered out requests to the Top 1M Domains and those targeting VPS providers. (ii) We committed to keeping all user data and metadata confidential, ensuring none was exposed to third parties. (iii) The collected data was securely transmitted back via SSH encrypted channels and stored on a secure server located within a campus machine room, which has limited physical access. (iv) Our interaction with the data was limited to observation without any modification and did not disturb the operation of Tor. (v) We focused solely on identifying IoT device traffic and detecting IoT threats. (vi) All collected data was anonymized. (vii) The data was subsequently deleted upon submission of this paper.\r

  (viii) No personally identifiable information or content tied to users was ever inspected, and processing of the data was limited to automatic algorithms.\r

  Use of Anonymity Provided by Tor: The Tor mechanism anonymizes the source IP, which prevents us from obtaining user information based on the source IP, ensuring the privacy of users.\r

  Reflection: We acknowledge the ethical complexities inherent in this work, which can be viewed as a variation of the \"trolley problem.\" On one hand, attackers are abusing Tor to conduct cyberattacks, which harm public safety. Our method ology has the potential to mitigate these attacks through responsible disclosure and its adoption for intrusion detection.\r

  Conversely, analyzing data from a system intended to ensure privacy and anonymity may still raise ethical concerns, despite the safeguards we have implemented. While we believe that our decision to study Tor exit node traffic was the most ethical decision in this context, and we designed our methodology to help us understand the adversarial use of the Tor network while respecting the privacy of Tor users, we also explicitly caution that the existence of this work should not be used as justification for any future study of Tor exit traffic without special care to the underlying ethical considerations. While we were not aware of the Tor Research Safety Board at the time that we did our study, we recommend that future researchers consider consulting it when planning related studies."
Framework Used:
  - Custom
Indirect Stakeholders: []
key_quotes: ""
Menlo.Beneficience: false
Menlo.Justice: false
Menlo.RespectForLawAndPublicInterest: false
Menlo.RespectForPersons: false
notes: ""
pages: 1053--1072
Research Domain:
  - Hardware & Embedded Systems Security
Research_Type: []
Risk Benefit Analysis: false
Status: Ethics Section Extracted
Subdomain:
  - System Security
  - Trusted and Robust Computing
title: "{TORCHLIGHT:} Shedding {LIGHT} on Real-World Attacks on Cloudless IoT Devices Concealed within the Tor Network"
url: https://www.usenix.org/conference/usenixsecurity25/presentation/pan-yumingzhi
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
