---
Alternatives Considered: false
author: Shubham Agarwal and Rafael Mrowczynski and Maria Hellenthal and Ben Stock
author_tags:
  - Shubham Agarwal
  - Rafael Mrowczynski
  - Maria Hellenthal
  - Ben Stock
base: "[[Databook.base]]"
coded_date: 2026-04-23T15:05:00
DBLP Ref: DBLP:conf/uss/0006MHS25
Direct Stakeholders:
  - Study Participants
  - System Operators
  - Data Subjects
  - Software Maintainers
Emerging Themes:
  - Call to Action/Report to Owner
Ethics Depth:
  - Detailed
Ethics Location:
  - Main Body
Ethics section: "We proactively considered and modeled the ethical and legal factors associated with the individual stakeholders that may be directly or indirectly affected throughout the course of the design and execution of this study. Additionally, our Institutional Review Board approved our study design and the methodology before we moved to the execution stage. Below, we discuss in detail the potential risks and benefits associated with these stakeholders in line with our adopted methodology. Recruitment Strategy: We collected the publicly available email addresses of the extension developers and associated details on their extensions that were available on CWS and AMO. However, we only sent invites to those developers who fulfilled our study criteria. While we could have recruited participants through social media platforms and developerfocused forums, we would have been unable to derive concrete details and statistics on their live extensions. Further, none of the participants expressed any discomfort or anguish; some were even positively surprised to be contacted for the study. Participants’ Rights: In the first stage of our study, we sent email invites to the extension developers, inviting them to participate in our study by completing the pre-screening survey. The questionnaire included a detailed explanation of the purpose of the data collection, and we only collected data from those individuals who provided explicit consent to participate. Further, we separately collected individuals’ consent for data collection during the interview (i.e., audio, video, and screen recording), provided to them along with the scheduling details. In addition, right before starting the interview, we verbally explained their rights, including the option to quit at any time or to skip answering questions they felt uncomfortable with during the interview. Participants could also switch off the video feed during the interview if preferred. During recruitment, we only informed participants that we were Computer Science researchers to minimize potential biases in their responses. However, we made sure to inform them about our full background and the purpose of the study after the interview. Coding Task Design: We asked our participants to download the extension files provided by us to work on the coding tasks and share their screens. An alternative approach could have been to provide them with remote access to our machines for the coding tasks to avoid any risk of capturing user-sensitive data during screen-sharing. However, we provided them with the extension files to allow them to work on their accustomed setup that they use for development: the IDE, the AI tools and plugins used for development, and the preferred browser. This approach allowed us to capture their real-world development tools and environment while providing them with the flexibility to work as they usually would. As a precautionary step, we explicitly asked them to close any sensitive applications before starting screen-sharing, both in the email containing interview details and verbally before the task began. Unfortunately, one of the participants did not carefully read the email and refused to work on the coding task, as they were reluctant to download files to their machine. The test website and the extensions designed for the coding tasks did not request or capture any privacy-sensitive identifiers (e.g., IP address, device identifiers, etc.) at any point and were hosted within our institutional network. The second coding task involved embedding a live website – Amazon, in an iframe as a solution by appropriately handling the framing policy enforced by the website. We resorted to using Amazon for our study to factor in the proximity to the realworld scenario of the coding task in terms of the participants’ familiarity with the website along with the severity of the perceived threat. Additionally, the task only required to query the publicly exposed Amazon search endpoint for products and load inside an iframe, with no further interactions required. This ensured not violating any terms of service [6, 94]. Hence, we believe that our coding task did not incur any tangible or intangible damages to the live website. Data Collection & Transparency: As discussed before, we collected user data at different stages of our study for analysis. Importantly, we stored all the data collected through the pre-screening survey and the interviews within our institutional premises. Further, we deleted all the personally identifiable information (e.g., demographics, audio/video recordings, etc.) associated with the participants upon the completion of data analysis and only stored the anonymized and aggregated results for later verification. We used the in-house instance of the OpenAI Whisper model for transcription services. Naturally, the artifacts related to this study are accessible exclusively to the members directly involved in the study. At no stage do we share any raw or processed data with any third-party entities. Responsible Disclosure: We believe that the insights gathered from our study participants may help facilitate changes and guide towards an improved ecosystem, including, but not limited to, the security and privacy aspects. Thus, we plan to create an additional artifact that would include the participants’ views, perceptions, and expectations beyond what is discussed in this paper. We plan to reach out to the store vendors and provide them with gathered insights so that they can take the necessary steps in the future. Naturally, we will not include any PIIs related to any of the participants in our study."
Framework Used:
  - IRB
  - Custom
Indirect Stakeholders:
  - Broader Public
key_quotes: ""
Menlo.Beneficience: true
Menlo.Justice: false
Menlo.RespectForLawAndPublicInterest: true
Menlo.RespectForPersons: true
notes: The paper conducts a qualitative study, consisting of a semi-structure interview and a coding task, for to evaluate the perception and mindset of browser extension developers. The section 4.3 Sampling & Recruitment describes extensively the procedure of choosing the developers for the study, including a pre-screening survey and also change in sampling strategy to ensure diversity in the subjects. Maintaining privacy and anonymity of the  of the subjects are also addressed Careful effort has been put also ensure that the subject of study itself didn’t influence the developer to prepare themselves prior to the interview (authors pointed out a case where a possible subject researched the authors beforehand which influenced their mindset and had to be ejected from the study). The ethics section is thorough with respect to the study, and they their methodology inspected by their respective IRB prior to executing it. Section 7 Conclusion and Call to Action also addresses the responsibility of the System Operators (in this case the browser operators) in in taking proactive measures to mitigate current threats and set more secure standards for extension development.
pages: 2927--2946
Research Domain:
  - Software Security & Development Lifecycle
Research_Type:
  - Human Subjects
Risk Benefit Analysis: true
Status: Data coded
Subdomain:
  - Software Security and Usable Security
title: '"I have no idea how to make it safer": Studying Security and Privacy Mindsets of Browser Extension Developers'
url: https://www.usenix.org/conference/usenixsecurity25/presentation/agarwal-shubham
Usenix.DataPrivacy: true
Usenix.HarmMitigation: false
Usenix.HumanSubjects: true
Usenix.LiveTesting: true
Usenix.ResearcherSafety: false
Usenix.StakeholderImpact: false
Usenix.ToSViolation: false
Usenix.VulnDisclosure: false
---
