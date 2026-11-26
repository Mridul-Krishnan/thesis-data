---
Alternatives Considered: false
author: Marcell Szak{\'{a}}ly and Sebastian K{\"{o}}hler and Ivan Martinovic
author_tags:
  - Marcell Szak{\'{a}}ly
  - Sebastian K{\"{o}}hler
  - Ivan Martinovic
base: "[[Databook.base]]"
DBLP Ref: DBLP:conf/uss/Szakaly0M25
Direct Stakeholders:
  - System Operators
Emerging Themes: []
Ethics Depth:
  - Detailed
Ethics Location:
  - Main Body
Ethics section: "For both practical and ethical reasons, we modeled our research after commonly conducted Internet-wide scans. As such, our experiments perform non-malicious CCS charging sessions and collect data in the process. All tested chargers were installed for public use and are part of critical infrastructure, so we did not want to risk damaging them, or compromising any user data. We analyze the ethics of our work from the below angles: Data Privacy: All of our data was collected using our EV emulator and public chargers. We did not collect data on the charging sessions of real users charging their car, and there was no foreseeable way in which data from a previous charging session could be leaked to us. Since the tested devices were provided and owned by companies, none of the information we collected about them could be classified as personal information.\r

  Infrastructure Damage: Our experiments mostly followed standard-compliant behavior, but deviated in minor non-malicious ways, such as by attempting a connection with a TLS 1.1 client instead of the required 1.2. Therefore, any CCS implementation should handle our experiments gracefully and we are confident that we caused no damage to tested devices.\r

  Public Safety: We believe that documenting the current state of security in EV charging is important and necessary.\r

  Our results will inform researchers, companies and legislators, allowing them to push for changes in the industry that will benefit everyone. In cases where implementations used older, less secure versions of CCS, we treated this as a design choice by manufacturers, which does not require disclosure.\r

  However, in cases where we discovered actual flaws in the implementation, we disclosed them to the affected parties.\r

  Data Availability: In the paper, we discuss the statistics seen in our dataset, and the companies that implemented TLS.\r

  The dataset is made publicly available consisting of a list of each specific charger we tested, including location, serial numbers, time of test, and key findings. During our evaluation we found certain issues and potential vulnerabilities which are discussed anonymously. Our raw data files contain information about these, as well as more sensitive data such as TLS certificates. Therefore, this detailed data is only made available upon request"
Framework Used:
  - Custom
Indirect Stakeholders:
  - Broader Public
  - Adversaries
key_quotes: ""
Menlo.Beneficience: true
Menlo.Justice: true
Menlo.RespectForLawAndPublicInterest: true
Menlo.RespectForPersons: true
notes: ""
pages: 7997--8015
Research Domain:
  - Cryptography & Formal Verification
Research_Type:
  - Vuln Research
  - Measurement
Risk Benefit Analysis: true
Status: Data coded
Subdomain:
  - System Security
  - Securing Systems and Protocols
title: "Current Affairs: {A} Security Measurement Study of {CCS} {EV} Charging Deployments"
url: https://www.usenix.org/conference/usenixsecurity25/presentation/szakaly
Usenix.DataPrivacy: true
Usenix.HarmMitigation: true
Usenix.HumanSubjects: false
Usenix.LiveTesting: false
Usenix.ResearcherSafety: false
Usenix.StakeholderImpact: true
Usenix.ToSViolation: false
Usenix.VulnDisclosure: true
coded_date: 2026-11-02
kanban_order: V3
---
