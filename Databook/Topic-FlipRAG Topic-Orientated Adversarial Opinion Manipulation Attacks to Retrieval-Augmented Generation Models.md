---
Alternatives Considered: false
author: Yuyang Gong and Zhuo Chen and Jiawei Liu and Miaokun Chen and Fengchang Yu and Wei Lu and XiaoFeng Wang and Xiaozhong Liu
author_tags:
  - Yuyang Gong
  - Zhuo Chen
  - Jiawei Liu
  - Miaokun Chen
  - Fengchang Yu
  - Wei Lu
  - XiaoFeng Wang
  - Xiaozhong Liu
base: "[[Databook.base]]"
DBLP Ref: DBLP:conf/uss/GongC0CY00L25
Direct Stakeholders: []
Emerging Themes: []
Ethics Depth:
Ethics Location: []
Ethics section: "Our research investigates vulnerabilities in RAG systems through the lens of adversarial opinion manipulation. We rigorously evaluated ethical implications using principles from The Menlo Report (Beneficence, Respect for Persons, Justice, and Respect for Law) and the USENIX Security Ethics Guidelines.\r

  Responsible Disclosure. We understand the importance of engaging with model and framework providers, so we re ported this vulnerability to the LangChain Security Team, hoping to collaborate on developing a mitigation module.\r

  However, due to limitations in defense measures, we have not yet gained recognition, and we are still striving to make effective progress. Additionally, the widespread use of hybrid open-source frameworks means that ownership boundaries are less clear compared to traditional software vulnerabilities.\r

  This ambiguity prompted us to explore a policy-oriented dis closure approach, aiming to encourage systemic preventative measures. Therefore, we used an accessible and efficient channel to initiate policy-level mitigation. We reported our preliminary findings and associated risks to our institution. This information, along with related content, was subsequently dis closed to Xinhua News Agency, not for public release. We want to emphasize that this initial disclosure was not intended to be exclusive or politically motivated. We are willing to in form other relevant platforms and international organizations.\r

  Data Privacy and User Consent. Our experiments involved opinion-based datasets covering various topics. To protect individual privacy, we ensured that all datasets are anonymized to remove personally identifiable information (PII), thus safeguarding individual privacy. Moreover, before beginning the user experiments, participants were thoroughly informed about the study’s background, purpose, and the measures in place to ensure fairness and privacy protection. After the experiment, we reiterated the true data distribution to participants to minimize any potential cognitive impact. Through out the research, we conducted all experiments, particularly those involving adversarial attacks, in secure environments to prevent unintended consequences.\r

  By addressing these ethical considerations, our research not only highlights vulnerabilities but also contributes to the development of robust solutions in safeguarding RAG models against exploitation.\r

  IRB Approval. This study was conducted under full Institutional Review Board (IRB) approval (Protocol No.\r

  WHU-HSS-IRB2025010. We confirm that all research activities strictly complied with the IRB-approved protocol. All research activities involving human participants received approval from our institution’s Humanities and Social Sciences Ethics Committee. To obtain IRB approval, we submitted a comprehensive application package, including a research ethics justification report, informed consent forms, a detailed project protocol, and the CVs of both the principal investiga tor and all research participants. The application was subject to a rigorous, multi-stage review process involving sequential approval by the project leader, institutional supervisors, the ethics committee secretary, and the committee leadership.\r

  After successfully completing all review stages, our study was formally granted IRB approval. Specific procedures are detailed as follows: Informed Consent: All participants were required to sign an informed consent form prior to the experiment. The document clearly communicated the study’s objectives, procedures, esti mated duration, potential psychological risks (e.g., exposure to controversial topics), compensation scheme (a cash reward of 50 RMB), and participants’ rights to withdraw at any time without penalty. Participants were also informed that their responses would be used solely for academic research.\r

  Data Handling and Anonymization: Allresponses and opin ion scores were collected using anonymized participant IDs.\r

  No personally identifiable information (such as name, contact details, or student ID) was stored. Data were encrypted and stored on secure servers accessible only to core research staff.\r

  Data will be retained for three years and then permanently deleted. Throughout the study, strict anonymization procedures were enforced. Participant identifiers were randomly assigned, and all data records excluded any direct or indirect personal information. This ensured that individuals could not be re-identified during analysis or in any published findings.\r

  User Privacy Protection: The entire study was conducted in a controlled laboratory environment to minimize external data exposure. All data were used exclusively for academic purposes and were never shared with third parties. Participants were provided with post-experiment debriefing, including full disclosure of the study’s objectives and safeguards. Additionally, experimental group participants were shown control group outputs after completion to reduce potential cognitive bias introduced by adversarial content exposure.\r

  In summary, this study not only adhered to rigorous ethical standards but also aimed to advance the development of trustworthy AI by systematically identifying vulnerabilities in RAG systems and promoting secure, transparent, and user-respecting model design."
Framework Used: []
Indirect Stakeholders: []
key_quotes: ""
Menlo.Beneficience: false
Menlo.Justice: false
Menlo.RespectForLawAndPublicInterest: false
Menlo.RespectForPersons: false
notes: ""
pages: 3807--3826
Research Domain:
  - Large Language Models (LLM)
Research_Type: []
Risk Benefit Analysis: false
Status: Ethics Section Extracted
Subdomain:
  - LLM Security
title: "Topic-FlipRAG: Topic-Orientated Adversarial Opinion Manipulation Attacks to Retrieval-Augmented Generation Models"
url: https://www.usenix.org/conference/usenixsecurity25/presentation/gong-yuyang
Usenix.DataPrivacy: false
Usenix.HarmMitigation: false
Usenix.HumanSubjects: false
Usenix.LiveTesting: false
Usenix.ResearcherSafety: false
Usenix.StakeholderImpact: false
Usenix.ToSViolation: false
Usenix.VulnDisclosure: false
coded_date: 2026-09-16
---
