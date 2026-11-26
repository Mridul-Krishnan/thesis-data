---
Alternatives Considered: false
author: Mingming Zhang and Yunyi Zhang and Baojun Liu and Haixin Duan and Min Zhang and Fan Shi and Chengxi Xu
author_tags:
  - Mingming Zhang
  - Yunyi Zhang
  - Baojun Liu
  - Haixin Duan
  - Min Zhang
  - Fan Shi
  - Chengxi Xu
base: "[[Databook.base]]"
DBLP Ref: DBLP:conf/uss/ZhangZLD00X25
Direct Stakeholders: []
Emerging Themes: []
Ethics Depth:
Ethics Location: []
Ethics section: Our analysis involves using public datasets and querying domain nameservers, with careful consideration of ethical issues in the experimental design. We adhere to ethical standards based on the Menlo Report [35], best practices for network measurement [46], and recommendations for using public dataset [17]. First, we collected data from publicly accessible TLD zone files, which include domain delegation information commonly used in DNS research [16, 33, 54], without registrant information. All data was stored securely on internal servers with no unauthorized access. Second, for historical WHOIS data, we focused on registration dates and status fields, excluding registrant information to ensure anonymity and privacy. Third, we adhered to vendor-imposed rate limits when accessing registrar interfaces to determine domain status and avoid straining their systems. Forth, during active DNS probes, such as querying NS records, we strictly limit the scan rate to minimize the impact on public DNS resolvers and nameservers.
Framework Used: []
Indirect Stakeholders: []
kanban_order: 23
key_quotes: ""
Menlo.Beneficience: false
Menlo.Justice: false
Menlo.RespectForLawAndPublicInterest: false
Menlo.RespectForPersons: false
notes: ""
pages: 7117--7134
Research Domain:
  - Network Security & Infrastructure
Research_Type: []
Risk Benefit Analysis: false
Status: Ethics Section Extracted
Subdomain:
  - Network Security
  - Internet and Beyond
title: "Misty Registry: An Empirical Study of Flawed Domain Registry Operation"
url: https://www.usenix.org/conference/usenixsecurity25/presentation/zhang-mingming
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
