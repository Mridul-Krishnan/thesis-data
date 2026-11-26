---
Alternatives Considered: false
author: Jun Ho Huh and Hyejin Shin and Sunwoo Ahn and Hayoon Yi and Joonho Cho and Taewoo Kim and Minchae Lim and Nu{-}El Choi
author_tags:
  - Jun Ho Huh
  - Hyejin Shin
  - Sunwoo Ahn
  - Hayoon Yi
  - Joonho Cho
  - Taewoo Kim
  - Minchae Lim
  - Nu{-}El Choi
base: "[[Databook.base]]"
DBLP Ref: DBLP:conf/uss/HuhSAYCKLC25
Direct Stakeholders: []
Emerging Themes: []
Ethics Depth:
Ethics Location: []
Ethics section: "Although the authors’ affiliation and the organization that shared SMS request log dataset are independent entities, the two are part of the same global corporate umbrella. While confidentially receiving the dataset – i.e., the dataset never left the corporate private and secure network – we inquired and checked with the internal legal and privacy protection office, and received confirmation that the conducted research and the act of publishing statistical results comply with the terms and conditions stated in users’ consent for data collection and use. Specifically, the collection and use of all personally identifiable information (PII), including phone numbers, IMEIs, and IP addresses, are explicitly stated in terms and conditions that users must read and agree upon creating an account. In fact, all log attributes disclosed in Section 4.2 (used to compute features) are explicitly mentioned in the “what information do we collect,” “how do we use your information,” and “how do we keep your information secure” sections. Before conducting the presented research, we contacted internal legal office and privacy protection office, and completed both legal, privacy, and personal data compliance reviews with respect to (1) collecting and storing SMS authentication request logs (including all attributes disclosed in Section 4.2) from the studied authentication service, and (2) analyzing those logs to develop an AIT attack detection system for both web and native channels, and publishing statistical results and findings. All SMS authentication logs were encrypted and made accessible only within the organization’s secure private network – performing two-factor authentication was mandatory to access the data. Access to PIIs were governed with more stringent policies: the authors had to request specific PII access permissions on a daily basis (every 24 hours) to decrypt them. Decrypted PIIs (phone numbers and IMEIs) were merely used for initial AIT attack pattern analyses. Subsequent feature extraction, model training, and evaluation tasks were performed using just the prefix values, and the number of distinct occurrences were counted in the original encrypted form. Benign end users may benefit from this research in two areas: (1) elimination of high-volume peak traffics would ensure more consistent SMS authentication latency and log in experience, and (2) prevention of genuine phone numbers being exploited by attackers, and users constantly having to deal with spam (unknown) SMS texts. There is a risk that publishing feature engineering details and experimental results could provide means for adversaries to re-configure attack settings and perform evasive attacks. Our evasive attack analysis (see Section 6.5), however, revealed that such cost-intensive efforts would still lead to modest attack success rates (51% for web and 9% for native channels) yet significantly increase the overall attack preparation costs. Considering low return on investment, we argue it is somewhat unlikely that attackers would heavily invest in evasive attacks. Even if some attackers do proceed with evasive manipulations, overall attack success rates would be significantly lower than when rate limit policies are used alone (state-of-the-art). Further, the presented feature engineering techniques are designed based on commonly available SMS authentication log attributes – to that end, we believe our features can be adapted quickly to other similar SMS-based authentication services, and facilitate deployment of their own highly effective AIT attack detection systems."
Framework Used: []
Indirect Stakeholders: []
kanban_order: 25
key_quotes: ""
Menlo.Beneficience: false
Menlo.Justice: false
Menlo.RespectForLawAndPublicInterest: false
Menlo.RespectForPersons: false
notes: ""
pages: 5405--5423
Research Domain:
  - Network Security & Infrastructure
Research_Type: []
Risk Benefit Analysis: false
Status: Ethics Section Extracted
Subdomain:
  - Network Security
  - BLE and Cellular
title: Preventing Artificially Inflated {SMS} Attacks through Large-Scale Traffic Inspection
url: https://www.usenix.org/conference/usenixsecurity25/presentation/huh
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
