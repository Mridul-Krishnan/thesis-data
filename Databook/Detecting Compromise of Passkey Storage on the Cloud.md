---
Alternatives Considered: false
author: Mazharul Islam and Sunpreet S. Arora and Rahul Chatterjee and Ke Coby Wang
author_tags:
  - Mazharul Islam
  - Sunpreet S. Arora
  - Rahul Chatterjee
  - Ke Coby Wang
base: "[[Databook.base]]"
coded_date: 2026-02-18T14:46:00
DBLP Ref: DBLP:conf/uss/0002A0W25
Direct Stakeholders:
  - System Operators
Emerging Themes:
  - Usability Analysis
Ethics Depth: Minimal
Ethics Location:
  - Main Body
Ethics section: Ethics considerations. Our work aims to improve account security by detecting the abuse of passkeys leaked from the cloud storage of passkey management services or providers. Thus we believe our work does not pose any potential harm to users or raise any ethical concerns.
Framework Used:
  - None Explicit
Indirect Stakeholders:
  - End Users
key_quotes: "CASPER1, which, to the best of our knowledge, is the first framework to detect the abuse of passkeys leaked from PMS. Underlying CASPER is a decoy-based detection technique [30,50,75]: it hides the real passkey within a list of decoy passkeys that are indistinguishable from the real one. As a result, an attacker who steals the passkeys from PMS and attempts to use them to log into the user’s account at a relying party (RP), e.g., a website, inadvertently will end up using a decoy passkey with high probability. These login attempts will trigger breach detection at the RP, indicating the abuse of passkeys stolen from the PMS."
Menlo.Beneficience: true
Menlo.Justice: true
Menlo.RespectForLawAndPublicInterest: false
Menlo.RespectForPersons: true
notes: While the Ethics section is very minimal, Section 8 Discussion, goes in depth in analysing the usage of the tool CASPER in a user, system operator (in this case RE or Relying Entity) as well as attacker perspective. It appears that it is important to give emphasis to all stakeholders and the impacts in order to engage and encourage  the tool’s usability and beneficence.  Attack on the tool itself (figuring out the user secret) only results in the fallback to the previous existing system.
pages: 7743--7762
Research Domain:
  - System Security & Threat Detection
Research_Type:
  - System
  - Theory
Risk Benefit Analysis: true
Status: Data coded
Subdomain:
  - Authentication
title: Detecting Compromise of Passkey Storage on the Cloud
url: https://www.usenix.org/conference/usenixsecurity25/presentation/islam
Usenix.DataPrivacy: false
Usenix.HarmMitigation: false
Usenix.HumanSubjects: false
Usenix.LiveTesting: false
Usenix.ResearcherSafety: false
Usenix.StakeholderImpact: true
Usenix.ToSViolation: false
Usenix.VulnDisclosure: false
---
