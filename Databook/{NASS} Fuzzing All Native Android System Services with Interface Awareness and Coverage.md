---
Alternatives Considered: false
author: Philipp Mao and Marcel Busch and Mathias Payer
author_tags:
  - Philipp Mao
  - Marcel Busch
  - Mathias Payer
base: "[[Databook.base]]"
DBLP Ref: DBLP:conf/uss/MaoBP25
Direct Stakeholders:
  - Software Maintainers
Emerging Themes: []
Ethics Depth:
  - Brief
Ethics Location:
  - Main Body
Ethics section: As part of our evaluation, we discovered vulnerabilities on COTSphones. These vulnerabilities could be weaponized to target real people. We understand the criticality of our findings, and we have disclosed all vulnerabilities discovered by NASS immediately after discovery to the responsible vendors. The five assigned CVEs serve as proof of our dedication to responsible disclosure. At the time of publication, all affected vendors had at least 90 days to address the disclosed vulnerabilities. We present novel techniques to help discover vulnerabilities. We are aware that these techniques could also be lever aged by malicious actors. We contend that security through obscurity is not a sustainable strategy for safeguarding soft ware. By openly sharing our findings, we empower organizations and researchers to harden native RPC servers, reducing the overall attack surface available to malicious actors.
Framework Used:
  - None Explicit
Indirect Stakeholders:
  - End Users
kanban_order: 10
key_quotes: We contend that security through obscurity is not a sustainable strategy for safeguarding software.
Menlo.Beneficience: true
Menlo.Justice: true
Menlo.RespectForLawAndPublicInterest: false
Menlo.RespectForPersons: false
notes: The paper proposes NASS, an RPC fuzzer. The ethics section is short but brief, it covers stakeholder (vendor) impact, and the communication of the vulns to stakeholders. It also includes a risk benefit analysis. Table 5 and Section 8.4 discusses live localized testing on 5 devices and the respective CVEs and disclosure statuses.
pages: 4225--4243
Research Domain:
  - System Security & Threat Detection
Research_Type:
  - Measurement
  - System
  - Vuln Research
Risk Benefit Analysis: true
Status: Data coded
Subdomain:
  - System Security
  - Mobile Platforms
title: "{NASS:} Fuzzing All Native Android System Services with Interface Awareness and Coverage"
url: https://www.usenix.org/conference/usenixsecurity25/presentation/mao
Usenix.DataPrivacy: false
Usenix.HarmMitigation: true
Usenix.HumanSubjects: false
Usenix.LiveTesting: true
Usenix.ResearcherSafety: false
Usenix.StakeholderImpact: false
Usenix.ToSViolation: false
Usenix.VulnDisclosure: true
coded_date: 2026-09-30
---
