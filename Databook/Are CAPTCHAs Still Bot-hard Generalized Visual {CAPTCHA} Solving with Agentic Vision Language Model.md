---
Alternatives Considered: false
author: Xiwen Teoh and Yun Lin and Siqi Li and Ruofan Liu and Avi Sollomoni and Yaniv Harel and Jin Song Dong
author_tags:
  - Xiwen Teoh
  - Yun Lin
  - Siqi Li
  - Ruofan Liu
  - Avi Sollomoni
  - Yaniv Harel
  - Jin Song Dong
base: "[[Databook.base]]"
DBLP Ref: DBLP:conf/uss/Teoh0LLSH025
Direct Stakeholders:
  - Software Maintainers
Emerging Themes: []
Ethics Depth:
  - Detailed
Ethics Location:
  - Main Body
Ethics section: "A generalized CAPTCHA solver poses severe negative consequences for the Internet ecosystem. It can undermine community trust, degrade the quality of online experiences, and inflict financial loss on web service providers. We fully under stand the severity of this work. Therefore, we strictly adhered to these guidelines when conducting research.\r

  • Responsiblity and Disclosure. We actively communicated our findings with AI research organizations (i.e., OpenAI, Anthropic, DeepMind) and CAPTCHA services (i.e., Google, Cloudflare, Datadome, Arkose Labs).\r

  • Conscientious Sharing: We restrict our source code to registration only and permit access to researchers with verified credentials. For transparency, we will publicly release media demonstrations and execution traces.\r

  • Benchmark: The CAPTCHAs in the benchmark were solved offline with no interaction with the CAPTCHA providers. To construct the benchmark, we register our own API keys with CAPTCHA services or use demo websites.\r

  As a last resort, we scrape live websites.\r

  • FieldStudy: Halligan’s success is measured by its ability to retrieve a token from the CAPTCHA provider. Ultimately, only the target site that receives this token can determine its validity, as they possess the secret (or private key) to make a validation request to the CAPTCHA provider, and intermediaries such as 2Captcha could not do so. In theory, we could have retrieved a token and tampered with it before forwarding it to 2Captcha, thereby avoiding an active role in facilitating attacks against target sites. However, such tampering could raise suspicion if it resulted in errors reported by 2Captcha’s customers, potentially leading to our account being banned. Therefore, we opted for a relatively small-scale study (100 tasks/day) to minimize risk.\r

  • Affected Stakeholders: All experiments except the user study do not involve human subjects. Although website users could be indirectly affected by our benchmark collection, the potential impact remains minimal. We limit scrap ing to a small subset of CAPTCHAs (5 out of 26), which are otherwise unobtainable, capping it at 100 challenges per website. Based on published pricing from reCAPTCHA and hCaptcha, this represents around 0.1% of the typical monthly usage in the enterprise tier. To mitigate potential risks to scraped websites, we sanitize all identifiable information (e.g., domain names and CAPTCHA public keys).\r

  • User Study: This study received an exemption from our institutional review board due to the de-identification of participants in interviews and tests, absence of personally identifiable information, and the fact that disclosure of results posed no harm to participants. The study also involved no deception or concealment. Participants were pre-screened for normal or corrected-to-normal vision and no accessibility challenges. Informed consent was obtained, and partici pants were briefed on the study’s purpose, duration (up to 2 hours), and potential discomforts (visual strain from pro longed tasks). Participation was voluntary, with the right to withdraw at any time. After the study, participants received a thank-you gift (unrelated to performance), access to study results, and optional public acknowledgment.\r

  • Deterrence: Currently, our prototype is relatively costlier and slower than human-driven CAPTCHA farms. We do not intend to perfect the design, but rather demonstrate its potential destruction when fully weaponized."
Framework Used:
  - Custom
Indirect Stakeholders:
  - Adversaries
key_quotes: ""
Menlo.Beneficience: true
Menlo.Justice: true
Menlo.RespectForLawAndPublicInterest: true
Menlo.RespectForPersons: true
notes: Covers mitigation methods in Discussions. The ethics section is comprehensive, a question does arise regarding whether CAPTCHA vendors should be made alert of the research prior to the field study, even though the authors have covered take steps to ensure data privacy of the sites.
pages: 3747--3766
Research Domain:
  - Large Language Models (LLM)
Research_Type:
  - System
  - Vuln Research
  - Human Subjects
  - Theory
Risk Benefit Analysis: true
Status: Data coded
Subdomain:
  - LLM Security
title: Are CAPTCHAs Still Bot-hard? Generalized Visual {CAPTCHA} Solving with Agentic Vision Language Model
url: https://www.usenix.org/conference/usenixsecurity25/presentation/teoh
Usenix.DataPrivacy: false
Usenix.HarmMitigation: true
Usenix.HumanSubjects: true
Usenix.LiveTesting: true
Usenix.ResearcherSafety: false
Usenix.StakeholderImpact: true
Usenix.ToSViolation: false
Usenix.VulnDisclosure: true
coded_date: 2026-11-02
kanban_order: V2
---
