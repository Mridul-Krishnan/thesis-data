---
Alternatives Considered: false
author: Johnny So and Iskander S{\'{a}}nchez{-}Rola and Nick Nikiforakis
author_tags:
  - Johnny So
  - Iskander S{\'{a}}nchez{-}Rola
  - Nick Nikiforakis
base: "[[Databook.base]]"
DBLP Ref: DBLP:conf/uss/SoSN25
Direct Stakeholders: []
Emerging Themes: []
Ethics Depth:
Ethics Location:
Ethics section: "Our work conducted a large-scale analysis of the dependencies of apps by downloading them and dynamically exploring them with a UI-guided test input generator. As such, all interactions with apps follow a generic behavior that does not attempt targeted execution flows for specific apps, nor generate highly-realistic, human-like interactions with backend services. We did not attempt to bypass any login or splash screens of apps, and our infrastructure interacted with each APK for a total of nine minutes. Thus, we are confident that our dynamic analysis of apps did not negatively impact the contacted backend services. We did not register any expired domains and therefore never interacted with potential users of the affected APKs (we manipulated our testing environment for the investigations presented in Section 4.5).Disclosure of our findings was complicated by the fact that we finished our analyses more than six months after the initial data collection, and that there is no immediately obvious purpose in contacting app developers about outdated versions of their software having been susceptible to the use of expired domains in the past (particularly for the analyses with passive DNS). We instead opted to contact the developers of the apps affected by the 41 registrable domains we found at runtime.Only one affected app developer replied: most of our disclosures were redirected to automated support ticket customer support systems, and these tickets were automatically closed with no response. The one contact that responded asked for more information to relay to the relevant app developers, but never followed up."
Framework Used: []
Indirect Stakeholders: []
key_quotes: ""
Menlo.Beneficience: false
Menlo.Justice: false
Menlo.RespectForLawAndPublicInterest: false
Menlo.RespectForPersons: false
notes: ""
pages: 3297--3316
Research Domain:
  - Software Security & Development Lifecycle
Research_Type: []
Risk Benefit Analysis: false
Status: Ethics Section Extracted
Subdomain:
  - Web and Mobile Security
title: "Lost in the Mists of Time: Expirations in {DNS} Footprints of Mobile Apps"
url: https://www.usenix.org/conference/usenixsecurity25/presentation/so
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
