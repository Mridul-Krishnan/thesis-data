---
Alternatives Considered: false
author: Gilad Moav and Yehuda Afek and Anat Bremler{-}Barr and Amit Klein
author_tags:
  - Gilad Moav
  - Yehuda Afek
  - Anat Bremler{-}Barr
  - Amit Klein
base: "[[Databook.base]]"
DBLP Ref: DBLP:conf/uss/MoavAB025
Direct Stakeholders: []
Emerging Themes: []
Ethics Depth:
Ethics Location: []
Ethics section: This research investigates DNS cache vulnerabilities to enhance security and privacy awareness. While the study includes controlled experiments against live websites, the techniques used do not harm or disrupt the regular operation of the websites or DNS infrastructure being tested. All the experiments and the PoC, were conducted in a controlled laboratory environment, with dedicated computers and forwarders. Additionally, all participants were fully aware about the nature and purpose of the PoC during its execution. We initiated a responsible disclosure procedure for the "Port 0" technique with Google (Chromium), Opera, and Apple (Safari). Additionally, we shared our findings and potential fixes with dnsmasq, and systemd. As a result, Chromium has blocked port 0. Apple has assigned CVE-2025-43227 to this issue, and stated that it will be addressed in an upcoming security update available to all users. Dnsmasq has not implemented any new mitigation (they noted that the cache size limit is already configurable and can be increased “where appropriate”). Opera responded that they updated their base software to Chromium 135, which includes the patch implemented by the Chromium team. We disclosed the issues to systemd, and they notified us that they plan to open a ticket in their public issue management system for future improvements once the embargo is lifted.
Framework Used: []
Indirect Stakeholders: []
kanban_order: 1
key_quotes: ""
Menlo.Beneficience: false
Menlo.Justice: false
Menlo.RespectForLawAndPublicInterest: false
Menlo.RespectForPersons: false
notes: ""
pages: 3557--3576
Research Domain:
  - Network Security & Infrastructure
Research_Type: []
Risk Benefit Analysis: false
Status: Ethics Section Extracted
Subdomain:
  - Network Security
  - Routing and DoS
title: "{DNS} FLaRE: {A} Flush-Reload Attack on {DNS} Forwarders"
url: https://www.usenix.org/conference/usenixsecurity25/presentation/moav
Usenix.DataPrivacy: false
Usenix.HarmMitigation: false
Usenix.HumanSubjects: false
Usenix.LiveTesting: false
Usenix.ResearcherSafety: false
Usenix.StakeholderImpact: false
Usenix.ToSViolation: false
Usenix.VulnDisclosure: false
coded_date: 2026-08-26
---
