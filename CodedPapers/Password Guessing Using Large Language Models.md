---
Alternatives Considered: false
author: Yunkai Zou and Maoxiang An and Ding Wang
author_tags:
  - Yunkai Zou
  - Maoxiang An
  - Ding Wang
base: "[[Databook.base]]"
DBLP Ref: DBLP:conf/uss/ZouA025
Direct Stakeholders:
  - Data Subjects
Emerging Themes:
  - Trolley Problem
Ethics Depth:
  - Detailed
Ethics Location:
  - Main Body
Ethics section: "Our study uses publicly available password datasets that were leaked through past breaches and have been widely used in prior password research (e.g., [25, 26, 30, 32, 42, 43]). However, besides passwords, our study incorporates associated personally identifiable information (PII), such as usernames and emails, in the context of targeted guessing scenarios. We acknowledge that this introduces a potentially higher risk to data subjects than studies using passwords alone. Also, we recognize that the individuals whose data were exposed in these breaches have not consented to the use of their data in research, nor have any meaningful opportunity to consent. Although these datasets are already publicly available, their continued use still raises important ethical considerations. To mitigate potential risks to affected individuals, we take four precautions to ensure that our research does not cause any additional harm to users: (1) We make sure no further dissemination of password data to other parties; (2) All our datasets are (ever) publicly available, and are stored and processed on computers not linked to the Internet; (3) We only report the aggregated statistical information and treat each individual account as confidential (so that using it in our research will not increase the risk to the corresponding victim, i.e., no personally identifiable information can be learned); (4) We delete the sensitive information (e.g., PII) once our analysis is completed. In particular, our analysis has been guided by the related Scenario B from [22], which explores the moral dilemma of studying stolen data that subjects have explicitly asked to be deleted. That scenario highlights the tension between deontological ethics (which emphasizes the rights of data subjects and the duty to respect privacy) and consequentialist ethics (which justifies data use if it leads to substantial public benefit). In line with the latter view, we believe the additional scientific insights gained from analyzing real-world password data can significantly enhance password security. Given the data’s prior public exposure and our strict safeguards, the additional knowledge gained from the research outweighs what is believed to be a small risk of additional harm to the data subjects. Specifically, our work aims to improve password security through the responsible use of real-world leaked password datasets. By analyzing password vulnerabilities in both trawling and targeted attack scenarios, we develop practical defenses such as a password strength meter based on LLMs. This tool evaluates the strength of passwords by estimating their guessability, and does not explicitly generate passwords, thereby reducing the risk of misuse."
Framework Used:
  - Custom
Indirect Stakeholders:
  - Adversaries
  - End Users
kanban_order: V1
key_quotes: ""
Menlo.Beneficience: true
Menlo.Justice: false
Menlo.RespectForLawAndPublicInterest: false
Menlo.RespectForPersons: true
notes: An attack-oriented LLM password-guessing study using non-consensually exposed credentials and linked PII. The detailed ethics discussion explicitly recognizes data privacy of the subject and secure handling of the data. The authors justify the work through consequentialist benefit–risk reasoning informed by a published ethical scenario (The paper highlighted in USENIX guidelines).
pages: 7799--7818
Research Domain:
  - System Security & Threat Detection
Research_Type:
  - Vuln Research
  - System
Risk Benefit Analysis: true
Status: Data coded
Subdomain:
  - Authentication
title: Password Guessing Using Large Language Models
url: https://www.usenix.org/conference/usenixsecurity25/presentation/zou-yunkai
Usenix.DataPrivacy: true
Usenix.HarmMitigation: true
Usenix.HumanSubjects: false
Usenix.LiveTesting: false
Usenix.ResearcherSafety: false
Usenix.StakeholderImpact: true
Usenix.ToSViolation: false
Usenix.VulnDisclosure: false
coded_date: 2026-11-04
---
