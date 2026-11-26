---
Alternatives Considered: false
author: Chris S. Lin and Joyce Qu and Gururaj Saileshwar
author_tags:
  - Chris S. Lin
  - Joyce Qu
  - Gururaj Saileshwar
base: "[[Databook.base]]"
DBLP Ref: DBLP:conf/uss/LinQS25
Direct Stakeholders:
  - Software Maintainers
Emerging Themes: []
Ethics Depth:
  - Brief
Ethics Location:
  - Main Body
Ethics section: We responsibly disclosed the Rowhammer vulnerability in the A6000 GPU to NVIDIA on 15th January, 2025, sharing proof-of-concept code and a draft of our paper. Subsequently, we also disclosed our findings to major cloud providers (AWS, Azure, GCP) who may be affected, so that the vulnerability is addressed before public dissemination. Our experiments were conducted locally or in isolated environments, and targeted open-source models, mitigating risks to production systems.
Framework Used:
  - Custom
Indirect Stakeholders:
  - Broader Public
  - Adversaries
kanban_order: 3
key_quotes: ""
Menlo.Beneficience: false
Menlo.Justice: false
Menlo.RespectForLawAndPublicInterest: false
Menlo.RespectForPersons: true
notes: The paper does have a Mitigations section that explains various means of mitigation against the GPURowhammer attack. The overall paper addresses and acknowledges the impact of the tool on stakeholders, and the Ethics section covers responsible disclosure. However, a risk-benefits analysis would greatly benefit the paper, as it introduces a new attack vector for adversaries, even if patched by the stakeholder.
pages: 5719--5738
Research Domain:
  - Hardware & Embedded Systems Security
Research_Type:
  - Vuln Research
Risk Benefit Analysis: false
Status: Data coded
Subdomain:
  - Hardware Security
  - Side-Channel and Fault Injection Attacks
title: "GPUHammer: Rowhammer Attacks on {GPU} Memories are Practical"
url: https://www.usenix.org/conference/usenixsecurity25/presentation/lin-shaopeng
Usenix.DataPrivacy: false
Usenix.HarmMitigation: true
Usenix.HumanSubjects: false
Usenix.LiveTesting: false
Usenix.ResearcherSafety: false
Usenix.StakeholderImpact: true
Usenix.ToSViolation: false
Usenix.VulnDisclosure: true
coded_date: 2026-09-28
---
