---
Alternatives Considered: false
author: Yihan Ma and Xinyue Shen and Yiting Qu and Ning Yu and Michael Backes and Savvas Zannettou and Yang Zhang
author_tags:
  - Yihan Ma
  - Xinyue Shen
  - Yiting Qu
  - Ning Yu
  - Michael Backes
  - Savvas Zannettou
  - Yang Zhang
base: "[[Databook.base]]"
coded_date: 2026-04-24T17:18:00
DBLP Ref: DBLP:conf/uss/00010Q00Z025
Direct Stakeholders:
  - Research Team
Emerging Themes: []
Ethics Depth: Brief
Ethics Location:
  - Main Body
Ethics section: Our research evaluates whether VLMs can understand hateful memes and be misused to generate harmful content, such as hate speech, jokes, and slogans. The primary aim is to identify vulnerabilities in these systems and contribute to their improvement, rather than propagating or endorsing harmful content. To ensure ethical compliance, the dataset was carefully collected from publicly available sources, focusing on representative challenges. We follow established ethical guidelines throughout our analysis of these datasets and in the presentation of our results. We want to clarify that any hateful or discriminatory content included in our study is used solely for academic and educational purposes. All annotators are authors of this paper and receive comprehensive training on the task. We were informed about the nature of the content and provided with appropriate resources to mitigate the potential psychological impact. We used a structured annotation codebook to ensure consistency and reduce unnecessary exposure to harmful material. During the evaluation of VLMs’ ability to generate harmful content, strict controls were implemented to ensure ethical compliance. The generation process was carefully monitored, and any outputs were restricted to the experimental context. We guarantee that no content was stored, shared, or made accessible in a way that could lead to misuse or harm. This approach ensured that the study remained focused on identifying vulnerabilities without contributing to the propagation of harmful material. We strongly recommend that VLM providers implement robust safeguards to prevent the interpretation and generation of harmful content. These safeguards should include mechanisms to detect and block hateful content at both the input and output stages, as well as continuous monitoring and updates to address newly emerging hateful memes and content. By implementing such safeguards, providers can ensure safer deployment of VLMs while minimizing potential misuse.
Framework Used:
  - None Explicit
Indirect Stakeholders:
  - Broader Public
  - Vulnerable Populations
key_quotes: |-
  “All annotators are authors of this paper and receive comprehensive training on the task. We were informed about the
  nature of the content and provided with appropriate resources
  to mitigate the potential psychological impact.”
Menlo.Beneficience: true
Menlo.Justice: false
Menlo.RespectForLawAndPublicInterest: true
Menlo.RespectForPersons: false
notes: The study was conducted on locally hosted VLMs and the content created was not distributed. The dataset was procured from public sources. The goal of the in itself is provide a foundation to improve VLM safety and ethical standards in dealing with hateful content. The paper also includes a red font disclaimer in Abstract at the start of the paper as a warning for the offensive material present in the paper.
pages: 4703--4722
Research Domain:
  - Machine Learning & AI (non-LLM)
Research_Type:
  - Theory
  - Vuln Research
Risk Benefit Analysis: false
Status: Data coded
Subdomain:
  - ML and AI Security
title: "From Meme to Threat: On the Hateful Meme Understanding and Induced Hateful Content Generation in Open-Source Vision Language Models"
url: https://www.usenix.org/conference/usenixsecurity25/presentation/ma-yihan
Usenix.DataPrivacy: false
Usenix.HarmMitigation: false
Usenix.HumanSubjects: false
Usenix.LiveTesting: false
Usenix.ResearcherSafety: true
Usenix.StakeholderImpact: true
Usenix.ToSViolation: false
Usenix.VulnDisclosure: false
---
