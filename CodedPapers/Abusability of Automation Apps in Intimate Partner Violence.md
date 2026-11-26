---
Alternatives Considered: false
author: Shirley Zhang and Paul Chung and Jacob Vervelde and Nishant Korapati and Rahul Chatterjee and Kassem Fawaz
author_tags:
  - Shirley Zhang
  - Paul Chung
  - Jacob Vervelde
  - Nishant Korapati
  - Rahul Chatterjee
  - Kassem Fawaz
base: "[[Databook.base]]"
coded_date: 2026-04-30T16:27:00
DBLP Ref: DBLP:conf/uss/0002CVK0F25
Direct Stakeholders:
  - Software Maintainers
Emerging Themes:
  - Call to Action/Report to Owner
Ethics Depth: Detailed
Ethics Location:
  - Main Body
Ethics section: "This research involves two primary activities: (1) evaluating publicly available mobile automation applications, and (2) collecting and analyzing publicly shared automation “recipes” or scripts. Our goal is to understand the abuse potential of these tools in the specific and increasingly relevant threat model of interpersonal abuse, and to inform proactive strategies for harm reduction. Research Artifacts. During our research, we identified and developed several automation recipes that could potentially be used for surveillance, harassment, or other abusive purposes. While these artifacts are valuable for understanding risk and for building future detection systems, they also pose potential for misuse. Our aim is to assess and raise awareness about such risks—not to enable abuse. To minimize harm, we do not share links to harmful recipes or include detailed methods for bypassing app restrictions in the paper or accompanying materials. We follow principles similar to those used in security research on malware or phishing, where risky artifacts are shared responsibly for scientific benefit but not publicly released. We make our dataset of potentially harmful recipes available only to verified academic researchers, upon explicit written request. Access to these materials is granted under the condition that they are not redistributed or used outside of a research context. Our institution maintains a formal datasharing process to authenticate and vet requesting researchers. All shared datasets are accompanied by clear warnings about their potential for misuse and the expectation of ethical use only within academic and research boundaries. Research Environment. Studying tools and scenarios related to interpersonal abuse can take a psychological toll. To support researcher well-being, the research team holds regular check-ins to discuss progress and emotional impacts. Two team members have formal training and professional experience working with survivors of intimate partner violence (IPV). All testing of potentially harmful recipes was conducted on secured, dedicated research devices. No personal devices or accounts were used, and no personal data was involved at any stage of the analysis. Responsible Disclosure. We followed responsible disclosure practices by notifying relevant developers and platform operators — including Apple (Shortcuts), Tasker, and ShareShortcuts — about the abuse potential of recipes on their platforms. Our goal was to assist these stakeholders in recognizing risks and improving safeguards in their tools. This research addresses an underexplored but pressing threat to vulnerable individuals through automation applications. We approach this work with careful attention to ethics: avoiding the dissemination of harmful technical details, restricting access to potentially abusive content, and prioritizing both researcher safety and survivor protection. We hope this work helps the broader community better recognize and mitigate the risks of automation abuse."
Framework Used:
  - Custom
Indirect Stakeholders:
  - End Users
  - Vulnerable Populations
key_quotes: “For all data access that includes mapping pseudonyms to the real names of recipes and the raw XML files of recipes, we will share a “restricted access” dataset with researchers who have been verified by our university’s research ethics committee upon request.” , “After mapping capabilities and analyzing shortcuts in public domains, we reported safety concerns about automation applications in an IPV setting to the application carrier and public domain manager in September 2024.”
Menlo.Beneficience: true
Menlo.Justice: true
Menlo.RespectForLawAndPublicInterest: false
Menlo.RespectForPersons: true
notes: The paper analyses automation apps revolving a round a TFA (Technology Facilitated) Threat Model in the context of IPV(Intimate Partner Violence). The context of the paper innately has ethical aspects to it. The authors create a tool, a LLM.-Powered Detector that can help mitigate the TFA attacks via automation apps. While not explicitly discussed the in the ethics section as it the objective of the paper itself, stakeholder impacts are assessed (Software Maintainers and End Users) , and  the respective owners of the apps were also reached out to and informed. The research environment and team is also addressed in the ethics section. Overall, the ethics has been comprehensively discussed.
pages: 41--60
Research Domain:
  - Usable Security & Privacy
Research_Type:
  - Vuln Research
  - System
Risk Benefit Analysis: true
Status: Data coded
Subdomain:
  - Social Issues and Usable Security and Privacy
title: Abusability of Automation Apps in Intimate Partner Violence
url: https://www.usenix.org/conference/usenixsecurity25/presentation/zhang-shirley
Usenix.DataPrivacy: true
Usenix.HarmMitigation: true
Usenix.HumanSubjects: false
Usenix.LiveTesting: false
Usenix.ResearcherSafety: true
Usenix.StakeholderImpact: true
Usenix.ToSViolation: false
Usenix.VulnDisclosure: true
---
