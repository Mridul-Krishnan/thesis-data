---
Alternatives Considered: false
author: Antoine Delignat{-}Lavaud and C{\'{e}}dric Fournet and Kapil Vaswani and Manuel Costa and Sylvan Clebsch and Christoph M. Wintersteiger
author_tags:
  - Antoine Delignat{-}Lavaud
  - C{\'{e}}dric Fournet
  - Kapil Vaswani
  - Manuel Costa
  - Sylvan Clebsch
  - Christoph M. Wintersteiger
base: "[[Databook.base]]"
DBLP Ref: DBLP:conf/uss/Delignat-Lavaud25
Direct Stakeholders:
  - System Operators
Emerging Themes:
  - Usability Analysis
Ethics Depth:
  - Brief
Ethics Location:
  - Main Body
Ethics section: "Our goal is to improve Internet security for service providers and their users, by providing a usable, transparent, and auditable way to distribute and verify the attestations of confidential service implementations. Even a trivial service policy that just checks the service runs in a valid TEE improves security against compromise of the service operator (e.g. public clouds). Confidential computing may be used by malicious service owners to build end-to-end encrypted platforms (e.g.\r

  to share or distribute illegal content). Our research does not amplify this risk—on the contrary, aDNS is designed to make service owners accountable for the policy and code they de ploy under the service name. Existing DNS-based censorship mechanisms are largely unimpacted by aDNS.\r

  Our design and prototype implementation build on open standards whenever possible. In particular, we comply with DNS,DNSSEC, ACME, DANE, and related standards, and we do not decrease their security for their existing users.\r

  Regarding user privacy, the additional records used by aDNS do not reveal more information than the name of the service, which already appears in the IP address resolution query. Privacy conscious users can use DNS over HTTPS to ensure network observers can’t track their service usage, though this only works if the resolver is shared by many users as network traffic to authoritative DNS servers leaks a lot of information about potential services. A confidential DoH resolver can also mitigate trust in the resolver, though this protection should be evaluated against the risks of side channels of their particular TEE platforms. Our research and its experimental evaluation did not involve any private data."
Framework Used:
  - None Explicit
Indirect Stakeholders:
  - End Users
key_quotes: ""
Menlo.Beneficience: true
Menlo.Justice: false
Menlo.RespectForLawAndPublicInterest: true
Menlo.RespectForPersons: false
notes: It proposes a protocol which only has improved accountability compared to the existing system. There is a dedicated section, Implementation, that covers how both clients and servers can implement the system, which can be considered a form of Usability Analysis. The ethics section covers the risk benefit analysis. The paper doesn't have any other avenues to cover.
pages: 1129--1148
Research Domain:
  - Hardware & Embedded Systems Security
Research_Type:
  - System
  - Theory
  - Measurement
Risk Benefit Analysis: true
Status: Data coded
Subdomain:
  - System Security
  - Trusted and Robust Computing
title: Transparent Attested {DNS} for Confidential Computing Services
url: https://www.usenix.org/conference/usenixsecurity25/presentation/delignat-lavaud
Usenix.DataPrivacy: true
Usenix.HarmMitigation: true
Usenix.HumanSubjects: false
Usenix.LiveTesting: false
Usenix.ResearcherSafety: false
Usenix.StakeholderImpact: true
Usenix.ToSViolation: false
Usenix.VulnDisclosure: false
coded_date: 2026-09-29
kanban_order: 6
---
