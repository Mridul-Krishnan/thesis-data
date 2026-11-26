---
Alternatives Considered: false
author: Anish Chand and Nick Nikiforakis and Phani Vadrevu
author_tags:
  - Anish Chand
  - Nick Nikiforakis
  - Phani Vadrevu
base: "[[Databook.base]]"
DBLP Ref: DBLP:conf/uss/ChandNV25
Direct Stakeholders: []
Emerging Themes: []
Ethics Depth:
Ethics Location: []
Ethics section: "We approached this research with careful and deliberate attention to ethical responsibility, aiming to minimize any potential harm while evaluating the email services. Although we did not obtain prior consent from the email providers involved in our experiments, we carefully considered this decision. We determined that the practical challenges of identifying and reaching out to the appropriate point of contact within such large organizations (email providers) authorized to provide consent to our work made obtaining consent infeasible. Due to this, we designed our methodology along the lines of previous works [25, 28, 40, 43, 44, 56].\r

  Our experiments involved sending a total of 1,997 emails for the study of email reporting infrastructure (§ 4) over several days, and 495 emails over five days to evaluate the response to phishing reports (§ 5). We argue that both the volume and the rate of these emails are negligible in comparison to the daily scale handled by these services. The total number of phishing reports submitted across the entire study was 1,876. While we acknowledge that each email reported by us imposes a waste of time and resources for these email services, we argue that the total number of email reports (1,876) is very small in comparison to the large number of email reports that these services receive daily. For context, Gmail blocks around 100 million phishing emails every day [17], making our total of 1,876 email reports (across all services) negligible.\r

  To further evaluate the ethical implications of our approach, we consulted with the authors of related prior work [25] while planning our experiments, who shared their experience with us. They described how the product lead from Google Safe Browsing encouraged their team to continue sending phishing report URLs, justifying that the volume of phishing reports sent out by them had a negligible impact on Google, which receives an astronomical number of phishing reports daily.\r

  Additionally, during the account-creation phase of our experiments, some of our accounts were flagged and blocked by ProtonMail. We reached out to them and clarified that the accounts were created as part of our research project. Proton Mail acknowledged the need for our study and reactivated our accounts, indicating they were happy to let us continue with our study. In light of the feedback, statistics, and the overall setup of our experiments, we concluded that neither our emails nor our reports negatively affected any of these services. Instead, the findings from our paper can help strengthen these services against sophisticated evasions that attackers could already be silently exploiting the identified email-open signals in the wild. Furthermore, prior work in evaluating web-based phishing reporting systems [25, 26, 28, 43, 44] has also followed a similar procedure of submitting small-scale false phishing reports to investigate the security of real-world anti-phishing systems.\r

  On the website front, the phishing sites were simulated and non-functional and thus not harmful to real users in the unlikely event that they would somehow stumble upon them.\r

  The URLs were not shared outside of the reported emails, both for research results’ fidelity and ethical purposes. The email accounts were not accessible by anyone except the authors, and these accounts were not used to communicate with real users. For creating email accounts, we used personal phone numbers whenever required. Further, we have also clearly communicated the details of our measurements, including the number of false reports we made to these services in our disclosure reports to these email services."
Framework Used: []
Indirect Stakeholders: []
key_quotes: ""
Menlo.Beneficience: false
Menlo.Justice: false
Menlo.RespectForLawAndPublicInterest: false
Menlo.RespectForPersons: false
notes: ""
pages: 3181--3200
Research Domain:
  - Software Security & Development Lifecycle
Research_Type: []
Risk Benefit Analysis: false
Status: Ethics Section Extracted
Subdomain:
  - Web and Mobile Security
title: "Doubly Dangerous: Evading Phishing Reporting Systems by Leveraging Email Tracking Techniques"
url: https://www.usenix.org/conference/usenixsecurity25/presentation/chand
Usenix.DataPrivacy: false
Usenix.HarmMitigation: false
Usenix.HumanSubjects: false
Usenix.LiveTesting: false
Usenix.ResearcherSafety: false
Usenix.StakeholderImpact: false
Usenix.ToSViolation: false
Usenix.VulnDisclosure: false
coded_date: 2026-09-07
---
