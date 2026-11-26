---
Alternatives Considered: false
author: Juyang Bai and Md Hafizul Islam Chowdhuryy and Jingtao Li and Fan Yao and Chaitali Chakrabarti and Deliang Fan
author_tags:
  - Juyang Bai
  - Md Hafizul Islam Chowdhuryy
  - Jingtao Li
  - Fan Yao
  - Chaitali Chakrabarti
  - Deliang Fan
base: "[[Databook.base]]"
DBLP Ref: DBLP:conf/uss/BaiCLYCF25
Direct Stakeholders: []
Emerging Themes: []
Ethics Depth:
Ethics Location: []
Ethics section: In developing Phantom, we conducted a thorough ethical analysis to ensure responsible innovation while protecting legitimate security interests. Our analysis focused on key stakeholder impacts and technical design decisions that could affect different parties involved in the deployment and use of our system. From a stakeholder perspective, we primarily considered model owners who face significant risks from model theft that could undermine their competitive advantage. Our research addresses their need for intellectual property protection while maintaining reasonable implementation costs through our Top-K sensitivity optimization. For legitimate users, our system ensures authorized users maintain high model accuracy with minimal performance overhead, where the Top-K layer sensitivity analysis specifically optimizes this balance between security and efficiency. Regarding the broader research community, while our work advances model protection techniques, we acknowledge potential misuse risks. Therefore, we focus on defensive techniques and transparently document their capabilities. Our technical design choices were guided by ethical considerations at each step. We chose obfuscation over full encryption to balance security with practical deployment constraints, particularly for resource-constrained organizations. Our selective layer protection approach through sensitivity analysis achieves robust security while minimizing system overhead. Throughout development and evaluation, we used only public datasets (CIFAR-10, CIFAR-100, STL-10) and commit to open-sourcing our implementation to ensure transparency and reproducibility
Framework Used: []
Indirect Stakeholders: []
kanban_order: 28
key_quotes: ""
Menlo.Beneficience: false
Menlo.Justice: false
Menlo.RespectForLawAndPublicInterest: false
Menlo.RespectForPersons: false
notes: ""
pages: 5565--5582
Research Domain:
  - Machine Learning & AI (non-LLM)
Research_Type: []
Risk Benefit Analysis: false
Status: Ethics Section Extracted
Subdomain:
  - ML and AI Privacy
title: "Phantom: Privacy-Preserving Deep Neural Network Model Obfuscation in Heterogeneous {TEE} and {GPU} System"
url: https://www.usenix.org/conference/usenixsecurity25/presentation/bai-juyang
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
