---
Alternatives Considered: false
author: Jinseo Lee and Hobin Kim and Min Suk Kang
author_tags:
  - Jinseo Lee
  - Hobin Kim
  - Min Suk Kang
base: "[[Databook.base]]"
coded_date: 2026-05-28
DBLP Ref: DBLP:conf/uss/LeeKK25
Direct Stakeholders:
  - Software Maintainers
  - System Operators
Emerging Themes:
  - Call to Action/Report to Owner
Ethics Depth:
  - Detailed
Ethics Location:
  - Main Body
Ethics section: We conduct all experiments with careful ethical precautions to minimize any impact on the broader Tor network. Moreover, we have shared our attack scripts and the setup on the live Tor network with the Tor developers so that they can review any potential impact on the network while reproducing our results. As a basic precaution, we set up our own onion service as the target and establish as many introduction points as possible (twenty) to distribute the attack traffic effectively. We then carefully review the impact of our experiments on other parts of the network (e.g., relays, directory servers) to ensure it is not significant. First, in terms of bandwidth, our experiments can consume up to 3.7 Mbit per second in the worst case (771 requests/second × 602 bytes/request × 8 bit/byte). With twenty introduction points, our bandwidth consumption per relay is 0.2 Mbit/s. Given that the minimum required bandwidth is 10 Mbit/s and the recommended bandwidth is 16 Mbit/s [46], our experiments consume only 1.9% of the minimum required bandwidth (1.2% of the recommended bandwidth) even in the worst case. Next, since each experiment generates a different amount of traffic, we first calculate the maximum number of generated requests by summing the number of requests each experiment can produce. Assuming we conduct the same experiment three times, the total number of requests is 14,100,000. Given that the maximum traffic each request can generate is less than 7,000 bytes, the total traffic generated is less than 98.7 GB, with 4.9 GB per relay. Considering that the minimum required traffic is 100 GB/month and the recommended traffic is 2 TB/month [46], our experiments account for 4.9% of the minimum required traffic and 0.2% of the recommended traffic even in the worst case. Regarding CPU and memory, it is important to note that the primary target of our experiments is not the relays but the onion service under our control. Since relays are merely parts of the paths to the service, the impact on the relays’ CPU and memory is minimal. Specifically, given that relays should be able to handle at least 7,000 concurrent connections [46] and the maximum instantaneous connection rate in our experiments is 39 per relay, we only occupy 0.6% of the minimum required capacity. Even assuming each connection lasts for 5 seconds (our connections typically last less than 5 seconds), we still account for just 2.8% of the required capacity. Responsible disclosure. To ensure the ethical disclosure of our findings, we reported the discovered vulnerability to the Tor developers in August 2024. We shared comprehensive details of the vulnerability, including test sets and experiment results, to assist the developers in identifying and resolving the issue. They acknowledged the issue and the team is currently evaluating the attack strategies and working on a fix. In particular, we have obtained permission to state that the Tor’s security team is “taking it very seriously.”
Framework Used:
  - Custom
Indirect Stakeholders:
  - End Users
kanban_order: 0
key_quotes: ""
Menlo.Beneficience: true
Menlo.Justice: false
Menlo.RespectForLawAndPublicInterest: false
Menlo.RespectForPersons: false
notes: The paper investigates the DoS mitigation solution in onion services, specifically the client puzzles and new vulnerability, named Onionflation, which takes advantage of it. The research concludes that new to anonymity being central to onion networks, there will always be a trade-off between Congest and Inflation attacks to these networks. The paper discussed the impact and means of harm  mitigation to great length, and also addresses it in the ethics section. They tested the attack vector on a locally hosted network.  **Responsible Disclosure** is discussed , and how they inform Tor developers. Harm mitigation is discussed in other sections and is also the main subject of the paper (not explicitly referred to in the Ethics Section). The Live testing is only conducted in a locally hosted onion network.
pages: 3667--3685
Research Domain:
  - Network Security & Infrastructure
Research_Type:
  - Vuln Research
  - Theory
Risk Benefit Analysis: false
Status: Data coded
Subdomain:
  - Network Security
  - Routing and DoS
title: "Onions Got Puzzled: On the Challenges of Mitigating Denial-of-Service Problems in Tor Onion Services"
url: https://www.usenix.org/conference/usenixsecurity25/presentation/lee
Usenix.DataPrivacy: false
Usenix.HarmMitigation: true
Usenix.HumanSubjects: false
Usenix.LiveTesting: true
Usenix.ResearcherSafety: false
Usenix.StakeholderImpact: true
Usenix.ToSViolation: false
Usenix.VulnDisclosure: true
---
