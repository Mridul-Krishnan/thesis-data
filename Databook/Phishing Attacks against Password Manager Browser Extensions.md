---
Alternatives Considered: false
author: Claudio Anliker and Daniele Lain and Srdjan Capkun
author_tags:
  - Claudio Anliker
  - Daniele Lain
  - Srdjan Capkun
base: "[[Databook.base]]"
DBLP Ref: DBLP:conf/uss/AnlikerLC25
Direct Stakeholders: []
Emerging Themes: []
Ethics Depth:
  - Detailed
Ethics Location: []
Ethics section: "Our study was approved by our institution’s IRB and executive board. Due to the sensitive nature of our experiment, the project was reviewed by and/or conducted in collaboration with the university’s Legal Office, Human Resources, Student Administration, IT, and Corporate Communications. In the following, we will summarize the key points of our IRB application.\r

  \r

  User deception and waiver of informed consent. Our study is a “natural observational” study, the preferred way of setting up ecologically valid experiments about phishing detection and perception [19, 26]. Both real phishing attacks and simulated phishing campaigns rely on user deception to be successful; any forewarning will likely lead to additional diligence on the participant’s part. The effect would be skewed results that do not represent the considered population’s reaction in the face of a real attack. Consequently, it is common practice not to inform participants of a phishing simulation beforehand [19, 26, 38]; Our IRB granted us a waiver of informed consent after assessing that the study respected the necessary criteria (study could not have been conducted otherwise; minimal risk for participants welfare, and full debriefing after the study ended). Furthermore, participants were informed during the debriefing of their right to opt-out, which would lead to deleting all their data.\r

  \r

  Recruitment of Participants. Following our IRB application, we encouraged the corresponding university offices to exclude vulnerable people from the study. We only involved participants whose contact data was provided to us by our university.\r

  \r

  Privacy and Data Protection. Every participant was represented with a pseudonym based on an HMAC with a secret key. However, we conducted the evaluation anonymously. To protect against data breaches, we kept demographic information separate from the study infrastructure and stored all recorded data under pseudonyms. After submission, all data will be irrevocably anonymized by deleting the secret key.\r

  \r

  Data Collection and Passwords. We did not collect any passwords, but discarded all user inputs directly in the participant’s web browser. We only saved password metadata (like length and similarity between consecutive login attempts) in our system, and took a heuristic decision about the password’s correctness. While we stored client information like browser language or User-Agent, we treated this information confidentially, and it is only associated with the aforementioned pseudonym. Furthermore, we informed participants in the debriefing in detail about what we collected and reassured them that all their data was safe.\r

  \r

  Risks and Countermeasures. We identified the following risks in our IRB application: (i) data breach, (ii) emotional distress of participants, (iii) reputational damage for the institution, and (iv) a higher workload for IT services due to the phishing simulation. We addressed all these risks, namely (i) by employing encryption, pseudonymization, and strict system monitoring during the campaign, (ii-iv) by designing a thorough and timely debriefing of all participants, and (iii/iv) by involving corporate communications before and during the simulation. After the study, we gave an interview explaining the study in detail.\r

  \r

  Phishing Mail. Our phishing simulation was different in the sense that our main interest was not how participants reacted to the email, but how they behaved on the phishing website. Consequently, we used a high-quality phishing email about public transport reimbursements after careful consideration and approval by our IRB.\r

  \r

  Debriefing. Due to the scale of our study, face-to-face debriefings were impractical. Instead, we debriefed our participants with an email and a website. To maximize credibility, we sent the email from an email address associated with our IT services and hosted the website on the official web portal of our institution. The contents of both email and website were reviewed by our IRB, corporate communications, and representatives of IT services, and improved over several iterations. Email. The purpose of the email was to provide all participants with a self-contained yet concise debriefing (around 460 words), regardless of their participation or performance. The email can be found in Section A.2. Website. The debriefing website led with the same content as the email, followed by an additional 1,500-word Q&A for participants with further questions or a special interest. The Q&A contained a total of 12 questions on the topics of phishing, password managers, and our project. The questions can be found at the end of the email in Section A.2. Debriefing Process. We ensured that the debriefing email was delivered to all participants. The debriefing process is detailed in Section 5.3.\r

  \r

  Reception. Nine participants opted out of our study. In addition, 6 participants sent us complaints by email, and around 10 complained to the authors over other channels. On the other hand, we received around 10 emails or calls of participants showing appreciation or giving positive feedback, with another 23 asking questions about phishing or our study"
Framework Used:
  - Custom
Indirect Stakeholders: []
kanban_order: 34
key_quotes: ""
Menlo.Beneficience: false
Menlo.Justice: false
Menlo.RespectForLawAndPublicInterest: false
Menlo.RespectForPersons: false
notes: ""
pages: 7857--7876
Research Domain:
  - System Security & Threat Detection
Research_Type: []
Risk Benefit Analysis: false
Status: Ethics Section Extracted
Subdomain:
  - Authentication
title: Phishing Attacks against Password Manager Browser Extensions
url: https://www.usenix.org/conference/usenixsecurity25/presentation/anliker
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
