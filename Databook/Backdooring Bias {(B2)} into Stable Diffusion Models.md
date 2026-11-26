---
Alternatives Considered: false
author: Ali Naseh and Jaechul Roh and Eugene Bagdasarian and Amir Houmansadr
author_tags:
  - Ali Naseh
  - Jaechul Roh
  - Eugene Bagdasarian
  - Amir Houmansadr
base: "[[Databook.base]]"
DBLP Ref: DBLP:conf/uss/NasehRBH25
Direct Stakeholders: []
Emerging Themes: []
Ethics Depth:
Ethics Location: []
Ethics section: Our research adheres to the principles outlined in The Menlo Report and aligns with the ethical guidelines established in the USENIX Security ’25 Ethics Guidelines. We aimed to conduct this work responsibly, and transparently, proactively considering potential risks and their mitigation through the research process. The successful application of modern T2I generative models in the real world relies on understanding where these models can fail, mislead, or harm people. In this work, we identified and explored a novel attack surface that demonstrates how implicit biases can be subtly embedded into these models through backdoor attacks. Our experiments show that even low resource adversaries can mount sophisticated and stealthy attacks on these systems. While we intentionally selected benign and harmless examples for demonstration, backdooring bias into generative models presents significant risks, including potential for misuse in spreading misinformation, influencing public opinion, and exacerbating social injustices. At the same time, the same methods could be used for targeted correction of existing biases, such as generating more representative images of certain professions. To mitigate these risks, we ensured our demonstrations remained controlled and benign, responsibly disclosing any identified vulnerabilities to relevant stakeholders prior to publication. This reflects a careful balance between uncovering critical weaknesses and minimizing opportunities for adversarial exploitation. Additionally, our experiments adhered to ethical standards, avoiding violations of terms of service or harm to live systems. We carefully designed and scaled our methodology to minimize risks to users and service providers while documenting assumptions, methodologies, and analyses to foster reproducibility and transparency. Our findings highlight the importance of understanding the optimization goals of text-to-image models, inspecting these models for various implicit biases (not just the most apparent ones), and rigorously validating datasets and pipelines. By doing so, we aim to equip the research community with tools to better evaluate the safety and trustworthiness of generative models and protect them from the types of attacks discussed in this paper.
Framework Used: []
Indirect Stakeholders: []
kanban_order: 11
key_quotes: ""
Menlo.Beneficience: false
Menlo.Justice: false
Menlo.RespectForLawAndPublicInterest: false
Menlo.RespectForPersons: false
notes: ""
pages: 977--996
Research Domain:
  - Machine Learning & AI (non-LLM)
Research_Type: []
Risk Benefit Analysis: false
Status: Ethics Section Extracted
Subdomain:
  - ML and AI Security
  - Images
title: Backdooring Bias {(B2)} into Stable Diffusion Models
url: https://www.usenix.org/conference/usenixsecurity25/presentation/naseh
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
