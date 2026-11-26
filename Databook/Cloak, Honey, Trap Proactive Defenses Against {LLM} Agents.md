---
Alternatives Considered: false
author: Daniel Ayzenshteyn and Roy Weiss and Yisroel Mirsky
author_tags:
  - Daniel Ayzenshteyn
  - Roy Weiss
  - Yisroel Mirsky
base: "[[Databook.base]]"
DBLP Ref: DBLP:conf/uss/AyzenshteynWM25
Direct Stakeholders: []
Emerging Themes: []
Ethics Depth:
Ethics Location: []
Ethics section: "This work proposes defensive strategies against malicious LLM agents by identifying and exploiting inherent vulnerabilities in model behavior and agent design. All experiments were conducted in isolated CTF environments with no inter action with real users, systems, or networks.\r

  We acknowledge the dual-use potential of techniques such as hallucination induction, agent manipulation, and adversarial tokens. While these could be misused, we believe our framework is a greater benefit to defenders than attackers.\r

  The most immediate vulnerability is the “token mines” which were disclosed to Meta, Mistral, and TII on April 28, 2025 (see Table 11). A straightforward mitigation is to halt generation when model confidence in upcoming tokens sharply declines. To reduce risk, of the token mine artifacts will be delayed by one month post-publication, giving users time to implement protections.\r

  We believe responsible disclosure and transparent publication serve defenders far more than attackers. Public scrutiny enables the research and security communities to anticipate, mitigate, and ultimately eliminate emerging threats. Security through obscurity is unsustainable; resilience depends on openness and proactive defense."
Framework Used: []
Indirect Stakeholders: []
key_quotes: ""
Menlo.Beneficience: false
Menlo.Justice: false
Menlo.RespectForLawAndPublicInterest: false
Menlo.RespectForPersons: false
notes: ""
pages: 8095--8114
Research Domain:
  - Large Language Models (LLM)
Research_Type: []
Risk Benefit Analysis: false
Status: Ethics Section Extracted
Subdomain:
  - Vulnerabilities in LLMs
  - Privacy Safety and Defense
title: "Cloak, Honey, Trap: Proactive Defenses Against {LLM} Agents"
url: https://www.usenix.org/conference/usenixsecurity25/presentation/ayzenshteyn
Usenix.DataPrivacy: false
Usenix.HarmMitigation: false
Usenix.HumanSubjects: false
Usenix.LiveTesting: false
Usenix.ResearcherSafety: false
Usenix.StakeholderImpact: false
Usenix.ToSViolation: false
Usenix.VulnDisclosure: false
coded_date: 2026-09-07
---
