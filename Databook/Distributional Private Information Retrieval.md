---
Alternatives Considered: false
author: Ryan Lehmkuhl and Alexandra Henzinger and Henry Corrigan{-}Gibbs
author_tags:
  - Ryan Lehmkuhl
  - Alexandra Henzinger
  - Henry Corrigan{-}Gibbs
base: "[[Databook.base]]"
DBLP Ref: DBLP:conf/uss/LehmkuhlHC25
Direct Stakeholders: []
Emerging Themes: []
Ethics Depth:
Ethics Location: []
Ethics section: "As technology becomes increasingly ubiquitous in our lives, it is critical to build systems that protect the privacy of personal information—this aligns with both the “Respect for Persons” and “Beneficence” ethical principles laid out in the Menlo Report [25]. In this work we presented new techniques that further this goal by improving the performance of private information retrieval, enabling users to fetch data from service providers without revealing what they are fetching.\r

  However,there are several possible ethical concerns with applying our techniques in practice, particularly surrounding the “Justice” principle of the Menlo Report [25]. Our techniques weaken the correctness guarantees of traditional PIR,but do so more notably for less popular database entries. Consequently, deploying a system like CrowdSurf for private social-media feeds could lead to: (i) less-popular content-creators receiving less attention than they would have otherwise (ii) users with abnormal usage patterns receiving fewer of the posts they’re interested in. Thus, before using our techniques in practice one must consider the balance between the negative impacts experienced by these subsets of users with the privacy benefits that cheaper PIR could provide for all users.\r

  The Twitter dataset we use in our paper is from the work of Gabielkov et al. [30] and anonymizes user identifiers."
Framework Used: []
Indirect Stakeholders: []
key_quotes: ""
Menlo.Beneficience: false
Menlo.Justice: false
Menlo.RespectForLawAndPublicInterest: false
Menlo.RespectForPersons: false
notes: ""
pages: 3377--3396
Research Domain:
  - Cryptography & Formal Verification
Research_Type: []
Risk Benefit Analysis: false
Status: Ethics Section Extracted
Subdomain:
  - Crypto
  - Private Information Retrieval and Computation
title: Distributional Private Information Retrieval
url: https://www.usenix.org/conference/usenixsecurity25/presentation/lehmkuhl
Usenix.DataPrivacy: false
Usenix.HarmMitigation: false
Usenix.HumanSubjects: false
Usenix.LiveTesting: false
Usenix.ResearcherSafety: false
Usenix.StakeholderImpact: false
Usenix.ToSViolation: false
Usenix.VulnDisclosure: false
coded_date: 2026-09-07
---
