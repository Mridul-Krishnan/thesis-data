---
Alternatives Considered: false
author: Fengyu Liu and Yuan Zhang and Jiaqi Luo and Jiarun Dai and Tian Chen and Letian Yuan and Zhengmin Yu and Youkun Shi and Ke Li and Chengyuan Zhou and Hao Chen and Min Yang
author_tags:
  - Fengyu Liu
  - Yuan Zhang
  - Jiaqi Luo
  - Jiarun Dai
  - Tian Chen
  - Letian Yuan
  - Zhengmin Yu
  - Youkun Shi
  - Ke Li
  - Chengyuan Zhou
  - Hao Chen
  - Min Yang
base: "[[Databook.base]]"
DBLP Ref: DBLP:conf/uss/Liu0LDCYYSLZ0025
Direct Stakeholders:
  - Software Maintainers
Emerging Themes: []
Ethics Depth:
  - Minimal
Ethics Location:
  - Main Body
Ethics section: Vulnerability Verification Environment. In our evaluation part, all of the agents are open-source, and we downloaded and conducted static analysis on them locally through AgentFuzz. This process did not involve any data related to real user privacy. Then, after AgentFuzz reported potential vulnerabilities, we built these agents on a local server for vulnerability verification. This process also did not involve any data related to real users. Vulnerability Disclosure. In terms of vulnerability disclosure, all our vulnerability reports have strictly adhered to the time line of the CVE Numbering Authorities (CNA), along with proactive communication with all developers. Specifically, after we manually confirmed the vulnerabilities, we immediately contacted the developers, including raising issues in the Github repository and via email. We carefully explained to the developers the cause of the vulnerability, the details of vulnerability exploitation, and the corresponding recommended solutions for fixing the issues. Although some vulnerabilities were still being fixed at the time we submitted this paper, we did not mention any important information about these vulnerabilities in the paper and anonymized all vulnerabilities and affected applications. Therefore, the release of this paper will not cause any harm to real-world users.
Framework Used:
  - Custom
Indirect Stakeholders:
  - Adversaries
  - End Users
kanban_order: 0
key_quotes: ""
Menlo.Beneficience: false
Menlo.Justice: false
Menlo.RespectForLawAndPublicInterest: true
Menlo.RespectForPersons: false
notes: They have followed through on proper reporting of the vulnerabilities discovered by their tool, AgentFuzz. However, they have no discussed the impact of their tool on LLM based applications as their tool can be used by bad actors to discover new taint style vulnerabilities. A risk-benefit analysis would be very valuable in their discussions.
pages: 3767--3786
Research Domain:
  - Large Language Models (LLM)
Research_Type:
  - System
  - Vuln Research
Risk Benefit Analysis: false
Status: Data coded
Subdomain:
  - LLM Security
title: "Make Agent Defeat Agent: Automatic Detection of Taint-Style Vulnerabilities in LLM-based Agents"
url: https://www.usenix.org/conference/usenixsecurity25/presentation/liu-fengyu
Usenix.DataPrivacy: true
Usenix.HarmMitigation: true
Usenix.HumanSubjects: false
Usenix.LiveTesting: false
Usenix.ResearcherSafety: false
Usenix.StakeholderImpact: true
Usenix.ToSViolation: false
Usenix.VulnDisclosure: true
coded_date: 2026-09-28
---
