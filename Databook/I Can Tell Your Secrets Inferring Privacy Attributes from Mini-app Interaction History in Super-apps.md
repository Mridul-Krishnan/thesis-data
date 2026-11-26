---
Alternatives Considered: false
author: Yifeng Cai and Ziqi Zhang and Mengyu Yao and Junlin Liu and Xiaoke Zhao and Xinyi Fu and Ruoyu Li and Zhe Liu and Xiangqun Chen and Yao Guo and Ding Li
author_tags:
  - Yifeng Cai
  - Ziqi Zhang
  - Mengyu Yao
  - Junlin Liu
  - Xiaoke Zhao
  - Xinyi Fu
  - Ruoyu Li
  - Zhe Liu
  - Xiangqun Chen
  - Yao Guo
  - Ding Li
base: "[[Databook.base]]"
DBLP Ref: DBLP:conf/uss/CaiZYLZFL0C0025
Direct Stakeholders:
  - Data Subjects
  - Software Maintainers
  - Study Participants
Emerging Themes:
  - Stakeholder involvement at the Start of Study
Ethics Depth:
  - Detailed
Ethics Location:
  - Main Body
Ethics section: "We carefully reviewed the conference’s ethical guidelines, submission instructions, and ethics documents. Our research was conducted ethically and responsibly, with IRB approval from AliPay obtained before starting the study. We conducted our study transparently, assessing and mitigating risks for all stakeholders. For volunteer participants, we secured informed consent, anonymized their data, and ensured secure handling to prevent unauthorized access. A dedicated team of internal engineers, under strict confidentiality agreements, managed data extraction and anonymization, providing researchers only with anonymized, non-identifiable datasets. For AliPay as a company and its employees, there was a potential risk of reputational damage or exploitation of identified vulnerabilities by insiders. We proactively engaged with relevant departments to address these vulnerabilities and provided recommendations for improved security practices, aiming to minimize any negative impact on the company. Considering the broader super-app user base, we recognized that our findings might reveal vulnerabilities that could be exploited if not properly addressed. To mitigate this risk, we disclosed our findings to AliPay’s security team and other major super-app vendors. We received positive responses, and several vendors have committed to addressing these issues, thereby enhancing the security of all users. AliPay’s IRB Overview. AliPay, an international company with over a billion users, has an IRB that complies with ethical standards like the Common Rule and ISO 27701 for privacy management. This independent committee includes legal experts, ethicists, and external professionals unaffiliated with the company, ensuring unbiased and thorough reviews. The IRB evaluates all research involving human subjects to uphold the Participant Data Protection within AliPay. We protected participant data both externally and within AliPay by restricting access to a dedicated team of internal engineers bound by strict confidentiality agreements. This team handled data extraction and anonymization, with all activities logged and monitored. Engineers were prohibited from using the data for any purposes beyond this study. Researchers received only anonymized datasets with pseudonyms replacing unique identifiers, ensuring no access to personally identifiable in formation. Additionally, the engineers did not participate in research analysis, maintaining a clear separation of roles and further safeguarding participant privacy. User Consent and Data Collection. Since our evaluation involves the collection of privacy attributes, we obtained IRB approval from AliPay before collecting any data. The IRB requires us to obtain volunteers’ consent prior to data collection, and all procedures were conducted by internal engineers at AliPay under IRB supervision. For volunteer selection, internal engineers sent invitations to active users using automated systems that only checked login timestamps, ensuring no sensitive information was ac cessed. This procedure was approved by the IRB as low-risk and compliant with data protection policies. Once volunteers were selected, the engineers assisted us with the following steps: • Informed Consent: We informed the volunteers about the data we would collect, its intended use, and the measures taken to protect it. We assured them that the data would not be used for commercial purposes or shared with third parties. • Consent Acquisition: We obtained consent from users to access their mini-app interaction history and privacy attributes. For adult users, we obtained their consent directly. For minors, who typically use authorized accounts, we obtained consent from both the users and their parents. • Attributes Verification: During data verification, internal engineers matched participants’ provided attributes with internal databases(e.g., databases from the loan and insurance departments) in a secure and controlled environment. The matching process was automated to minimize human exposure to sensitive data. • Data Collection: We used AliPay-dev to notify volunteers of their participation, after which internal engineers extracted their mini-app interaction history from AliPay’s servers Note that the internal engineers anonymized all unique user identifiers before being provided to us. The data was securely stored in an encrypted database and was carefully deleted under IRB supervision after the evaluation. Data Access. All code and anonymized data were accessible only to the authors. The NDA approval process involved sub mitting a data access request to AliPay’s IRB, which reviewed the request for compliance with data protection policies. An agreement was then signed by the authors and authorized USENIX Association 34th USENIX Security Symposium 6555 personnel, and upon NDA approval, data access permissions [10] David G Balash, Xiaoyuan Wu, Miles Grant, Irwin were granted. Overall, all data access and handling complied with AliPay’s data protection policies and relevant laws, ensuring participant privacy and data security throughout the research."
Framework Used:
  - Custom
  - IRB
Indirect Stakeholders:
  - End Users
  - Adversaries
kanban_order: 4
key_quotes: ""
Menlo.Beneficience: true
Menlo.Justice: false
Menlo.RespectForLawAndPublicInterest: true
Menlo.RespectForPersons: true
notes: The research team worked alongside Alipay, the main super-app that is the subject of the research, from the very start of the research and engaged with them to achieve transparency, data privacy, and an informed, consensual methodology for study participants. They had approval from Alipay's own IRB which is a unique step as the typical IRB is originates from an academic institution. Discussion with Alipay covered potential risk, vulnerabilities discovered and mitigations, thereby covering risk-benefit analysis in those means.
pages: 6541--6560
Research Domain:
  - System Security & Threat Detection
Research_Type:
  - System
  - Vuln Research
Risk Benefit Analysis: true
Status: Ethics Section Extracted
Subdomain:
  - Privacy
  - Attacks
title: "I Can Tell Your Secrets: Inferring Privacy Attributes from Mini-app Interaction History in Super-apps"
url: https://www.usenix.org/conference/usenixsecurity25/presentation/cai-yifeng
Usenix.DataPrivacy: true
Usenix.HarmMitigation: true
Usenix.HumanSubjects: true
Usenix.LiveTesting: false
Usenix.ResearcherSafety: false
Usenix.StakeholderImpact: true
Usenix.ToSViolation: false
Usenix.VulnDisclosure: true
coded_date: 2026-09-28
---
