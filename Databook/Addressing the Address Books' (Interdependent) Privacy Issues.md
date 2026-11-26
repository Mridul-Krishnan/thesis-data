---
Alternatives Considered: false
author: Kavous Salehzadeh Niksirat and Lev Velykoivanenko and Samuel M{\"{a}}tzler and Stephan Mulders and Aurelia Tam{\`{o}}{-}Larrieux and Marc{-}Olivier Boldi and Mathias Humbert and K{\'{e}}vin Huguenin
author_tags:
  - Kavous Salehzadeh Niksirat
  - Lev Velykoivanenko
  - Samuel M{\"{a}}tzler
  - Stephan Mulders
  - Aurelia Tam{\`{o}}{-}Larrieux
  - Marc{-}Olivier Boldi
  - Mathias Humbert
  - K{\'{e}}vin Huguenin
base: "[[Databook.base]]"
DBLP Ref: DBLP:conf/uss/NiksiratVMMTBHH25
Direct Stakeholders: []
Emerging Themes: []
Ethics Depth:
Ethics Location: []
Ethics section: "Our research received IRB approval. All respondents provided informed consent detailing the study’s purpose, data handling, withdrawal procedure, and compensation. We followed Prolific’s guidelines, compensating above the minimum recommended rate of GBP 9 per hour, consistent with ethical norms for fair compensation.19 There are two primary stakeholders: (1) respondents, who were asked to respond to the survey and, in some cases, share DAB summaries; and (2) DAB-SPs, contacted via DARs. We assessed risks across these groups. We minimized respondent risk through transparent communication and secure data collection. While DAB-SPs faced no legal or privacy risks, we address ethical concerns around our DARs. Next, we discuss various ethical considerations. Contacting DAB-SPs. We contacted five large DAB-SPs with GDPR-based DARs to explore how they assess interdependent data protection situations in practice—particularly how their corporate legal compliance teams view and treat IDP situations. For one DAB-SP (Proton), even though it uses E2EE, there was uncertainty (when sending DARs) around its legal roles due to technical unknowns (e.g., whether con tact cards were E2E-encrypted and whether all users enabled E2EE). Since email addresses, as we later learned, are not encrypted, Proton could have answered our query (“How many contact cards in your database contain my email address?”). Similar ambiguity existed with other DAB-SPs, whose public documentation did not clarify whether they act as controllers, processors, or joint controllers. Thus, our DARs were care fully formulated to avoid requesting access to sensitive or encrypted user content. Also, even if a DAB-SP concluded it was not a controller, our limited inquiries—only 2–3 e-mail exchanges—posed no harm. Our intent was not to coerce responses but to explore real-world inconsistencies and responses within a gray area of legal interpretation. Unlike large-scale DAR campaigns,9 our outreach was narrow, trans parent, and focused, with minimal burden on recipients. We view this as an ethically appropriate legal research practice that helps clarify underexplored regulatory boundaries. DDS Platform. In Study #2, respondents could choose to share structured summaries of their DABs using DDS [87]. The consent form specified that only aggregate statistics (i.e., the proportion of contact cards with certain fields) would be collected—no raw data would be stored. DDS uses OAuth based, granular consent: respondents authorize access to spe cific data categories, preview what will be accessed (i.e., see [87][p. 15, Figure 9a]) and computed (i.e., see S2.B6), and may opt-out at any point (i.e., see S2.B2). All raw data is processed temporarily in memory to compute predefined variables (e.g., number of contacts with e-mail addresses), which are then uploaded to the survey platform (Qualtrics); 19See https://researcher-help.prolific.com/en/article/2273bd. researchers access only these variables. DDS aligns with data donation principles [11]20 while emphasizing user control and transparency and adding safeguards via API scopes and selective access. To reduce re-identification risk, we excluded DABs with fewer than five contacts. DDS does not otherwise differentiate based on the dataset size, but we explicitly eval uated the sensitivity of small summaries and found minimal risk when dissociated from respondent identity. Treatment of Withdrawn Respondents. Those who with drew from the main survey had their survey session immediately terminated, and no data from these sessions was retained or analyzed (except for the count of withdrawals). Only their Prolific IDs, completion statuses (i.e., “withdrew”), and timings remained accessible on Prolific for standard respondents tracking. Respondents also received distinct completion codes reflecting their paths through the survey. For example, participants who granted access to their Google Contacts data received a different code than those who preferred to with draw. While this deviates slightly from Prolific’s typical use of a single, uniform completion code per study, it enabled us to accurately manage the study. Using these completion codes, we were able to later send an invitation for a short, optional, follow-up study focused only on their decision to withdraw. This follow-up was conducted as a separate study with independent consent. While this procedure complies with Prolific’s standard recruitment model and involved no reuse of personal data without re-consent, we acknowledge that our original consent form could have more clearly communicated the possibility of such follow-up contact. Positionality Statement. Our team is composed of computer scientists, covering both technical and user-centric aspects in the field of security and (interdependent) privacy, and of legal scholars, specialized in digital law and data protection. One of the legal researchers is a practicing attorney focused on data protection and IT law. The team is based in Europe."
Framework Used: []
Indirect Stakeholders: []
kanban_order: 6
key_quotes: ""
Menlo.Beneficience: false
Menlo.Justice: false
Menlo.RespectForLawAndPublicInterest: false
Menlo.RespectForPersons: false
notes: ""
pages: 6501--6520
Research Domain:
  - System Security & Threat Detection
Research_Type: []
Risk Benefit Analysis: false
Status: Ethics Section Extracted
Subdomain:
  - Privacy
  - Attacks
title: Addressing the Address Books' (Interdependent) Privacy Issues
url: https://www.usenix.org/conference/usenixsecurity25/presentation/niksirat
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
