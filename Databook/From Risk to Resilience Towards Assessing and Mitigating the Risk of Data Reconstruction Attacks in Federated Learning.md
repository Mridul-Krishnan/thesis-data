---
Alternatives Considered: true
author: Xiangrui Xu and Zhize Li and Yufei Han and Bin Wang and Jiqiang Liu and Wei Wang
author_tags:
  - Xiangrui Xu
  - Zhize Li
  - Yufei Han
  - Bin Wang
  - Jiqiang Liu
  - Wei Wang
base: "[[Databook.base]]"
coded_date: 2026-02-09T14:05:00
DBLP Ref: DBLP:conf/uss/0001000L025
Direct Stakeholders:
  - System Operators
  - Data Subjects
Emerging Themes: []
Ethics Depth: Detailed
Ethics Location:
  - Extra Page
Ethics section: |-
  Ethics considerations
  Our work on quantifying and mitigating Data Reconstruction
  Attack (DRA) risks in Federated Learning (FL) systems raises several important ethical considerations that we have carefully
  evaluated:
  Stakeholder Analysis. We carefully considered impacts on
  three key stakeholder groups to ensure comprehensive ethical
  evaluation.
  1). FL Clients: Our primary stakeholders are individuals
  and organizations contributing private data to FL systems.
  While our research could potentially be misused to develop
  more sophisticated attacks, its main purpose is to help these
  stakeholders better understand and mitigate privacy leak risks.
  The actual risk to clients is negligible in our study as we only
  use public datasets and simulated attacks.
  2). FL System Operators: Ourworkprovides operators with
  tools to assess and improve their systems’ privacy guarantees.
  The potential negative outcome would be if operators misuse
  our risk quantification to justify inadequate protection mea
  sures. We mitigate this by clearly presenting the limitations
  of our framework.
  3). Research Community: There is a risk that our attack
  analysis could be repurposed for malicious use. However, we
  believe this is outweighed by the benefits of enabling more
  robust defenses. We follow responsible disclosure principles
  by focusing on defense development.
  Research Process Ethics. We implemented multiple safe
  guards to ensure ethical research practices throughout our
  study.
  1). Dataset Selection: Although we use only public datasets
  (CIFAR10, STL10, etc.), we recognize that even these may
  contain problematic representations. We carefully reviewed
  dataset provenance and content to ensure no obvious ethical
  violations.
  2). Attack Methodology: Our DRA simulations are con
  ducted in controlled environments with no actual privacy vi
  olations. All experiments use synthetically constructed or
  publicly available data.
  3). Defense Implications: Our proposed noise perturbation
  defenses are designed to preserve model utility while enhanc
  ing privacy. We acknowledge they may increase computa
  tional overhead, potentially excluding resource-constrained
  participants- an important trade-off we explicitly discuss.
  Risk-Benefit Analysis. We considered alternative approaches
  that might reduce risks:
  1). Not publishing attack methodology details (but this
  would limit defense development).
  2). Only studying defenses without analyzing attacks (but
  this would weaken the scientific contribution).
  After careful consideration, we concluded that the benefits
  of transparent, rigorous analysis outweigh the risks, given
  appropriate safeguards:
  1). We focus on fundamental properties of information
  leakage rather than optimizing attack performance.
  2). The proposed defense method in our study are practical
  and immediately applicable.
Framework Used:
  - USENIX Guidelines
Indirect Stakeholders:
  - End Users
  - Vulnerable Populations
key_quotes: |-
  First, we show that DRA risk is governed
  by the spectral properties of the Jacobian matrix of exchanged
  model updates or feature embeddings, providing a unified
  explanation for the effectiveness of defense methods. Sec
  ond, we develop InvRE, an InvLoss-based DRA risk estimator
  that offers attack method-agnostic, comprehensive risk eval
  uation across data instances and model architectures. Third,
  we propose two adaptive noise perturbation defenses that
  enhance FL privacy without harming classification accuracy.
  Extensive experiments on real-world datasets validate our
  framework, demonstrating its potential for systematic DRA
  risk evaluation and mitigation in FL systems.
Menlo.Beneficience: true
Menlo.Justice: true
Menlo.RespectForLawAndPublicInterest: true
Menlo.RespectForPersons: true
notes: Excellent. Considers alternatives and addresses why they weren’t chosen. Addressed their research team. Provided mitigation and detection methods for DRA and fills in gap in research of such. Recognises that attack methodology is necessary to work on defense development.
pages: 3141--3160
Research Domain:
  - Machine Learning & AI (non-LLM)
Research_Type:
  - System
  - Theory
  - Vuln Research
Risk Benefit Analysis: true
Status: Data coded
Subdomain:
  - ML and AI Privacy
  - Federated Learning and Protecting Data
title: "From Risk to Resilience: Towards Assessing and Mitigating the Risk of Data Reconstruction Attacks in Federated Learning"
url: https://www.usenix.org/conference/usenixsecurity25/presentation/xu-xiangrui
Usenix.DataPrivacy: true
Usenix.HarmMitigation: false
Usenix.HumanSubjects: false
Usenix.LiveTesting: false
Usenix.ResearcherSafety: true
Usenix.StakeholderImpact: true
Usenix.ToSViolation: false
Usenix.VulnDisclosure: true
---
