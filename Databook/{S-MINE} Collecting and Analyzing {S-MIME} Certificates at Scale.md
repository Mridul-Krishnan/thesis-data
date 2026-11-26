---
Alternatives Considered: false
author: Gurur {\"{O}}ndar{\"{o}} and Jonas Kaspereit and Samson Umezulike and Christoph Saatjohann and Fabian Ising and Sebastian Schinzel
author_tags:
  - Gurur {\"{O}}ndar{\"{o}}
  - Jonas Kaspereit
  - Samson Umezulike
  - Christoph Saatjohann
  - Fabian Ising
  - Sebastian Schinzel
base: "[[Databook.base]]"
DBLP Ref: DBLP:conf/uss/OndaroKUSIS25
Direct Stakeholders: []
Emerging Themes: []
Ethics Depth:
Ethics Location: []
Ethics section: "Scanning and Crawling In our Internet-wide scans for LDAP servers, we followed standard best practices, as out lined by Durumeric et al. [20]. We sent only standard conforming TCP and LDAP packets, used rate limiting, and randomized the order of destination addresses to reduce strain on the network and servers. On the scanning IPs, a website gives project details and contact information for opt-out re quests. We honored all such requests. Our ISP, national CERT, and institutional network administrator cleared all scans.\r

  We applied a 60-second delay to all our LDAP reconnects to reduce the server load during our crawling process.\r

  We monitored the crawling process of servers and manually stopped long-running crawls that did not result in certificate collections to avoid straining servers.\r

  Scraping of Identifiable Private Information The data we collected from public LDAP servers was restricted to the minimum required for our research, i.e., X.509 certificates and distinguished names of entries. Since this data is stored on Internet-accessible servers, we assume that, in most cases, this data was published willingly and with the consent of the certificate owners. This is supported by the idea that certificates are often published to allow new communication partners to communicate with the owners privately. Multiple large organizations publicly and intentionally document access to these public LDAP servers on their website [1,16,55].\r

  However, even though this data is publicly available, not all users might be aware of this or might object to their data being used for research. We believe this data collection to be comparable to the scraping of social media profiles, even though we collect significantly fewer data about certificate owners, for which currently no clear ethical guidelines seem to exist [33]. We believe our research will not cause significant harm to certificate owners and benefit those with vulnerable certificates, but acknowledge that the leakage of the dataset with associated analysis results might have led to harm, which is why we took measures to reduce this risk (see below).\r

  We urge researchers undertaking similar projects to evaluate what data they need to collect and store, and, if possible, involve an Institutional Review Board (IRB) in the study design. Consequently, we have decided not to publish our certificate dataset to protect certificate owners’ privacy.\r

  Data Protection We designed our LDAP queries to retrieve only the S/MIME certificates and the distinguished name of entries, ensuring that no additional data is transmitted over the network. We maximized the protection of the transmitted data by prioritizing secure TLS connections and using plaintext transmission only as a fallback for the certificate crawling.\r

  All collected certificates and the associated analyses were stored and conducted exclusively on internal servers at our institution, which are accessible only to the research team.\r

  Furthermore, in analyses involving external APIs, no full certificates or personal data were transmitted, safeguarding the privacy of the information. We will delete all data when our studies have concluded.\r

  Coordinated Disclosure We classified our certificate related findings according to conditions that (a) are curious but technically not security-relevant and (b) are security-related vulnerabilities.\r

  The latter (b) classification includes non-expired S/MIME certificates with cryptographic vulnerabilities, as presented in Section 7. These certificates may still be used for applications where the security of the private key is crucial. We contacted a national CERT for assistance in disclosing this to the CAs, but after some discussion, they advised us to perform the disclosure directly. For this, we first tried identifying contact addresses for the CAs but found that they did not provide an email address in their certificates. Instead, in April 2025, we disclosed the issues to the corresponding operators of the LDAP servers where the certificates were stored, assuming they could contact their users or the CA. In June 2025, we per formed a second disclosure regarding additional certificates with cryptographic vulnerabilities obtained and identified dur ing follow-up certificate crawls. As of June 2025, no server operator has reacted to our disclosures.\r

  The findings belonging to (a) are not security relevant, e.g., expired historical certificates, and cannot be used in standard conforming applications. Nevertheless, we will inform the CAs about our research as soon as our paper is published.\r

  We have also disclosed the Outlook issue described in Section 5 to Microsoft. Microsoft has acknowledged the report but said that they do not consider this a vulnerability due to the common and legitimate usage of non-email certificates and the complexity of exploiting this in practice, rating the risk as very low."
Framework Used: []
Indirect Stakeholders: []
key_quotes: ""
Menlo.Beneficience: false
Menlo.Justice: false
Menlo.RespectForLawAndPublicInterest: false
Menlo.RespectForPersons: false
notes: ""
pages: 6737--6756
Research Domain:
  - Cryptography & Formal Verification
Research_Type: []
Risk Benefit Analysis: false
Status: Ethics Section Extracted
Subdomain:
  - Crypto
  - Systems and Protocols
title: "{S/MINE:} Collecting and Analyzing {S/MIME} Certificates at Scale"
url: https://www.usenix.org/conference/usenixsecurity25/presentation/oendaroe
Usenix.DataPrivacy: false
Usenix.HarmMitigation: false
Usenix.HumanSubjects: false
Usenix.LiveTesting: false
Usenix.ResearcherSafety: false
Usenix.StakeholderImpact: false
Usenix.ToSViolation: false
Usenix.VulnDisclosure: false
coded_date: 2026-08-28
---
