---
Alternatives Considered: false
author: Mark Russinovich and Ahmed Salem and Ronen Eldan
author_tags:
  - Mark Russinovich
  - Ahmed Salem
  - Ronen Eldan
base: "[[Databook.base]]"
DBLP Ref: DBLP:conf/uss/Russinovich0E25
Direct Stakeholders:
  - Software Maintainers
Emerging Themes:
  - Mitigation
  - Trolley Problem
Ethics Depth:
  - Detailed
Ethics Location:
  - Main Body
Ethics section: "Responsible Disclosure and Mitigation Efforts. First and foremost, we adhered to the coordinated vulnerability disclo sure protocol by reporting Crescendo to all impacted organizations, including OpenAI, Microsoft, Meta, Google, and Anthropic, prior to submitting our work. We believe this scenario aligns with the D1 scenario in [18], where vulnerabilities are reported to the companies and not published for three months to allow adequate time for developing mitigations. We confirmed receipt of our communications and, in some cases, reached out to multiple individuals within these companies to ensure our message was delivered. Alongside our reports, we provided comprehensive manual examples of Crescendo and the Crescendomation automation tool, and offered our assistance to help mitigate the identified issues. During this three-month period, we received no complaints or requests for a delay from any of the companies. Additionally, one organization collaborated with us to enhance their filters based on the gaps identified by Crescendo.\r

  Why We Are Publishing Crescendo (An Attack). Our primary goal in publishing this research is to highlight potential vulnerabilities in future public systems or large language models (LLMs) in general, thereby contributing to the development of more secure models. Current mitigations have predominantly focused on single-turn jailbreak techniques, of ten overlooking simpler methods that can be easily exploited by users. By introducing Crescendo and providing an automation tool, we aim to assist in evaluating the latest state-of the-art models, identifying quick fixes for revealed gaps, and improving alignment in future iterations of these models.\r

  Team Member Support. We are committed to the well-being of our team members who may interact with, view, assess, or handle harmful content. In addition to general mental health services, we offered a specialized mental health program that collaborates with best-in-class providers, including psychologists, counselors, and cybersecurity and intelligence experts.\r

  These providers have experience in supporting individuals exposed to harmful content in similar fields, ensuring that our team members receive the care and support they need."
Framework Used:
  - Custom
Indirect Stakeholders:
  - Private Institutions
key_quotes: ""
Menlo.Beneficience: true
Menlo.Justice: false
Menlo.RespectForLawAndPublicInterest: true
Menlo.RespectForPersons: false
notes: ""
pages: 2421--2440
Research Domain:
  - Large Language Models (LLM)
Research_Type:
  - System
  - Vuln Research
Risk Benefit Analysis: true
Status: Data coded
Subdomain:
  - LLM Security
  - Jailbreaking and Prompt Stealing
title: "Great, Now Write an Article About That: The Crescendo Multi-Turn {LLM} Jailbreak Attack"
url: https://www.usenix.org/conference/usenixsecurity25/presentation/russinovich
Usenix.DataPrivacy: false
Usenix.HarmMitigation: true
Usenix.HumanSubjects: false
Usenix.LiveTesting: false
Usenix.ResearcherSafety: true
Usenix.StakeholderImpact: true
Usenix.ToSViolation: false
Usenix.VulnDisclosure: true
coded_date: 2026-11-04
kanban_order: Uw
---
