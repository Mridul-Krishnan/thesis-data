---
Alternatives Considered: false
author: Florian Hantke and Peter Snyder and Hamed Haddadi and Ben Stock
author_tags:
  - Florian Hantke
  - Peter Snyder
  - Hamed Haddadi
  - Ben Stock
base: "[[Databook.base]]"
DBLP Ref: DBLP:conf/uss/HantkeSHS25
Direct Stakeholders: []
Emerging Themes: []
Ethics Depth:
Ethics Location: []
Ethics section: "As USENIX Security rightfully states, ethics plays a critical role in conducting research. Therefore, we carefully considered our project’s ethical implications before we started our research. In our study, we sent GET requests to the 10k most popular origins according to the CrUX list [53]. This is a research practice employed by numerous Web studies before and is generally considered ethical in the security and privacy community. However, it is essential to acknowledge that ethi cal standards can evolve, and each project should be assessed on a case-by-case basis.\r

  In this study, we requested each origin of the top 10k only once per experiment with a standard GET request. Since a GET request is designed to receive data without making any modifications, we assume no negative impact for the end user.\r

  We also ensure no negative impact for the website operators as our minimal interaction does not contribute significantly to the common internet traffic or pose any more risk than typical internet background noise. While we, however, might potentially violate some websites’ terms of service, as we did not verify whether automated site visits were explicitly allowed, we believe that the benefits to the research community in the form of our measurements and the demonstration of WebREC outweigh this concern. All our additional measurements are performed on our client side, i.e., our server, not influencing any third-party server. In conclusion, we are confident that our work did not cause harm to any individual or organization.\r

  Our research and measurements aim to contribute benefit to our research community by providing and influencing new ways how to conduct future Web measurement studies."
Framework Used: []
Indirect Stakeholders: []
key_quotes: ""
Menlo.Beneficience: false
Menlo.Justice: false
Menlo.RespectForLawAndPublicInterest: false
Menlo.RespectForPersons: false
notes: ""
pages: 8235--8253
Research Domain:
  - Software Security & Development Lifecycle
Research_Type: []
Risk Benefit Analysis: false
Status: Ethics Section Extracted
Subdomain:
  - Web Security
title: "Web Execution Bundles: Reproducible, Accurate, and Archivable Web Measurements"
url: https://www.usenix.org/conference/usenixsecurity25/presentation/hantke
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
