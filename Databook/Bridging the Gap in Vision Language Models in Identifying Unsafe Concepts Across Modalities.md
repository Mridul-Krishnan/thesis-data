---
Alternatives Considered: false
author: Yiting Qu and Michael Backes and Yang Zhang
author_tags:
  - Yiting Qu
  - Michael Backes
  - Yang Zhang
base: "[[Databook.base]]"
DBLP Ref: DBLP:conf/uss/Qu0025
Direct Stakeholders: []
Emerging Themes: []
Ethics Depth:
Ethics Location: []
Ethics section: "We have undergone an ethical review by our institution’s Ethics Review Board (ERB). Our ERB has approved the study and states that there are no ethical considerations if annotators are not exposed to images that are illegal to view or own, such as child sexual abuse materials, which do not exist in our dataset. Nonetheless, we recognize that ethical responsibility extends beyond the ERB approval. The main ethical concerns in this study involve the annotation process, demonstration of unsafe examples, future release of UnsafeConcepts images, and correct use of our proposed approach. First, To minimize potential harm from exposure to harmful content, all annotations are conducted by our research team. Although this prevents unsafe content from exposing to third parties, internal annotation might introduce bias, which originates from different opinions regarding what are considered unsafe or inappropriate in general safety contexts. To mitigate the annotation bias, we consider the following measures: (1) We did not define the unsafe taxonomy based on a single cultural lens. Instead, we referred to multiple sources, including the OpenAI content policy and relevant studies. This intersection ensures that ambiguous categories (e.g., Politics) are excluded, as they may be considered unsafe only in certain cultural contexts; (2) Before annotation, each unsafe concept was manually verified to ensure its unsafe nature in a general context. (3) During annotation, we identified whether the image accurately and completely depicts a specific unsafe concept (like an object detection task). This is different from simply labeling the image as safe or unsafe based on one’s subjective judgment. Second, to ensure the annotators’ well-being, we implement strict measures, including exposure limits, scheduled breaks, and regular mental health check-ins. Regarding the demonstration of unsafe images, since this is a study involving unsafe content, it is inevitable to display unsafe examples. However, we censor Not-Safe-For-Work (NSFW) images and avoid displaying unsafe images that might be offensive to different communities. Finally, while our proposed approach improves the safety alignment of VLMs in identifying unsafe concepts, it still relies on an annotated dataset in which humans define what is considered unsafe or inappropriate. This reliance introduces a risk: if misused by malicious actors, for example, by training the VLM on a poisoned dataset with flipped labels, this approach could distort the ethical standards built in the model. We call for the responsible and transparent use of such safety alignment methods."
Framework Used: []
Indirect Stakeholders: []
kanban_order: 13
key_quotes: ""
Menlo.Beneficience: false
Menlo.Justice: false
Menlo.RespectForLawAndPublicInterest: false
Menlo.RespectForPersons: false
notes: ""
pages: 957--976
Research Domain:
  - Machine Learning & AI (non-LLM)
Research_Type: []
Risk Benefit Analysis: false
Status: Ethics Section Extracted
Subdomain:
  - ML and AI Security
  - Images
title: Bridging the Gap in Vision Language Models in Identifying Unsafe Concepts Across Modalities
url: https://www.usenix.org/conference/usenixsecurity25/presentation/qu-yiting
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
