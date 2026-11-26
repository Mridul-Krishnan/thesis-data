---
Alternatives Considered: false
author: Mark DenHoed and Tom Melham
author_tags:
  - Mark DenHoed
  - Tom Melham
base: "[[Databook.base]]"
DBLP Ref: DBLP:conf/uss/DenHoedM25
Direct Stakeholders:
  - Software Maintainers
Emerging Themes: []
Ethics Depth:
  - Brief
Ethics Location:
  - Main Body
Ethics section: "All research into offensive techniques carries the risk of enabling bad actors. Such research contributions must be weighed against the potential harm they might cause. We believe the benefit of our research outweighs these risks.\r

  Our formal model of p-code in logic , taken on its own, merely provides a way to reason about binary code. While our p-code modeling is novel, the concept of modeling native code with propositional logic is well-established and extensively used in tools such as the popular symbolic executor angr.\r

  We believe there is a net benefit in releasing our code-reuse attack synthesis algorithm.\r

  There is a long history of interplay between offensive and defensive security research. Providing new methods for code reuse-attack synthesis may shed light on new mitigations, or provide new tools for those developing defenses against these techniques. Additionally, while this work presents novel techniques and applications, it does not uncover previously unknown vulnerabilities in computer systems."
Framework Used:
  - Custom
Indirect Stakeholders:
  - Adversaries
  - Broader Public
  - End Users
key_quotes: ""
Menlo.Beneficience: true
Menlo.Justice: false
Menlo.RespectForLawAndPublicInterest: false
Menlo.RespectForPersons: false
notes: The team ensures using previously known CVEs for real world testing of the proposed tool. It recognises the possible use by adversaries and does a risk benefit analysis. However, it is missing some form of usability analysis, thorough analysis of stakeholders and impact on them, detailed mitigation or alternatives considered.
pages: 395--411
Research Domain:
  - Software Security & Development Lifecycle
Research_Type:
  - Vuln Research
  - System
Risk Benefit Analysis: true
Status: Data coded
Subdomain:
  - Software Security
title: Synthesis of Code-Reuse Attacks from p-code Programs
url: https://www.usenix.org/conference/usenixsecurity25/presentation/denhoed
Usenix.DataPrivacy: false
Usenix.HarmMitigation: false
Usenix.HumanSubjects: false
Usenix.LiveTesting: false
Usenix.ResearcherSafety: false
Usenix.StakeholderImpact: true
Usenix.ToSViolation: false
Usenix.VulnDisclosure: false
coded_date: 2026-09-29
kanban_order: 5
---
