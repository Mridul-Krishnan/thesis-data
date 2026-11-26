---
Alternatives Considered: false
author: Youkun Shi and Yuan Zhang and Tianhao Bai and Feng Xue and Jiarun Dai and Fengyu Liu and Lei Zhang and Xiapu Luo and Min Yang
author_tags:
  - Youkun Shi
  - Yuan Zhang
  - Tianhao Bai
  - Feng Xue
  - Jiarun Dai
  - Fengyu Liu
  - Lei Zhang
  - Xiapu Luo
  - Min Yang
base: "[[Databook.base]]"
DBLP Ref: DBLP:conf/uss/Shi0BXDL0L025
Direct Stakeholders: []
Emerging Themes: []
Ethics Depth:
Ethics Location: []
Ethics section: "This research was conducted with careful attention to ethical responsibilities, which are detailed below.\r

  Vulnerability Verification Environment. In our evaluation part, all of the applications are open-source, and we down loaded and conducted analysis on them locally through XSSky.\r

  This process did not involve any data related to real user privacy. Then, after XSSky reported potential vulnerabilities, we built these applications on a local server for vulnerability verification. This process also did not involve any user privacy.\r

  Vulnerability Disclosure. In terms of vulnerability disclosure, all our vulnerability reports have strictly adhered to the timeline of the CVE Numbering Authorities (CNA), along with proactive communication with all developers. Specifically, after we manually confirmed the vulnerabilities, we immediately contacted the developers, including raising is sues in the Github repository and via email. We carefully explained to the developers the cause of the vulnerability, the details of vulnerability exploitation, and the corresponding recommended solutions for fixing the issues. Although the detected vulnerabilities were still being fixed at the time we submitted this paper, we did not mention any information about these vulnerabilities in the paper. Therefore, the release of this paper will not cause any harm to real-world users.\r

  Artifact Availability and Potential for Misuse. We have carefully considered the ethical implications of releasing the XSSky artifact.\r

  • Potential Risks: As a tool that proved effective in dis covering numerous previously unknown XSS vulnerabilities, with many involving sanitizer bypasses, XSSky could be repurposed by malicious actors to find and exploit vulnerabilities in live web applications. We acknowledge that while other XSS testing tools are publicly avail able, XSSky’s novel path-persistent fuzzing and interpreter feedback mechanisms may grant it an advantage in discovering vulnerabilities that other tools miss, heightening the risk of misuse.\r

  • Mitigating Factors in Real-World Systems: We recognize that modern applications often deploy defense-in-depth mechanisms. Security measures like a well-configured Content Security Policy (CSP), Web Application Firewalls (WAFs), or Trusted Types can mitigate or block the exploitation of XSS vulnerabilities. However, these defenses are not universally adopted, can be misconfigured, and are sometimes overlooked.\r

  • Trade-offs and Our Approach: We weighed the risks of unrestricted release against the scientific benefits of open access. Releasing the tool without any controls could empower attackers, but restricting it entirely would prevent the community from building on our work to create better defenses. We have therefore chosen a middle ground: controlled distribution. By making the artifact available upon request to identified researchers, we aim to support legitimate scientific inquiry while adding a layer of account ability that deters casual misuse. This approach balances our commitment to open science with our ethical duty to prevent foreseeable harm."
Framework Used: []
Indirect Stakeholders: []
key_quotes: ""
Menlo.Beneficience: false
Menlo.Justice: false
Menlo.RespectForLawAndPublicInterest: false
Menlo.RespectForPersons: false
notes: ""
pages: 8255--8272
Research Domain:
  - Software Security & Development Lifecycle
Research_Type: []
Risk Benefit Analysis: false
Status: Ethics Section Extracted
Subdomain:
  - Web Security
title: "XSSky: Detecting {XSS} Vulnerabilities through Local Path-Persistent Fuzzing"
url: https://www.usenix.org/conference/usenixsecurity25/presentation/shi-youkun
Usenix.DataPrivacy: false
Usenix.HarmMitigation: false
Usenix.HumanSubjects: false
Usenix.LiveTesting: false
Usenix.ResearcherSafety: false
Usenix.StakeholderImpact: false
Usenix.ToSViolation: false
Usenix.VulnDisclosure: false
coded_date: 2026-09-16
---
