---
Alternatives Considered: false
author: Taisic Yun and Suhwan Jeong and Yonghwa Lee and Seungjoo Kim and Hyoungshick Kim and Insu Yun and Yongdae Kim
author_tags:
  - Taisic Yun
  - Suhwan Jeong
  - Yonghwa Lee
  - Seungjoo Kim
  - Hyoungshick Kim
  - Insu Yun
  - Yongdae Kim
base: "[[Databook.base]]"
DBLP Ref: DBLP:conf/uss/YunJLKKYK25
Direct Stakeholders:
  - System Operators
  - Data Subjects
Emerging Themes: []
Ethics Depth:
  - Detailed
Ethics Location:
  - Main Body
Ethics section: "We ensure ethical conduct throughout our study, adhering to established protocols for vulnerability disclosure and user research.\r

  Responsible Disclosure. To ensure the ethical handling of vulnerabilities discovered during our technical analysis, we adhere to a structured and detailed responsible disclosure pro cess. This process involved multiple stages of communication and verification between our team, a government agency, and the vendors, ensuring that vulnerabilities were responsibly addressed without exposing users to undue risks.\r

  1. Initial Reporting: This section assessed participants’ knowledge and understanding of KSA. It included questions about the definition and scope of KSA, along with examples to provide clarity. Participants were asked to identify service types and statements related to KSA to gauge their level of familiarity with the subject.\r

  2. Vendor Communication: The government agency for warded our report to the respective vendors. Based on the provided details, vendors reviewed the vulnerabilities and implemented patches to address them. After completing the initial patching, vendors reported their patching progress and implementation details back to the government agency.\r

  3. Cross-Verification: The government agency shared the patched software and information about the applied fixes with us. Our team then conducted cross-checks to verify the efficacy of the implemented patches. This included testing for remaining vulnerabilities, evaluating the correctness of the fixes, and ensuring adherence to the recommended patching methods.\r

  4. Follow-Up and Additional Guidance: During the cross verification process, we identified cases where additional patches were required or where initial patches were in correctly implemented. For instance, some fixes failed to address the root cause of the vulnerability or introduced secondary issues. In these instances, we provided detailed feedback and further recommendations to vendors, ensuring that all vulnerabilities were adequately addressed.\r

  5. Timeline and Progress: The entire process was coordinated with a patch timeline agreed to extend until May 2025. Vendors typically implemented initial patches and provided reports within two months of disclosure. This timeline ensured sufficient time for thorough patching and verification while maintaining the security of affected systems.\r

  By following this multi-stage process, we ensured that vulnerabilities were addressed comprehensively, minimizing potential risks to users and systems. This detailed approach not only prioritized ethical standards but also helped foster trust and accountability among all stakeholders involved.\r

  Online Survey. Our user study fully adhered to ethical standards, and we obtained Institutional Review Board (IRB) approval. Participants were informed about the survey’s purpose, content, and procedures and were made aware that they could withdraw from the study at any time without any con sequences. Participation was voluntary and limited to adults, and anonymity was strictly maintained by collecting only non identifiable information, such as gender and age. For surveys requiring program installation, we provided participants with clear instructions on installation, program functionality, and uninstallation. Responses were limited to screenshots of final outputs to minimize data collection risks. Data collected during the study was securely stored and accessible only to authorized researchers to ensure participant privacy and data integrity.\r

  Desktop Analysis Study. An additional user study was con ducted to collect information about KSA 2.0 programs actually installed by users, providing insights into their prevalence and usage patterns in real-world environments. This study adhered to the same ethical standards as the online survey, including IRB approval, participant anonymization, voluntary participation, and secure data handling protocols.\r

  Embargo and Research Integrity. To protect the confidentiality of identified vulnerabilities, the findings remain under embargo until vendors have fully addressed the reported is sues. The embargo period is set to extend until May 2025, ensuring sufficient time for patch implementation. The public release of the USENIX paper will occur after this embargo period, eliminating the risk of prematurely exposing vulnerabilities to potential attackers. This timeline aligns with established ethical research practices and prioritizes user safety.\r

  By adhering to these principles, we ensured ethical integrity in both the technical analysis and user research components of our study."
Framework Used:
  - Custom
Indirect Stakeholders:
  - Broader Public
  - Adversaries
  - End Users
key_quotes: ""
Menlo.Beneficience: true
Menlo.Justice: true
Menlo.RespectForLawAndPublicInterest: true
Menlo.RespectForPersons: true
notes: The ethics section is very thorough about the steps taken to ensure responsible disclosure, and also ensure participants are informed throughout the Online Survey and their data privacy is ensure. The impacted stakeholders are informed, and an embargo has been established for the vendors to address the reported issues.
pages: 8035--8054
Research Domain:
  - Cryptography & Formal Verification
Research_Type:
  - Vuln Research
  - Human Subjects
  - Theory
Risk Benefit Analysis: true
Status: Data coded
Subdomain:
  - System Security
  - Securing Systems and Protocols
title: "Too Much of a Good Thing: (In-)Security of Mandatory Security Software for Financial Services in South Korea"
url: https://www.usenix.org/conference/usenixsecurity25/presentation/yun
Usenix.DataPrivacy: true
Usenix.HarmMitigation: true
Usenix.HumanSubjects: true
Usenix.LiveTesting: true
Usenix.ResearcherSafety: false
Usenix.StakeholderImpact: true
Usenix.ToSViolation: false
Usenix.VulnDisclosure: true
coded_date: 2026-09-30
kanban_order: 7
---
