---
Alternatives Considered: false
author: Marcos Bajo and Christian Rossow
author_tags:
  - Marcos Bajo
  - Christian Rossow
base: "[[Databook.base]]"
DBLP Ref: DBLP:conf/uss/BajoR25
Direct Stakeholders: []
Emerging Themes: []
Ethics Depth:
Ethics Location: []
Ethics section: All experiments carried out in this paper were done in an isolated manner against locally-hosted services. We did not interact with real-world systems to avoid any damage. Since this paper shows that the current implementation of C++ coroutines in the three major compilers—Clang/LLVM, GCC and MSVC—is vulnerable, we initiated a disclosure process with the corresponding parties to raise awareness and to provide developers the opportunity to implement our pro posed mitigations. We shared a copy of this paper with the affected compiler developers in November 2024. The general consensus was that this should not be classified as a security vulnerability but rather as a hardening opportunity against a novel exploitation technique. The Clang/LLVM developers acknowledged the issue and are actively discussing the best way to address it. The GCC developers have expressed their desire to open an upstream bug report when the paper is published. Meanwhile, the Microsoft Security Response Center referred the matter to the MSVC developers, from which we have not yet received further feedback. We declare no conflicts of interest or other ethical issues. We have not received funding from any of the affected parties.
Framework Used: []
Indirect Stakeholders: []
kanban_order: 10
key_quotes: ""
Menlo.Beneficience: false
Menlo.Justice: false
Menlo.RespectForLawAndPublicInterest: false
Menlo.RespectForPersons: false
notes: ""
pages: 7407--7426
Research Domain:
  - System Security & Threat Detection
Research_Type: []
Risk Benefit Analysis: false
Status: Ethics Section Extracted
Subdomain:
  - System Security
  - Kernel and Low-Level System Security
title: "Await() a Second: Evading Control Flow Integrity by Hijacking {C++} Coroutines"
url: https://www.usenix.org/conference/usenixsecurity25/presentation/bajo
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
