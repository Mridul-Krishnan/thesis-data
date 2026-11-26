---
Alternatives Considered: false
author: Shuhan Zhang and Shuai Wang and Li Chen and Dan Li and Baojun Liu
author_tags:
  - Shuhan Zhang
  - Shuai Wang
  - Li Chen
  - Dan Li
  - Baojun Liu
base: "[[Databook.base]]"
DBLP Ref: DBLP:conf/uss/Zhang000L25
Direct Stakeholders: []
Emerging Themes: []
Ethics Depth:
Ethics Location: []
Ethics section: "In this work, we strictly follow the ethical principles in the Menlo Report [10] and adhere to the best practices of network measurements [60]. We have also responsibly reported the discovered vulnerabilities to all the affected vendors. Specifically, we discuss the ethical concerns in the following aspects.\r

  \r

  Software testing. Regarding the DNS software testing in Section 5.1, we downloaded the latest available version of each software from the vendor’s official website and performed tests in controlled environments. Specifically, for open-source software, we installed and compiled them in docker containers. For closed-source software, e.g., Microsoft DNS, we ran them on local virtual machines under our control. Internet measurement. First, we registered our own apex zones as the victims and delegated them to nameserver hosts controlled by ourselves. To identify vulnerabilities in the wild, we positioned the simulated on-path attacker at our controlled nameserver hosts, which did not affect the real-world DNS components. Second, we sent DNS queries from our controlled cloud servers and adhered to the term of use of the cloud service provider [27]. We configured PTR records for the IP addresses of the cloud servers, which pointed to a website indicating the purpose of our research and our contacts for opt-out operations. So far, we have not received any complaints about our measurement campaign. Third, we carefully limited the DNS query rate to the target resolvers to be less than 10 QPS and restricted the overall measurement duration to 30 hours, so as to avoid overloading their normal services. Fourth, we bounded the TTL of the injected forged records to 86,400 seconds (i.e., 1 day), in order to prevent any abuse of the records staying in the resolver cache. Fifth, in terms of the measurement towards DNSSEC-signed zones, we collected real-world DNS zones from publicly available datasets [61, 69] or under the grant of ICANN CZDS [39].\r

  \r

  Vulnerability disclosure. We have proposed several suggestions to mitigate the risk of the RUC attack, and have responsibly disclosed the vulnerabilities to all the affected DNS vendors in December, 2024, leaving sufficient time for them to develop patches before the paper publication. For vulnerable vendors without any feedback, we retried to inform them of the vulnerability in a best-effort manner, i.e., resending the report on a monthly basis."
Framework Used: []
Indirect Stakeholders: []
kanban_order: 32
key_quotes: ""
Menlo.Beneficience: false
Menlo.Justice: false
Menlo.RespectForLawAndPublicInterest: false
Menlo.RespectForPersons: false
notes: ""
pages: 3517--3535
Research Domain:
  - Network Security & Infrastructure
Research_Type: []
Risk Benefit Analysis: false
Status: Ethics Section Extracted
Subdomain:
  - Network Security
  - Routing and DoS
title: "Your Shield is My Sword: {A} Persistent Denial-of-Service Attack via the Reuse of Unvalidated Caches in {DNSSEC} Validation"
url: https://www.usenix.org/conference/usenixsecurity25/presentation/zhang-shuhan
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
