---
Alternatives Considered: false
author: Jiachen Zhou and Mingsi Wang and Tianlin Li and Guozhu Meng and Kai Chen
author_tags:
  - Jiachen Zhou
  - Mingsi Wang
  - Tianlin Li
  - Guozhu Meng
  - Kai Chen
base: "[[Databook.base]]"
coded_date: 2026-03-10T15:42:00
DBLP Ref: DBLP:conf/uss/0001WLM025
Direct Stakeholders:
  - Study Participants
  - System Operators
Emerging Themes: []
Ethics Depth:
  - Detailed
Ethics Location:
  - Main Body
Ethics section: "DORMANT is a defense approach designed to prevent image misuse in pose-driven human image animation methods, thereby safeguarding individuals’ rights to portrait and privacy. To ensure fair and reproducible evaluations of the performance of DORMANT, we conducted experiments on commonly used public datasets, following the setups outlined in prior animation methods [13, 70, 74, 86]. All experimental data, including the fake videos generated during the experiments, were stored on private, secure servers and are strictly intended for academic research purposes only; they will not be shared beyond their intended scope. During the research process, three experiments posed potential risks of unauthorized exposure of generated fake videos: the human study, the GPT-4o study, and experiments on commercial services. These experiments used the TikTok test set [33, 70], which permits research purposes. Although this publicly available dataset is widely used in many studies, obtaining explicit consent from the individuals depicted in the photos remains challenging. An alternative approach could have involved collecting and using data from volunteers who could explicitly consent. However, the terms of service for video generation platforms typically allow the use of user inputs and outputs for training and improving their AI models. While publicly available data may have already been integrated into these platforms’ model training, uploading newly collected images from consenting individuals would introduce their data for the first time, potentially exposing them to additional privacy risks due to uncontrolled usage. To mitigate these risks and ensure fairness and reproducibility in our evaluation, we chose to use publicly available data. Meanwhile, we remained vigilant about the potential exposure of generated fake videos and implemented precautionary measures to minimize risks. All participants in the human study were required to consent to not disseminate any content from the questionnaire, which was accessible for a limited time. Before uploading data to GPT-4o and video generation websites, we configured our account privacy settings to the strictest levels, including disabling “Chat History & Training” in GPT-4o, setting repositories to private, and upgrading to memberships with enhanced privacy features, etc. During the experiments, we documented the setups for reproducibility, downloaded and stored the generated results on private servers, and cleared all data from the accounts upon completion. All activities were conducted in full compliance with the usage rules and regulations of the respective platforms. We conducted a human study to evaluate the performance of DORMANT from the perspective of human perception. The study was reviewed and received IRB approval at our institute. Before providing consent, participants were fully informed of the study’s purpose, procedures, potential risks and benefits, and lottery-based compensation. They were also warned that the questionnaire might include unfiltered videos that could be disturbing, and were shown sample videos upon request if they expressed concern. Participants were allowed to withdraw from the study at any point, with any data they provided excluded from the analysis. Additionally, participants were required to consent to not disseminate any content from the questionnaire. Explicit consent was obtained through a digital agreement before participants gained access to the questionnaire, which was available for a limited duration. All participants remained anonymous. Demographic data, including gender, age, education, expertise, and familiarity, were collected solely for research purposes through single-choice questions with generalized options, including a “prefer not to say” option. No personally identifiable information was collected, and all data were securely and privately stored."
Framework Used:
  - IRB
Indirect Stakeholders:
  - Broader Public
  - End Users
key_quotes: ""
Menlo.Beneficience: true
Menlo.Justice: true
Menlo.RespectForLawAndPublicInterest: false
Menlo.RespectForPersons: true
notes: The paper includes a Human Study to evaluate the perception of Humans against the  proposed tool DORMANT vs other similar tools, the study was reviewed and approved by their institute’s board. The team address data privacy concerns for the humans involved in the study. Additionally there was a LLM study (GPT.4o), they have ensured privacy in their repos for this case and the most secure privacy settings and membership. They have tested on commercial services but have limited themselves to the publicly available TikTok dataset (which is what they used in the studies as well) for testing the tool’s performance. They address harm mitigation via the usage of the publicly available dataset as well. Coming across the usability testing for a previous paper, perhaps they should do a study regarding that as well.
pages: 5209--5228
Research Domain:
  - Usable Security & Privacy
Research_Type:
  - Human Subjects
  - System
  - Theory
Risk Benefit Analysis: true
Status: Data coded
Subdomain:
  - Social Issues and Usable Security and Privacy
title: "Dormant: Defending against Pose-driven Human Image Animation"
url: https://www.usenix.org/conference/usenixsecurity25/presentation/zhou
Usenix.DataPrivacy: true
Usenix.HarmMitigation: true
Usenix.HumanSubjects: true
Usenix.LiveTesting: false
Usenix.ResearcherSafety: false
Usenix.StakeholderImpact: false
Usenix.ToSViolation: false
Usenix.VulnDisclosure: false
---
