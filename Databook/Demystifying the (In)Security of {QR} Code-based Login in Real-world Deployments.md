---
Alternatives Considered: false
author: Xin Zhang and Xiaohan Zhang and Bo Zhao and Yuhong Nan and Zhichen Liu and Jianzhou Chen and Huijun Zhou and Min Yang
author_tags:
  - Xin Zhang
  - Xiaohan Zhang
  - Bo Zhao
  - Yuhong Nan
  - Zhichen Liu
  - Jianzhou Chen
  - Huijun Zhou
  - Min Yang
base: "[[Databook.base]]"
DBLP Ref: DBLP:conf/uss/Zhang0ZNLCZ025
Direct Stakeholders:
  - Software Maintainers
Emerging Themes:
  - Call to Action/Report to Owner
Ethics Depth:
  - Detailed
Ethics Location:
  - Main Body
Ethics section: During this research, we strictly adhered to USENIX Security ’25 Ethics Guidelines [5], ensuring that no potential harm was caused to any stakeholders involved. This section discusses the ethical considerations we addressed throughout our study, from performing the user study, testing QRLogin websites for security analysis, to the responsible disclosure of identified vulnerabilities. User Study. Our study was approved by the Institutional Review Board (IRB). In our user study to investigate users’ perceptions of QRLogin security, we collected the participants’ anonymized background information to analyze and demonstrate the demographics of this user study. We ensured that participants were fully informed about the purpose of data collection, which is only for research, and we obtained consent for data collection. The data gathered, which was limited to non-sensitive demographics as outlined in Questions 10-13 in §B.3, ensures anonymity, making it impossible to contact or deduce specific individuals from the collected information. On the other hand, our questionnaire-based user study only asked about their habits, methods, and perceptions of using QRLogin. The survey did not request any confidential account information or credentials from participants. Testing Procedures. During our testing, we prioritized ethical standards to ensure that no harm was caused to the users and the websites. On the one hand, all tests were exclusively conducted using our own devices and test accounts, avoiding any potential risk to other users’ accounts. To avoid imposing unnecessary burdens on external systems, our tests were carefully designed and executed to simulate the typical behavior of regular users. The number of requests made during testing was strictly controlled within the normal user request range (i.e., fewer than 10 requests) to ensure that no excessive traffic or computational load was placed on any servers, thereby preventing any disruption to the normal operation of the websites. Moreover, as for the manual confirmation of the authorization hijacking attack, given it is a kind of race attack, launching a real attack would require the attacker to send requests to the server at a high frequency, which may cause stress on the server. Therefore, we adopted an approach of blocking the victim tester’s polling requests to confirm the race condition vulnerability. This approach avoids the impact on the website servers that would result from simulating the attack with high-frequency polling requests. Vulnerability Disclosure. All vulnerabilities identified in this study were promptly and responsibly reported to the relevant vendors following the specified ethical guidelines, along with proposed mitigation measures to minimize any potential risks. For vendors (websites) hosted in China, we reported the vulnerabilities through official platforms, including CNVD and CAPPVD,in compliance with the local regulation requirements (i.e., China). For vulnerabilities affecting other regions, we promptly contacted the affected vendors directly to report the security issues in their QRLogin implementations and provide practical measures to fix them, preventing potential exploitation. Note that while we initially attempted to report the vulnerabilities via the Common Vulnerabilities and Expo sures (CVE) platform, the idea seems not to work. According to CVE’s inclusion criteria, vulnerabilities on specific web sites are not assigned CVE IDs (as per INC3 in Inclusion Decisions [1]). As of our submission, we did not disclose any information of a specific vendor, if we have not received their response.
Framework Used:
  - USENIX Guidelines
Indirect Stakeholders:
  - End Users
kanban_order: 2
key_quotes: ""
Menlo.Beneficience: false
Menlo.Justice: true
Menlo.RespectForLawAndPublicInterest: true
Menlo.RespectForPersons: true
notes: There is a Suggestions for Developers section which covers additional details beyond their auditing tool which is acts as a call to action/guide for better practices for such widespread tooling. DevSecOps is not a widespread practice and engaging in coverage of such topics is helpful for Dev teams. There is also a Suggestion for Users section that has a similar effect. There is no form of risk-benefits analysis which would be useful since there was human subjects, live testing and vulnerabilities found.
pages: 3161--3180
Research Domain:
  - Software Security & Development Lifecycle
Research_Type:
  - Human Subjects
  - Vuln Research
Risk Benefit Analysis: false
Status: Data coded
Subdomain:
  - Web and Mobile Security
title: Demystifying the (In)Security of {QR} Code-based Login in Real-world Deployments
url: https://www.usenix.org/conference/usenixsecurity25/presentation/zhang-xin
Usenix.DataPrivacy: true
Usenix.HarmMitigation: true
Usenix.HumanSubjects: true
Usenix.LiveTesting: true
Usenix.ResearcherSafety: false
Usenix.StakeholderImpact: true
Usenix.ToSViolation: false
Usenix.VulnDisclosure: true
coded_date: 2026-09-28
---
