---
Alternatives Considered: false
author: Daniel Weber and Lukas Gerlach and Leon Trampert and Youheng L{\"{u}} and Jo Van Bulck and Michael Schwarz
author_tags:
  - Daniel Weber
  - Lukas Gerlach
  - Leon Trampert
  - Youheng L{\"{u}}
  - Jo Van Bulck
  - Michael Schwarz
base: "[[Databook.base]]"
coded_date: 2026-05-05T17:01:00
DBLP Ref: DBLP:conf/uss/00070TLB025
Direct Stakeholders:
  - Software Maintainers
Emerging Themes: []
Ethics Depth: Minimal
Ethics Location:
  - Main Body
Ethics section: The tool proposed in this work does not discover new vulnerabilities but rather automates the exploitation of known vulnerabilities. Hence, we do not see a direct ethical concern. While it could be used to assist in implementing attack applications, it is intended to be used for defensive purposes and lowers the barrier for security researchers to evaluate the security of an application. Furthermore, our experiments have been conducted on machines belonging to the authors themselves or their affiliation and do not involve any personal data. Nevertheless, to ensure that Intel is aware of our PoC implementation, we disclosed our work to them.
Framework Used:
  - None Explicit
Indirect Stakeholders:
  - Broader Public
  - End Users
key_quotes: |-
  “Athena makes PoC generation faster for
  experts and accessible to a broader audience.
  ”
Menlo.Beneficience: true
Menlo.Justice: false
Menlo.RespectForLawAndPublicInterest: false
Menlo.RespectForPersons: false
notes: The paper introduces a PoC framework called Athena that automatically recovers secrets from Intel SGX enclaves via controlled channels. It paves a way to automate software-based side-channel attacks without an in-depth understanding of the target application. The authors address that it is not a direct ethical concern as the tool automates exploitation of known vulnerabilities, however that is very debatable as it clearly reduces the software information gap a side-channel attacker may face . There is also no usability analysis however the steps for usage is outlined to an extent. They have  disclosed their implementation to Intel, but otherwise their ethical discussion is very minimal and seems dismissive of ethical concerns.
pages: 5739--5758
Research Domain:
  - Hardware & Embedded Systems Security
Research_Type:
  - System
  - Vuln Research
Risk Benefit Analysis: false
Status: Data coded
Subdomain:
  - Hardware Security
  - Side-Channel and Fault Injection Attacks
title: "{SCASE:} Automated Secret Recovery via Side-Channel-Assisted Symbolic Execution"
url: https://www.usenix.org/conference/usenixsecurity25/presentation/weber
Usenix.DataPrivacy: false
Usenix.HarmMitigation: true
Usenix.HumanSubjects: false
Usenix.LiveTesting: false
Usenix.ResearcherSafety: false
Usenix.StakeholderImpact: true
Usenix.ToSViolation: false
Usenix.VulnDisclosure: true
---
