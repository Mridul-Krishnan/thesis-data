---
Alternatives Considered: false
author: '{\"{O}}nder Askin and Holger Dette and Martin Dunsche and Tim Kutta and Yun Lu and Yu Wei and Vassilis Zikas'
author_tags:
  - '{\"{O}}nder Askin'
  - Holger Dette
  - Martin Dunsche
  - Tim Kutta
  - Yun Lu
  - Yu Wei
  - Vassilis Zikas
base: "[[Databook.base]]"
coded_date: 2026-05-12T17:55:00
DBLP Ref: DBLP:conf/uss/AskinDDK00Z25
Direct Stakeholders:
  - System Operators
  - Data Subjects
Emerging Themes: []
Ethics Depth: Minimal
Ethics Location:
  - Main Body
Ethics section: We attest that the algorithms our privacy auditor/estimator identify as having privacy vulnerabilities are already recognized for (or specifically created with) these issues. Thus, this work does not expose new vulnerabilities. Additionally, we do not make use of private datasets in our experiments. Thus, our experiment results do not introduce privacy leaks. We attest that our auditor/estimator do not have any biases stemming from a conflict of interest. While our auditor can be used on other existing mechanisms, our implementation mitigates risks by ensuring our output is limited to alerts to potential privacy violation, and does not leak any additional information about the dataset(s) tested.
Framework Used:
  - None Explicit
Indirect Stakeholders:
  - Private Institutions
  - Vulnerable Populations
key_quotes: ""
Menlo.Beneficience: true
Menlo.Justice: true
Menlo.RespectForLawAndPublicInterest: false
Menlo.RespectForPersons: false
notes: The proposes a general purpose f-DP estimator and auditor for a black boy setting. There is no discovery of a new vulnerability, and the results of the auditor/estimator is a statistical measurement of the privacy maintained against a threshold so there is no data leaked either. They used only public datasets for experimentation. The ethics section doesn’t have more to address. Usability is slightly addressed in §8 regarding the plug-and-play design of the tool.
pages: 2713--2732
Research Domain:
  - Privacy (Data Security & Analytics)
Research_Type:
  - System
  - Measurement
Risk Benefit Analysis: false
Status: Data coded
Subdomain:
  - Privacy
  - Differential Privacy and Audit
title: General-Purpose f-DP Estimation and Auditing in a Black-Box Setting
url: https://www.usenix.org/conference/usenixsecurity25/presentation/askin
Usenix.DataPrivacy: true
Usenix.HarmMitigation: true
Usenix.HumanSubjects: false
Usenix.LiveTesting: false
Usenix.ResearcherSafety: false
Usenix.StakeholderImpact: true
Usenix.ToSViolation: false
Usenix.VulnDisclosure: false
---
