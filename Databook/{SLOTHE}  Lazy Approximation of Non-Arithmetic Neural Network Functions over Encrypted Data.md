---
Alternatives Considered: false
author: Kevin Nam and Youyeon Joo and Seungjin Ha and Yunheung Paek
author_tags:
  - Kevin Nam
  - Youyeon Joo
  - Seungjin Ha
  - Yunheung Paek
base: "[[Databook.base]]"
DBLP Ref: DBLP:conf/uss/NamJHP25
Direct Stakeholders: []
Emerging Themes: []
Ethics Depth:
Ethics Location: []
Ethics section: We honor and support the code of conduct for USENIX Security 2025. This section discusses several potential sources of ethics violations and reasons why our work does not correspond to them. We may not be able to address all existing ethic aspects, but have made our best effort to cover a broad range, as elaborated below. About Harms to Humans and Plagiarism. Our work does not involve any human participants for surveys or experiments. For the psychological well-being of our research team, we ensured that no harmful data, such as hate speech or socially biased content, was involved in our work. As far as we know, our work is original until the submission date. About Likelihood of Harm to Potential Stakeholders. The stakeholders of Privacy-Preserving NN inference services would be the user and the service provider, and SLOTHE do not cause harm to them. Rather, SLOTHE brings benefits to them. FHE-based NN inferences basically keep the privacy of the two parties from being disclosed to each other. The user’s input data is hidden with FHE and the service provider’s model parameters are hidden since computation is processed on the service provider’s server. SLOTHE is a work that enhances the performance and accuracy of the ser vice, thus rather is likely to increase the user’s satisfaction as well as the service provider’s income (if the number of users increase). In a systematic view, the only external input to the system running SLOTHE is the user’s requirements (See Fig.1). These requirements are submitted in a form visible to SLOTHE. If the user-provided values are not in the format 3096 34th USENIX Security Symposium USENIX Association they are supposed to be, SLOTHE can detect and terminate 10 Open Science the launch. From the user’s perspective, his private input data is encrypted on his local side, and in kept encrypted during the whole NN inference. The user is in fact the only one who can decrypt the result which also takes place locally. The secret key is always on the client local environment, never disclosed to other parties. On the server’s perspective, all computation happens in his own environment, thus his model parameters are not disclosed to other parties. System attacks on the two environment could extract the key, but such attacks are orthogonal to our work and can happen not only in our scenario but for all sorts of computer related ones. On minor notes, our work does not exploit vulnerabilities, nor does it promote specific commercial products. Based on these grounds, we claim that there are no concrete stakeholders or potential victims affected by our work. About Malicious Software. SLOTHE does not use any harmful software nor allow unautorized execution that can potentially damage the system of the developers. We highlight that at the bottom line, we use FHE, a well-known privacy preserving technique for protecting the private data of both parties in MLaaS, where all computations are simply under taken in the encrypted state. The process do not introduce any systematic vulnerabilities, just as previous FHE based NN inference works do [10–12,27,40]. Our work does not include any experiments about attacks on systems. SLOTHE is composed with only a set of methods with the goal of analyzing an NAF code and modify it into a FHE compatible state. It does not hold any potential ethics violations. Our evaluations do not include performing attacks or analyzing vulnerabilities, thus, no potential vulnerability or threat invoked on the deployed system by the results of our work. Unethical Experiments. As discussed above, our work does not impose any risks to the system and we conducted all experiments in a controlled, closed environment. All programs we use are extensions of open-sources, including the math libraries, FHE tools, NN frameworks, NN architectures and the corresponding pre-trained codes [47–49],and datasets [19,58]. Note that we used pre-trained models in their original form as provided online. To the best of our knowledge, this is the most objective way to demonstrate how FHE-based NN inference offer good accuracy (less loss) since training a model for our own leaves the possibility of biased training using a model trained to fit our specific needs. We also cross-check that the public models are as they are in their original literature (we strictly follow the instructions in their repositories for fine-tuning and running the transformers) and works that already have used them, to validate (to the best of our efforts) the authenticity and righteousness. Our work do not rely on additional or re-training adapted to FHE, thus we do not need to modify the NN itself except for the replacement of NAFs into approximations. This also only happens during inference, and it is indeed not in our favor in terms of performance and accuracy.
Framework Used: []
Indirect Stakeholders: []
kanban_order: 4
key_quotes: ""
Menlo.Beneficience: false
Menlo.Justice: false
Menlo.RespectForLawAndPublicInterest: false
Menlo.RespectForPersons: false
notes: ""
pages: 3083--3102
Research Domain:
  - Machine Learning & AI (non-LLM)
Research_Type: []
Risk Benefit Analysis: false
Status: Ethics Section Extracted
Subdomain:
  - ML and AI Privacy
  - Federated Learning and Protecting Data
title: "{SLOTHE} : Lazy Approximation of Non-Arithmetic Neural Network Functions over Encrypted Data"
url: https://www.usenix.org/conference/usenixsecurity25/presentation/nam-slothe
Usenix.DataPrivacy: false
Usenix.HarmMitigation: false
Usenix.HumanSubjects: false
Usenix.LiveTesting: false
Usenix.ResearcherSafety: false
Usenix.StakeholderImpact: false
Usenix.ToSViolation: false
Usenix.VulnDisclosure: false
coded_date: 2026-08-26
---
