---
Alternatives Considered: false
author: Rujia Li and Jingyuan Ding and Qin Wang and Keting Jia and Haibin Zhang and Sisi Duan
author_tags:
  - Rujia Li
  - Jingyuan Ding
  - Qin Wang
  - Keting Jia
  - Haibin Zhang
  - Sisi Duan
base: "[[Databook.base]]"
coded_date: 2026-02-10T15:00:00
DBLP Ref: DBLP:conf/uss/0001D0JZD25
Direct Stakeholders:
  - System Operators
  - Software Maintainers
Emerging Themes: []
Ethics Depth: Brief
Ethics Location:
  - Main Body
Ethics section: |-
  Weare committed to complying with all relevant research
  ethics considerations. In particular, we are committed to the
  following principles:
  • RespectforPersons: Ourresearch does not involve human
  subjects or personal data. We respect the work of other
  researchers and properly cite all relevant prior work.
  • Beneficence: Our findings highlight a critical vulnerability
  in fast finality mechanism of BNB Smart Chain.
  • Justice: We strive to ensure our proposed modifications
  do not disproportionately impact or disadvantage any par
  ticular group of BSC users or validators. We have already
  disclosed our findings to BSC developers.
  • Respect for Law and Public Interest: No actions have
  been taken to exploit the identified vulnerabilities; instead,
  our research was conducted with the goal of improving the
  BSCsystem.
Framework Used:
  - Menlo
Indirect Stakeholders:
  - End Users
key_quotes: “Responsible disclosure. We have contacted the Binance team to disclose the attacks via Github and public channels (i.e., Medium). The attacks have been confirmed and acknowledged by the team.”
Menlo.Beneficience: true
Menlo.Justice: true
Menlo.RespectForLawAndPublicInterest: true
Menlo.RespectForPersons: true
notes: |-
  Binance team (direct stakeholder, system operator), was informed via Github, and the theoretical possibility of the first 2 attacks have been confirmed by a member (while hard to execute in practice), and addressed - Liveness issues exhibited by three attacks of Binance Consensus · Issue #3036 · bnb-chain/bsc . 
  A local testnet is used to do a Risk-Reward analysis from an adversarial pov.
pages: 4109--4125
Research Domain:
  - Blockchain & Distributed Ledger Security
Research_Type:
  - System
  - Theory
  - Vuln Research
Risk Benefit Analysis: true
Status: Data coded
Subdomain:
  - Blockchain Security Attacks and Defenses
  - Infrastructure Protocol Design and Governance
title: Does Finality Gadget Finalize Your Block? {A} Case Study of Binance Consensus
url: https://www.usenix.org/conference/usenixsecurity25/presentation/li-rujia
Usenix.DataPrivacy: false
Usenix.HarmMitigation: true
Usenix.HumanSubjects: false
Usenix.LiveTesting: false
Usenix.ResearcherSafety: false
Usenix.StakeholderImpact: true
Usenix.ToSViolation: false
Usenix.VulnDisclosure: true
---
