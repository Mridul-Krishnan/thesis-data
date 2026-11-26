---
Alternatives Considered: false
author: Tuan Dinh Hoang and Taekkyung Oh and CheolJun Park and Insu Yun and Yongdae Kim
author_tags:
  - Tuan Dinh Hoang
  - Taekkyung Oh
  - CheolJun Park
  - Insu Yun
  - Yongdae Kim
base: "[[Databook.base]]"
DBLP Ref: DBLP:conf/uss/HoangOPYK25
Direct Stakeholders:
  - System Operators
Emerging Themes:
Ethics Depth:
  - Brief
Ethics Location:
  - Main Body
Ethics section: "Responsible Disclosure. \r

  We responsibly disclosed all our findings to the baseband vendors, providing detailed reports and engaging in discussions to assist their investigations. As a result, the status of disclosed vulnerabilities is as follows: \r

  • Bugs B1 and B2 have already been patched by Qualcomm, and bugs B4, B5, and B7 have already been patched by MediaTek. \r

  • Bug B6 affects only older baseband firmware versions and had already been patched in the latest firmware. \r

  • Bugs B8, and B9 have been successfully verified, and vendors are working on releasing patches.\r

  • Bug B3 is still under review, and we are actively assisting the vendor in reproducing it. We continue to work closely with the vendors to ensure these issues are fully addressed. \r

  \r

  Controlled Experiment. \r

  We conducted our experiment in a isolated environment (i.e. Faraday cage) to prevent malicious signals from affecting other cellular devices. Also, we operate our base station in a frequency band that is not used by commercial cellular networks. This setup ensures that our experiment does not violate any local regulations in our country."
Framework Used:
  - None Explicit
Indirect Stakeholders:
  - Adversaries
  - Broader Public
kanban_order: 6
key_quotes: ""
Menlo.Beneficience: true
Menlo.Justice: false
Menlo.RespectForLawAndPublicInterest: true
Menlo.RespectForPersons: false
notes: Under the section Bug Discovery, the author cover the security implications of how adversaries could use their LLFuzz tool.
pages: 5267--5286
Research Domain:
  - Network Security & Infrastructure
Research_Type:
  - System
  - Vuln Research
Risk Benefit Analysis: false
Status: Data coded
Subdomain:
  - Network Security
  - BLE and Cellular
title: "LLFuzz: An Over-the-Air Dynamic Testing Framework for Cellular Baseband Lower Layers"
url: https://www.usenix.org/conference/usenixsecurity25/presentation/hoang
Usenix.DataPrivacy: false
Usenix.HarmMitigation: false
Usenix.HumanSubjects: false
Usenix.LiveTesting: false
Usenix.ResearcherSafety: false
Usenix.StakeholderImpact: true
Usenix.ToSViolation: false
Usenix.VulnDisclosure: true
coded_date: 2026-11-01
---
