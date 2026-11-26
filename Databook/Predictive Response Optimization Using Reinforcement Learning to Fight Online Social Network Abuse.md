---
Alternatives Considered: false
author: Garrett Wilson and Geoffrey Goh and Yan Jiang and Ajay Gupta and Jiaxuan Wang and David Freeman and Francesco Dinuzzo
author_tags:
  - Garrett Wilson
  - Geoffrey Goh
  - Yan Jiang
  - Ajay Gupta
  - Jiaxuan Wang
  - David Freeman
  - Francesco Dinuzzo
base: "[[Databook.base]]"
DBLP Ref: DBLP:conf/uss/WilsonGJGWFD25
Direct Stakeholders: []
Emerging Themes: []
Ethics Depth:
Ethics Location: []
Ethics section: "We have assessed the value of publishing this work against po\r

  tentially adverse consequences due to its methodology and/or\r

  data practices. Specifically, we considered risks related to\r

  user harm, equitable selection, user consent, and user data\r

  handling [71].\r

  User harm. We acknowledge that fighting abuse on online\r

  social networks is a task fraught with risk: some users are\r

  harmed by the abuse itself, while others are harmed by over\r

  enforcement when defenses become too aggressive. This\r

  entire work is devoted to systematically balancing reduction\r

  in both of these harms. Our system’s “explore-exploit” strat\r

  egy aims to reduce harm over the entire platform while taking\r

  into account that not all local decisions can be perfect. How\r

  ever, our experiments demonstrate that the PRO system offers\r

  significant benefit to users in terms of overall harm reduction.\r

  We also considered the risk of our experiments over\r

  enforcing on benign users due to system and/or model de\r

  ficiencies. To mitigate this risk we set up our experiments\r

  to include only users that our binary classifiers predicted to\r

  be abusive with high confidence. The precision of the binary\r

  classifiers was confirmed to be greater than 90% at the time of\r

  the experiments. Given the above considerations, we believe\r

  that our experiment exposes users to risks that are “reasonable\r

  in relation to anticipated benefits” [71].\r

  Equitable selection. Our subjects are necessarily chosen\r

  equitably since a user’s participation in the experiment is\r

  determined by a random number generator whose output is\r

  independent of any user properties.\r

  User consent. Partridge and Allman [60] observe that “direct\r

  consent is not possible in most Internet measurements,” and\r

  our study is a good example. Since we cannot predict in\r

  advance who our classifiers will determine to be abusive, we\r

  would have to obtain consent either from the entire OSN\r

  population or from the specific users acted on by PRO at the\r

  moment action is taken. Building a bespoke consent flow for\r

  this study would be a large engineering task and would risk\r

  both information bias (users might act differently knowing\r

  they were in a security study) and selection bias (both benign\r

  and abusive users who choose to participate in a security study\r

  may not reflect the general population). Either type of bias\r

  could render our statistical analyses invalid and thus handicap\r

  our ability to measurably improve abuse detection.\r

  Partridge and Allman suggest that “proxy consent” is the\r

  de facto standard in large-scale internet measurement studies,\r

  giving the example of “network measurements taken on a\r

  university campus typically seek consent from the university.”\r

  In our case institutional consent was rendered via the OSNs’\r

  agreements to let us conduct and publish this research. In\r

  particular, the reviewers approving the research noted that\r

  all users in our study have accepted the terms of service of\r

  Instagram or Facebook (as applicable), which address use of\r

  data in the context of investigating suspicious activity and ad\r

  dressing policy violations. The reviewers therefore concluded\r

  that the OSN terms of service provide users a sufficient level\r

  of transparency.\r

  We note that explicit consideration of user consent is not\r

  historically an element of large-scale internet security studies.\r

  Bilogrevic et al. [13] use a proxy approach similar to ours,\r

  deriving their user consent from the fact that users opted in to\r

  a setting to “Make searches and browsing better.” However,\r

  recent work studying millions of users on Reddit [44], Face\r

  book [25,58], and Google Chrome [69] do not address user\r

  consent at all in their ethics discussions. We discuss open\r

  questions in this area in Section 7.\r

  Data handling. Before developing and testing our system, we\r

  assessed how data would be used and protected and ensured\r

  that technical systems and/or manual processes were in place\r

  to mitigate any identified risks prior to the launching the\r

  experiment [54]. For this project, we mitigated risks by:\r

  \r

  • Limiting data collection to a set of user features identi\r

  fied as being relevant for abuse detection;\r

  \r

  • Specifically excluding any sensitive data from collection;\r

  \r

  • Restricting access to both collected and inferred data;\r

  \r

  • Deleting all user-identifying data within 90 days of col\r

  lection;\r

  \r

  • Using technical safeguards to ensure that the data are\r

  only used for safety, integrity, and security use cases."
Framework Used: []
Indirect Stakeholders: []
key_quotes: ""
Menlo.Beneficience: false
Menlo.Justice: false
Menlo.RespectForLawAndPublicInterest: false
Menlo.RespectForPersons: false
notes: ""
pages: 3239--3256
Research Domain:
  - Software Security & Development Lifecycle
Research_Type: []
Risk Benefit Analysis: false
Status: Ethics Section Extracted
Subdomain:
  - Web and Mobile Security
title: "Predictive Response Optimization: Using Reinforcement Learning to Fight Online Social Network Abuse"
url: https://www.usenix.org/conference/usenixsecurity25/presentation/wilson
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
