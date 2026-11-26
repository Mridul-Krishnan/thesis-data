---
Alternatives Considered: false
author: Wenlong Meng and Shuguo Fan and Chengkun Wei and Min Chen and Yuwei Li and Yuanchao Zhang and Zhikun Zhang and Wenzhi Chen
author_tags:
  - Wenlong Meng
  - Shuguo Fan
  - Chengkun Wei
  - Min Chen
  - Yuwei Li
  - Yuanchao Zhang
  - Zhikun Zhang
  - Wenzhi Chen
base: "[[Databook.base]]"
DBLP Ref: DBLP:conf/uss/MengFW0LZ0C25
Direct Stakeholders:
  - Study Participants
  - System Operators
  - Software Maintainers
Emerging Themes: []
Ethics Depth:
  - Detailed
Ethics Location:
  - Main Body
Ethics section: "Our research aims to expose the vulnerabilities in current AIGT detectors, assisting developers in creating more robust systems. We weighed the potential benefits and risks of this research and concluded our strategies can effectively mitigate such risks.\r

  Disclosure and Potential Misuse. Similar to other adversarial attack studies [84, 98, 99], the newly discovered vulnerabilities in our work may provide insight for potential attackers.\r

  Nonetheless, we believe that responsible disclosure is generally more beneficial than withholding such findings. To prevent potential misuse, our team has established strict internal regulations and requirements. All code of GradEscape was developed and maintained solely by the first author, who is the only person with access to it. We stored our trained evaders on a server that requires public key authentication to log in, lest they be stolen by unauthorized parties. No individuals outside our team have access to the server.\r

  Possible Defense. We propose an active paraphrasing defense method to neutralize the adversarial modifications made by evaders. Experimental results show that this approach can reduce the evasion rate to below 0.2 at the cost of additional computational overhead for paraphrasing. For overhead sensitive scenarios, developers may opt for a perplexity-based filter, as our findings suggest that strong attacks often increase text perplexity. However, perplexity filters can cause a lot of false positives when the input is from a diverse source [100].\r

  A recent study introduced certified robustness techniques into NLP classification models [101], offering rigorous guarantees against textual adversarial attacks.

  Responsible Real-world Deployment and Human Evaluation. We implement several measures to ensure our real world studies do not harm actual systems or users. For the dataset, we exclusively choose publicly available corpora. The human-generated texts were sourced from open-access web sites such as Reddit, Wikipedia, and OpenWebText. Querying cloud-based AIGT detectors with these texts does not involve private data. When querying Sapling, we employed the official API and paid a total of $20.25 for building evaders. For Scribbr, we employed an automated script to simulate user interactions with the WebUI. To avoid placing an unnecessary load on Scribbr’s infrastructure, all queries were sent at night in U.S. Eastern Time. They have updated their service models.

  Therefore, publishing our work poses no severe harm to these platforms. For human evaluation, we consulted and obtained approval from our IRB and paid our crowdworkers at a rate exceeding the minimum hourly wage in our hiring region."
Framework Used:
  - Custom
Indirect Stakeholders:
  - Adversaries
key_quotes: ""
Menlo.Beneficience: true
Menlo.Justice: false
Menlo.RespectForLawAndPublicInterest: true
Menlo.RespectForPersons: true
notes: "The paper covers a lot of ground: proposes a tool, and the means of mitigation and does live testing as well as include human participants for annotating during evaluation. All of these are addressed in the ethics section, including the potential misuse. They have outlined their responsible approach to real world testing as well. Scribbr is indicated to have updated their service models, however communications between the research team an the service providers have not been transparently outlined, merely implied."
pages: 181--200
Research Domain:
  - Large Language Models (LLM)
Research_Type:
  - System
  - Vuln Research
Risk Benefit Analysis: true
Status: Data coded
Subdomain:
  - LLM Security
title: "GradEscape: {A} Gradient-Based Evader Against AI-Generated Text Detectors"
url: https://www.usenix.org/conference/usenixsecurity25/presentation/meng
Usenix.DataPrivacy: true
Usenix.HarmMitigation: true
Usenix.HumanSubjects: true
Usenix.LiveTesting: true
Usenix.ResearcherSafety: false
Usenix.StakeholderImpact: false
Usenix.ToSViolation: false
Usenix.VulnDisclosure: true
coded_date: 2026-09-29
kanban_order: 2
---
