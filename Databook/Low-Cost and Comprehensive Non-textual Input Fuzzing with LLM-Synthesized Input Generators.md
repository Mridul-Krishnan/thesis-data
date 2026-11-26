---
Alternatives Considered: false
author: Kunpeng Zhang and Zongjie Li and Daoyuan Wu and Shuai Wang and Xin Xia
author_tags:
  - Kunpeng Zhang
  - Zongjie Li
  - Daoyuan Wu
  - Shuai Wang
  - Xin Xia
base: "[[Databook.base]]"
DBLP Ref: DBLP:conf/uss/ZhangLW0025
Direct Stakeholders: []
Emerging Themes: []
Ethics Depth:
Ethics Location: []
Ethics section: "Vulnerability Disclosure. Our fuzzing tool is designed to uncover security vulnerabilities in software. If we identify such vulnerabilities, failing to disclose them responsibly could lead to serious security risks, such as unauthorized access or exploitation by malicious actors.\r

  We have established a responsible disclosure process.\r

  When we find vulnerabilities, we promptly notify the affected software vendors, giving them sufficient time to patch the issues before making any public disclosures. This ensures our research contributes positively to security without exposing users to unnecessary risks.\r

  Experiments with Live Systems Without Informed Con sent. If we apply our fuzzing tool to live systems or real-world software without obtaining consent from the owners or operators, this could disrupt services or negatively impact users who rely on those systems.\r

  We avoid testing live systems without explicit consent from the system owners. When testing on live systems is necessary, we first obtain informed consent and design our testing methods to minimize any potential harm or disruption. This approach respects the rights and interests of those who rely on the systems we study.\r

  Terms of Service. Our tool could potentially violate the terms of service of the software we are testing, particularly if the software explicitly prohibits automated testing or fuzzing.\r

  This could lead to legal issues or harm our reputation in the research community.\r

  Before conducting any fuzzing, we thoroughly review the terms of service of the software being tested. If our activities might violate these terms, we seek permission from the soft ware provider or adjust our methods to avoid violations. This ensures our research is both ethical and legally compliant.\r

  Deception. If our testing involves any form of deception, such as obscuring the true nature of the tests from the system administrators or users, this could raise ethical concerns, particularly if it results in harm or a loss of trust.\r

  We avoid using deception in our research. If deception is necessary for the validity of the study, it is ethically justified and followed by a thorough debriefing to explain the research’s purpose and methods to all affected parties. This approach maintains transparency and trust.\r

  Wellbeing for Team Members. Our work may expose team members to stressful or disturbing content, especially when analyzing malicious software, which could impact their psychological wellbeing.\r

  We prioritize our team’s wellbeing by supporting those exposed to stressful content, setting clear boundaries, and maintaining a safe, supportive work environment.\r

  Innovations with Both Positive and Negative PotentialOut comes. The tools and techniques we develop have potential for misuse by adversaries. While our intention is to improve software security, there is a risk that others could use our tool to find and exploit vulnerabilities for malicious purposes.\r

  We recognize the dual-use nature of our tool and have implemented safeguards to prevent misuse. Access is restricted, and we work with ethical review boards to assess risks. We also engage with the security community to ensure our re search is used positively.\r

  Retroactively Identifying Negative Outcomes. If our re search unintentionally causes negative outcomes, like service disruptions or exploitation of vulnerabilities, failing to address them could harm users and damage our credibility.\r

  We will monitor for any issues and take responsibility if they arise, working to remediate any harm. This proactive approach ensures our research remains ethical and responsible.\r

  The Law. Our fuzzing activities must comply with cybersecurity laws and regulations. Any inadvertent violations could lead to legal consequences for us and our institution.\r

  We consult legal experts to ensure compliance and obtain necessary approvals before engaging in risky activities, minimizing legal risks and ensuring proper conduct."
Framework Used: []
Indirect Stakeholders: []
key_quotes: ""
Menlo.Beneficience: false
Menlo.Justice: false
Menlo.RespectForLawAndPublicInterest: false
Menlo.RespectForPersons: false
notes: ""
pages: 6999--7018
Research Domain:
  - Software Security & Development Lifecycle
Research_Type: []
Risk Benefit Analysis: false
Status: Ethics Section Extracted
Subdomain:
  - Software Security
  - Fuzzing and Other Software Analysis
title: Low-Cost and Comprehensive Non-textual Input Fuzzing with LLM-Synthesized Input Generators
url: https://www.usenix.org/conference/usenixsecurity25/presentation/zhang-kunpeng
Usenix.DataPrivacy: false
Usenix.HarmMitigation: false
Usenix.HumanSubjects: false
Usenix.LiveTesting: false
Usenix.ResearcherSafety: false
Usenix.StakeholderImpact: false
Usenix.ToSViolation: false
Usenix.VulnDisclosure: false
coded_date: 2026-09-08
---
