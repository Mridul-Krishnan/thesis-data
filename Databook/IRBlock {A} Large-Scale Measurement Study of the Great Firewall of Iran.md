---
Alternatives Considered: false
author: Jonas Tai and Karthik Nishanth Sengottuvelavan and Peter Whiting and Nguyen Phong Hoang
author_tags:
  - Jonas Tai
  - Karthik Nishanth Sengottuvelavan
  - Peter Whiting
  - Nguyen Phong Hoang
base: "[[Databook.base]]"
DBLP Ref: DBLP:conf/uss/TaiSWH25
Direct Stakeholders: []
Emerging Themes: []
Ethics Depth:
Ethics Location: []
Ethics section: Internet censorship research, particularly at the national scale, raises distinct ethical challenges given the political sensitivity of the topic and the risk of misattribution or unintended disruption [46, 66]. We assess our methodology through the lens of the ethical principles articulated in the Menlo Report [24] (Respect for Persons, Beneficence, Justice, and Respect for Law and Public Interest), guidance from USENIX Security regarding research ethics [16], and recent literature [47]. Tradeoffs and Motivations. Our primary goal is to measure the design and deployment of Iran’s national censorship infrastructure while minimizing risk to individuals inside the country. To this end, IRBlock is designed to rely only on external probing techniques. We do not involve or intend to use volunteers, VPN infrastructure, or in-country public servers, as done in some prior measurement studies (e.g., OONI [37], ICLab [51], or Censored Planet [63]), thereby minimizing ethical exposure for local actors. Instead, IRBlock uses bidirectional measurement techniques, relying solely on censorship infrastructure reacting to externally generated probes. This approach builds on and significantly extends prior work, such as Iris [59], Censored Planet [63], and TMC [54], which justify scanning public infrastructure for public-interest research while minimizing risk. Our design incorporates additional safeguards such as responsive-IP exclusion in the second phase of our measurements and opt-out mechanisms. Impact of Our Measurements. We use a two-phase measurement process. The first phase involves lightweight probing of Iran’s IPv4 address space to identify IPs subject to censorship. These probes—limited to 19 domains tested per IP—are minimal in bandwidth and designed to not initiate any actual application-layer sessions due to the unsolicited and stateless nature of our probing packets. These probes are sent to all IPv4 addresses, potentially including responsive ones. While this is not our intention, sending packets to responsive addresses introduces additional ethical complexity. However, omitting all responsive IPs, over 600k in Iran according to Censys data [33], would reduce the fidelity of our data and obscure important findings. For example, we would not have discovered stable exceptions like president.ir (mapped to 185.143.233.120), or special uncensored IPs linked to state-sponsored malware operations [18]. As discussed in §4.1, these findings are crucial for understanding the granularity and policy exceptions of censorship deployment. To mitigate any potential impact on responsive addresses, we have implemented several safeguards. First, one of the 19 domains tested is a domain under our control that we know is not censored and has the form optout.our_research_domain.tld. The presence of this domain in the payload would allow any entity observing it to reach out to us for an opt-out request. Second, our scanning machines have HTTP port 80 open to serve the opt-out page while their IPs are mapped to DNS PTR records, pointing to the opt-out domain as well. This is the best practice and widely adopted within Internet measurement research that involves network scanning [15, 34, 35]. Another potential ethical consideration is that our initial DNS scan of Iran’s IPv4 address space may result in some queries for blocked domains being received by open DNS forwarders [52]. In such cases, the forwarder may relay the query to an upstream resolver, possibly generating an additional DNS lookup. Nonetheless, the forwarded request does not initiate any subsequent application-level communications with the censored domain (e.g., Web requests), and no enduser is directly involved. While we assess the likelihood of harm to be extremely low, we recognize that future studies may further reduce exposure by pre-filtering active forwarders using non-sensitive control domains. Future work can adopt such refinements to further reduce ethical risk while maintaining measurement fidelity. In retrospect, to eliminate even this small risk we could have excluded the about 11k IPs in Iran that respond to DNS queries on port 53 (Censys, May 2025 [33]). The impact of excluding those DNS-responsive IPs from our initial DNS scans would not have affected our discovery of special-exception IPs, since none of them answered on port 53. For the second measurement phase, we only probe IPs that have been identified as censored in the first phase and are not alive based on up-to-date data provided by Censys [33]. Moreover, we have revamped our measurement tools to include active SYN checks before sending more probes, minimizing unnecessary contact with responsive IPs if Censys data happens to be outdated or missing some. Finally, we note that if Iranian authorities were to investigate our probes, it would be evident that all measurement traffic originates from our machines located outside of Iran. At no point do we rely on infrastructure or relays within the country. This design decision was intentional and reflects our goal of minimizing risk to individuals inside the country. As of this writing, we have not received any complaints or opt-out requests related to our probing activities, suggesting that the traffic did not cause any disruptions or has been misinterpreted by network operators. Testing Frequency Considerations. Given that the majority of censored infrastructure in Iran appears to not change drastically over the course of our study, we can reduce scan frequency for long-term monitoring from daily to once per week or spread it over a longer time frame. This reduction further minimizes exposure while maintaining the ability to detect policy shifts or infrastructure reconfiguration. However, it is important to note that IRBlock is designed to flexibly launch new scans any time granularity in response to emerging events, if needed. Public Benefits. In accordance with the Menlo Report’s principle of Justice [24], our research is designed to support a broad range of stakeholders—including researchers, journalists, policymakers, and circumvention tool developers. By identifying blocking infrastructure, policy granularity, and operational fingerprints of censorship in Iran, we aim to support digital rights advocacy and informed public debate. We will publish our dataset and measurement scripts, enabling transparent validation of our study and facilitates future research. One may concern that releasing our work could also help the censor to improve their censorship infrastructure. However, we believe that the benefits of transparency and open science outweigh the risks. The Iranian government is already aware of the existence of censorship measurement and circumvention tools. By sharing our findings, we aim to empower individuals and organizations working to resist censorship and promote digital rights. To that end, IRBlock is designed to balance the imperative to understand widespread censorship with the obligation to minimize risk. We strive to be transparent, proactive, and responsive to feedback from the community. We are committed to keeping IRBlock operational and to continuously improving our measurement techniques. We believe that the potential benefits of our work—in documenting and enabling resistance to repressive information controls—outweigh the minimal and carefully mitigated risks associated with our methodology.
Framework Used: []
Indirect Stakeholders: []
kanban_order: 19
key_quotes: ""
Menlo.Beneficience: false
Menlo.Justice: false
Menlo.RespectForLawAndPublicInterest: false
Menlo.RespectForPersons: false
notes: ""
pages: 705--722
Research Domain:
  - Network Security & Infrastructure
Research_Type: []
Risk Benefit Analysis: false
Status: Ethics Section Extracted
Subdomain:
  - Network Security
  - Censorship Evasion and Trustworthy Infrastructure
title: "IRBlock: {A} Large-Scale Measurement Study of the Great Firewall of Iran"
url: https://www.usenix.org/conference/usenixsecurity25/presentation/tai
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
