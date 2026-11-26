---
Alternatives Considered: false
author: Saiid El Hajj Chehade and Ben Stock and Carmela Troncoso
author_tags:
  - Saiid El Hajj Chehade
  - Ben Stock
  - Carmela Troncoso
base: "[[Databook.base]]"
DBLP Ref: DBLP:conf/uss/ChehadeST25
Direct Stakeholders: []
Emerging Themes: []
Ethics Depth:
Ethics Location: []
Ethics section: We acknowledge the importance of the ethical implications of conducting research, as reinforced by USENIX. Our work includes diverse experiments and data sources that we ensure are ethically valid. We detail the ethical considerations regarding our experiments in the following. User data sources. we scrape publicly accessible GitHub forums for open-source (GPL-3) ad-blockers. Scraping GitHub forums is standard practice in the privacy and security community [26, 58], and only processes publicly accessible resources. To ensure that public information about the forum authors cannot be used to harm users with our proposed attacks, we do not store any author’s personal information in our pipeline and randomize the identifiers while ensuring that the identifiers for posts by the same user are the same. In addition, ad-blocker maintainers employ proprietary methods that reduce personal information in posts, such as moderation and submissions through bot intermediaries. Proposed attacks. The attacks we propose do not rely on specific browser or ad-blocker vulnerabilities that were previously undetected. Instead, we present simple techniques to utilize CSS to demonstrate the inherent susceptibility of ad blockers to detection. We provide attacks similar to prior stylistic attacks previously known to the community, some of which are already implemented [1]. As other fingerprinting works, we provide these attacks as examples to raise awareness for the larger security and privacy community and ad-blocker users about the privacy cost of over-configuring ad blockers. As part of our ethical duty, we explore ways to detect these attacks, try to mitigate them and provide recommendations for appropriate protection against their potential risk. We also provide our pipeline to identify problematic filter rules and eliminate them. Overall, we believe the awareness benefit of disclosing this risk to the community outweighs the potential attack implementation – especially to ad-blocker maintainers and users. This is consistent with the tracking literature, which states that simply describing browser fingerprinting channels does not require a private disclosure to immediate stakeholders. Web measurements. We adopt the same precautions as the large body of web measurement studies. We visit 22K web pages at most thrice in sequence, giving ample delay (30 seconds) between consecutive visits. We only visit publicly accessible pages, which do not require any prior consent from the servers. We use only 10 parallel crawlers to constrain the additional internet traffic volume. Also, we only load the pages passively by loading the page and any associated resources for about 10 seconds. Our crawlers do not interact with the web server in any other way. All additional operations happen on the front end in our browser instances without impacting the services. Finally, the data we generate from the pages is purely functional, including timing information and HTML element counting. Overall, we believe our crawling techniques do not harm servers, ad blockers, or other users.
Framework Used: []
Indirect Stakeholders: []
kanban_order: 20
key_quotes: ""
Menlo.Beneficience: false
Menlo.Justice: false
Menlo.RespectForLawAndPublicInterest: false
Menlo.RespectForPersons: false
notes: ""
pages: 6659--6678
Research Domain:
  - System Security & Threat Detection
Research_Type: []
Risk Benefit Analysis: false
Status: Ethics Section Extracted
Subdomain:
  - Privacy
  - Attacks
title: "Double-Edged Shield: On the Fingerprintability of Customized Ad Blockers"
url: https://www.usenix.org/conference/usenixsecurity25/presentation/el-hajj-chehade
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
