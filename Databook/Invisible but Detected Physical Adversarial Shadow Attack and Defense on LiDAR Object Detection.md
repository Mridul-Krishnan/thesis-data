---
Alternatives Considered: false
author: Ryunosuke Kobayashi and Kazuki Nomoto and Yuna Tanaka and Go Tsuruoka and Tatsuya Mori
author_tags:
  - Ryunosuke Kobayashi
  - Kazuki Nomoto
  - Yuna Tanaka
  - Go Tsuruoka
  - Tatsuya Mori
base: "[[Databook.base]]"
DBLP Ref: DBLP:conf/uss/KobayashiNTTM25
Direct Stakeholders: []
Emerging Themes: []
Ethics Depth:
Ethics Location: []
Ethics section: In this study, we proposed an attack method that exploits the physical mechanisms inherent in LiDAR systems and examined its impacts and potential defense strategies. To ensure ethical research conduct, we have taken the following measures. Collaboration with Affected Stakeholders. We recognized that our research outcomes could affect automobile manufacturers, autonomous driving system developers, and creators of LiDAR datasets. We engaged in collaboration with these stakeholders by initiating a process of responsible disclosure. We have provided them with comprehensive information regarding the potential vulnerabilities identified and corresponding countermeasures. We plan to compile all the details and make them available on our website upon acceptance of this paper. Assessment of Risks in Data and Model Usage. This research utilized public datasets (KITTI) and open-source object detection models (PointPillars, PointRCNN, SECOND-IoU). Based on the nature of these data, attacks against object detection systems trained on these datasets can be executed. To address this, we are in the process of summarizing precautions for using public point cloud data and sharing this information with data providers and open-source model developers. We are also working to encourage them to alert users about potential risks. Positive and Negative Impacts of Proposing Attack Methods. The attack method proposed in this study aims to promote the development of defense strategies and enhance the safety of autonomous driving technology, aligning with the public interest as outlined in the Menlo Report [12]. Recognizing the potential misuse of this method, potentially negatively affecting the safety of autonomous vehicles, we carefully considered the benefits and risks. In accordance with the Menlo Report’s emphasis on minimizing potential harms, we determined that the potential positive impacts justify the publication of our findings. To further mitigate risks, we collaborated with stakeholders before the publication of this research and recommended the implementation of defense measures. Safety Considerations for Experiments and Team Members. We used LiDAR devices certified as Class 1 eye-safe in our experiments to eliminate risks to eyesight. Additionally, all experiments were conducted in a safely managed environment within private property, ensuring the safety of team members and the surrounding area. Compliance with Research Ethics Policies. Based on the USENIX Security ’25 Ethics Guidelines and the principles outlined in the Menlo Report, we evaluated potential negative impacts during the research process and at the time of publishing the results, conducting the research with ethical judgment. While the likelihood of this research causing direct harm at this stage is low, we are considering future risks and are engaged in continuous monitoring and responsible disclosure. We believe that the dissemination of this research will ultimately contribute to the public good by improving the security and reliability of autonomous systems.
Framework Used: []
Indirect Stakeholders: []
kanban_order: 24
key_quotes: ""
Menlo.Beneficience: false
Menlo.Justice: false
Menlo.RespectForLawAndPublicInterest: false
Menlo.RespectForPersons: false
notes: ""
pages: 7369--7386
Research Domain:
  - Machine Learning & AI (non-LLM)
Research_Type: []
Risk Benefit Analysis: false
Status: Ethics Section Extracted
Subdomain:
  - ML and AI Security
  - Robustness
title: "Invisible but Detected: Physical Adversarial Shadow Attack and Defense on LiDAR Object Detection"
url: https://www.usenix.org/conference/usenixsecurity25/presentation/kobayashi
Usenix.DataPrivacy: false
Usenix.HarmMitigation: false
Usenix.HumanSubjects: false
Usenix.LiveTesting: false
Usenix.ResearcherSafety: false
Usenix.StakeholderImpact: false
Usenix.ToSViolation: false
Usenix.VulnDisclosure: false
coded_date: 2026-08-27
---
