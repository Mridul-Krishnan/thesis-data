---
Alternatives Considered: false
author: Malte Wessels and Simon Koch and Jan Drescher and Louis Bettels and David Klein and Martin Johns
author_tags:
  - Malte Wessels
  - Simon Koch
  - Jan Drescher
  - Louis Bettels
  - David Klein
  - Martin Johns
base: "[[Databook.base]]"
DBLP Ref: DBLP:conf/uss/Wessels0DB0J25
Direct Stakeholders: []
Emerging Themes: []
Ethics Depth:
Ethics Location: []
Ethics section: We did not deploy HyTrack into any app store. We have not tested it on third parties. After concluding this work, we will delete all raw traffic collections to remove any user-generated content requested by the apps. We disclosed HyTrack to Google via the Android Vulnerability Reward Program. Furthermore, we are in contact with the affected upstream browser vendors, disclosing our findings to the engine developers of the browsers tested browsers with Custom Tabs or Trusted Web Activities support. As of 2025-01 the Chromium team considers this issue a won’t-fix, while the Firefox team discussed potential mitigations. Additionally, we contacted the vendors of downstream privacy browsers. However, as detailed earlier, resolving this privacy threat is far from trivial and likely requires fundamental changes to the core Custom Tab functionality. Therefore, weighing the harms of publishing this work against the benefits is detrimental. As harm, we identified the risk to user privacy that tracking providers and malicious actors could use our findings about HyTrack to deploy it themselves. However, by publishing this work, we contribute to user knowledge. HyTrack is a risk users must be aware of to make informed choices about their browsing and mobile usage behavior. Only by knowing about it, users can act accordingly, e.g., by disabling features or switching to a browser with ad-blocking capabilities to use privacy-focused blocking lists. Additionally, publishing this work puts pressure on the browser vendors to reconsider their implementations and provide safer defaults. We only describe this issue while browser vendors ship features that can compromise users’ privacy. Additionally, we assume that other researchers and tracking companies will encounter this behavior. Even though we could not identify HyTrack instances in the wild, we can not be sure that tracking vendors and malicious actors are unaware of it or using it on people or apps outside our dataset. I.e., HyTrack might already be in use, putting users at risk. Therefore, we would harm user privacy by not publishing this work, as they could or might be already impacted by HyTrack in the future without their knowledge. We consider the harm from publishing this work sufficiently reduced by the benefits of making users aware of the risk and allowing them to act accordingly, putting pressure on vendors to fix the issue systematically, and informing users that might already be impacted by HyTrack without their knowledge. We urge all researchers working on similar issues to weigh the harms and benefits of their work as well before publishing it. Similarly, we want to encourage vendors to consider privacy implications early in the design of new (browser) features; privacy must be by design and considered early
Framework Used: []
Indirect Stakeholders: []
kanban_order: 27
key_quotes: ""
Menlo.Beneficience: false
Menlo.Justice: false
Menlo.RespectForLawAndPublicInterest: false
Menlo.RespectForPersons: false
notes: ""
pages: 6521--6539
Research Domain:
  - System Security & Threat Detection
Research_Type: []
Risk Benefit Analysis: false
Status: Ethics Section Extracted
Subdomain:
  - Privacy
  - Attacks
title: "HyTrack: Resurrectable and Persistent Tracking Across Android Apps and the Web"
url: https://www.usenix.org/conference/usenixsecurity25/presentation/wessels
Usenix.DataPrivacy: false
Usenix.HarmMitigation: false
Usenix.HumanSubjects: false
Usenix.LiveTesting: false
Usenix.ResearcherSafety: false
Usenix.StakeholderImpact: false
Usenix.ToSViolation: false
Usenix.VulnDisclosure: false
coded_date: 2026-08-27
---
