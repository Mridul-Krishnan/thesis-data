---
Alternatives Considered: false
author: Sayak Saha Roy and Elham Pourabbas Vafa and Kobra Khanmohamaddi and Shirin Nilizadeh
author_tags:
  - Sayak Saha Roy
  - Elham Pourabbas Vafa
  - Kobra Khanmohamaddi
  - Shirin Nilizadeh
base: "[[Databook.base]]"
DBLP Ref: DBLP:conf/uss/RoyVKN25
Direct Stakeholders:
  - Software Maintainers
Emerging Themes:
  - Stakeholder Identification
  -  Ethical and Legal Challenges
Ethics Depth:
  - Detailed
Ethics Location:
  - Extra Page
Ethics section: 'Ethical Considerations: As per the USENIX Security guidelines for ethical considerations, we have included this ethics report in accordance with the principles outlined in their call for papers and submission policies. Our research on Telegram CACs was conducted with a thorough consideration of ethical implications, grounded in consequentialist and deontological ethics. Throughout the study, we prioritized transparency, privacy, and the potential impact on various stakeholders, including Telegram users, cybercrime victims, and the broader cybersecurity community. Stakeholder Considerations: Key stakeholders include the users and administrators of cybercriminal channels, potential victims (such as organizations and individuals affected by criminal activities), law enforcement agencies, and Telegram as a platform. We took special care to avoid interacting with sensitive content and focused exclusively on metadata and filenames, ensuring no personally identifiable information (PII) was involved. When releasing datasets, we employed Microsoft Presidio [4], an offline Python library that anonymizes sensitive text in data, to obfuscate all PII and excluded links to any compromised credentials. A dual manual review process by two coders, including the first author, further ensured the absence of PII. Data that could not be fully obfuscated was excluded from our analysis, and we promptly deleted such information from our experimental setup. Similarly, for malicious content and phishing URLs, we removed the data after completing the analysis. Furthermore, we respect the rights and autonomy of individuals who engaged in potentially illegal activities as well by obfuscating the identifiable channel information from all screenshots in the paper, and not including their names in the text as well. Consequentialist Ethics: In alignment with the Beneficence principle outlined in The Menlo Report [16], we sought to minimize harm while maximizing the benefits of our research. The primary long-term benefit lies in identifying harmful CACs and their content, potentially leading to their removal and reducing the spread of cybercriminal activity on Telegram. We recognize the risk of unintended consequences, such as criminals adapting to evade detection. To mitigate this, we limited the disclosure of specific vulnerabilities or methods in our DarkGram framework that could be exploited by malicious actors. Deontological Ethics: In line with the Respect for Personsprinciple, as previously mentoned in "Stakeholder Considerations", we ensured that no private or personally identifiable information (PII) was compromised during the course of our research. Also, our team avoided interacting with cybercriminals directly, and we did not engage in any actions that would violate the privacy or rights of the individuals involved. We did not download files that contained sensitive information (e.g., credentials) and focused our analysis strictly on the metadata and public information available from Telegram channels. Since our research did not involve direct interaction with human subjects or sensitive personal information, our study was deemed not to require an Institutional Review Board (IRB) approval. Disclosure and Vulnerability Reporting: When vulnerabilities or malicious content were identified, we followed responsible disclosure practices by promptly reporting them within 12 hours to Telegram and affected organizations (e.g., email providers, and domain hosts). We adhered to responsible disclosure timelines, allowing organizations to address the threats (for as long as required since verifying some of our reports, such as compromised credentials or malware can be a time-consuming process) before publicizing any findings. Also our public reports contain only aggregated statistics without identifying specific organizations. In our open-sourced dataset, we exclude any unresolved disclosures that had not been confirmed by vendors, which does reduce the size of our dataset that was open-sourced. As a result of these efforts, 196 channels were taken down, and several phishing and malware URLs were mitigated. Legal and Ethical Compliance: We ensured that our research complied with all applicable laws and respected platform terms of service, especially in our interactions with the Telegram API. We avoided conducting live experiments that could harm legitimate users or violate any platform’s policies. Proactive Ethics Consideration: Ethical considerations were proactively integrated at every stage of our research process as mentioned in the proceeding paragraphs. From project design to data collection and analysis, we continuously evaluated potential harms and benefits, allowing us to anticipate ethical challenges and implement solutions accordingly.'
Framework Used:
  - Custom
  - Menlo
  - USENIX Guidelines
Indirect Stakeholders:
  - Adversaries
  - End Users
kanban_order: V0
key_quotes: ""
Menlo.Beneficience: true
Menlo.Justice: true
Menlo.RespectForLawAndPublicInterest: true
Menlo.RespectForPersons: false
notes: The ethics page also addresses the paper from a Consequentialist and Deontological view, as well as from a legal perspective. It covers stakeholder analysis including a harms to consumers in an separate section.
pages: 4839--4858
Research Domain:
  - System Security & Threat Detection
Research_Type:
  - Measurement
  - Theory
Risk Benefit Analysis: true
Status: Data coded
Subdomain:
  - Fraud Malware Spam
title: "DarkGram: {A} Large-Scale Analysis of Cybercriminal Activity Channels on Telegram"
url: https://www.usenix.org/conference/usenixsecurity25/presentation/roy
Usenix.DataPrivacy: false
Usenix.HarmMitigation: true
Usenix.HumanSubjects: false
Usenix.LiveTesting: true
Usenix.ResearcherSafety: false
Usenix.StakeholderImpact: true
Usenix.ToSViolation: false
Usenix.VulnDisclosure: true
coded_date: 2026-11-01
---
