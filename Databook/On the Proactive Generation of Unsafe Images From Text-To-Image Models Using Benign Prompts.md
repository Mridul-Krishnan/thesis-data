---
Alternatives Considered: false
author: Yixin Wu and Ning Yu and Michael Backes and Yun Shen and Yang Zhang
author_tags:
  - Yixin Wu
  - Ning Yu
  - Michael Backes
  - Yun Shen
  - Yang Zhang
base: "[[Databook.base]]"
coded_date: 2026-03-05T15:25:00
DBLP Ref: DBLP:conf/uss/000100S025
Direct Stakeholders:
  - System Operators
Emerging Themes:
  - Adversarial Vuln to NN
Ethics Depth: Brief
Ethics Location:
  - Main Body
Ethics section: "We explain the following ethics-related decisions during our developing process: The goal of the paper is to poison the textto-image model, causing it to generate images that are similar to certain hateful memes. Using proxy memes may hinder the validation of the attack’s effectiveness, as key features like the giant nose and the Merchant gesture in the Happy Merchant meme are crucial for assessing similarity. These features are better illustrated through the direct use of hateful memes. Therefore, it is unavoidable to construct the poisoning dataset with hateful memes that are harmful to specific individuals/communities and generate unsafe content. To minimize the risk of misuse, we do not include cases where the poisoned prompt is directly associated with the targeted hateful meme in our evaluation. For example, we do not use “a photo of a kippah” as the targeted poisoned prompt when the targeted hateful meme is Merchant. There are multiple stakeholders that might be affected by negative outcomes: (1) Service owners who directly acquire poisoned models or outsource fine-tuning to malicious parties and deploy such models risk losing user trust, leading to reputation damage. (2) End users belonging to specific individuals or communities may feel the content is inappropriate or disturbing due to the hateful and discriminatory meaning of targeted memes. Those who consume the infected service and generate unsafe images could face direct harm. (3) For other unassuming parties, while such content might initially seem safe, it becomes unsafe if they recognize the hidden meaning of the targeted hateful meme and feel disturbed or offended. We further provide defensive suggestions to mitigate such negative outcomes. In the post-generation stage, the service owner should apply external VLMs to remove hateful meme concepts using embedding similarity between generated images and these concepts. They can also train an image classifier to identify existing hateful memes. Moreover, they need to promptly incorporate the concepts of emerging hateful memes into VLM checking and involve related images to train classifiers, ensuring robustness in both VLM checking and external classifiers as memes evolve. Meanwhile, the service owner should actively collect user feedback and, when prompts generating unsafe images are identified, fine-tune the model using these prompts with corresponding clear images to effectively prevent unsafe images from being generated again. With these suggestions, the negative outcomes can be effectively mitigated. The evaluation dataset is anonymous and publicly available. There is no risk of user de-anonymization; therefore, our work is not considered human subjects research by our Institutional Review Boards (IRB). Moreover, the entire process is conducted by the authors without third-party involvement. All authors do not feel uncomfortable about the generated content. We only provide the datasets for research purposes upon request. Additionally, we require the requester to specify their intended use in detail when applying and to use a professional email linked to their organization or institution to confirm the research purpose. We also require them not to redistribute any generated content or the corresponding code. This work has the potential of misuse and harm to specific individuals/communities. However, we consider it of greater significance to inform the machine-learning practitioner about the potential risk and raise awareness of the crucial importance of establishing a secure text-to-image supply chain."
Framework Used:
  - None Explicit
Indirect Stakeholders:
  - Broader Public
  - Vulnerable Populations
  - End Users
key_quotes: In this paper, we present the first comprehensive investigation into the proactive generation of unsafe images. Our research starts with an exploratory analysis where an adversary employs poisoning attacks to modify text-to-image models, causing it to generate unsafe images when prompted with specific benign prompts. We focus particularly on hateful memes (Figure 1), a special type of unsafe images used to disseminate ideological propaganda targeting specific individuals/communities [31, 38, 50, 54, 56]. Despite the detrimental effects that hateful memes exert on society, efforts to mitigate these risks have received minimal attention, making them harder to detect by external and internal checkers of text-toimage models than universally unsafe images [39], such as sexually explicit content. The targeted prompt employed in our attack can be arbitrary, e.g., “a photo of a cat.” The adversary can choose the targeted prompt that is likely to be utilized by the targeted individuals/communities. From both qualitative and quantitative perspectives, we observe that the SDMs are vulnerable to the basic poisoning attack, as the adversary attains the attack goal with 20 poisoning samples in all cases and as few as five poisoning samples in some cases
Menlo.Beneficience: true
Menlo.Justice: false
Menlo.RespectForLawAndPublicInterest: true
Menlo.RespectForPersons: true
notes: The ethics section does a stakeholder analysis, however it doesn’t consider the researchers as a stakeholders. They do address that all authors didn’t feel uncomfortable with regards to the generated content, perhaps more considerations should be made with respect to how the hateful memes sampled in this paper was chosen. They have addressed the procedure for procuring their dataset in a safe and responsible manner. Within Section 8 Discussion and Limitations - they have discussed that to reduce the risk of misuse, they have chosen not use explicit description of the hateful meme for the targeted prompt. The workflow of designing the attack also uses BLIP to extract the description of the hateful meme.
pages: 917--936
Research Domain:
  - Machine Learning & AI (non-LLM)
Research_Type:
  - Vuln Research
  - System
Risk Benefit Analysis: true
Status: Data coded
Subdomain:
  - ML and AI Security
  - Images
title: On the Proactive Generation of Unsafe Images From Text-To-Image Models Using Benign Prompts
url: https://www.usenix.org/conference/usenixsecurity25/presentation/wu-yixin-generation
Usenix.DataPrivacy: true
Usenix.HarmMitigation: true
Usenix.HumanSubjects: false
Usenix.LiveTesting: false
Usenix.ResearcherSafety: false
Usenix.StakeholderImpact: true
Usenix.ToSViolation: false
Usenix.VulnDisclosure: true
---
