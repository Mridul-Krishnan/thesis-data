---
Alternatives Considered: true
author: Xinyue Shen and Yixin Wu and Yiting Qu and Michael Backes and Savvas Zannettou and Yang Zhang
author_tags:
  - Xinyue Shen
  - Yixin Wu
  - Yiting Qu
  - Michael Backes
  - Savvas Zannettou
  - Yang Zhang
base: "[[Databook.base]]"
coded_date: 2026-02-06T17:43:00
DBLP Ref: DBLP:conf/uss/00010Q0Z025
Direct Stakeholders:
  - Research Team
  - Software Maintainers
Emerging Themes:
  - LLM Ethics
Ethics Depth: Brief
Ethics Location:
  - Main Body
Ethics section: |-
  Our work relies on LLMs to generate samples, and all the
  manual annotations are performed by the authors of this study.
  Therefore our study is not considered human subjects research
  by ourInstitutional Review Board (IRB). Also, by doing anno
  tations ourselves, we ensure that no human subjects were ex
  posedto harmfulinformation during ourstudy. Since ourwork
  involves the assessment of LLM-driven hate campaigns, it is
  inevitable to disclose how attackers can evade a hate speech
  detector. We have taken great care to responsibly share our
  findings. We disclosed the draft paper and the labeled dataset
  to OpenAI, Google Jigsaw, and the developers of open-source
  detectors. In our disclosure letter, we explicitly highlighted
  the high attack success rates in the LLM-driven hate cam
  paigns. We have received the acknowledgment from OpenAI
  and Google Jigsaw. We are still awaiting responses from the
  developers of open-source detectors. Besides, we clearly state
  in the artifacts that this study is intended for research pur
  poses only, and any misuse is strictly prohibited. The artifacts
  are hosted with the request-access feature enabled, and we
  will manually review applicants’ information to ensure the
  responsible use of these sensitive artifacts. We believe that the
  benefits of highlighting the vulnerability outweigh the risks,
  as it can inform AI practitioners, Web communities, and the
  broader research community to develop more advanced and
  robust detectors against LLM-driven hate campaigns.
Framework Used:
  - None Explicit
Indirect Stakeholders:
  - Adversaries
  - Private Institutions
  - Broader Public
  - Vulnerable Populations
key_quotes: |-
  1. Disclaimer. This paper contains examples of hateful and abu
  sive language. Reader discretion is recommended.
  2. • RQ1:Howeffective are hate speech detectors in discern
  ing hate speech in LLM-generated content? Does their
  performance vary across LLMs and identity groups?
  • RQ2:Canhate speech detectors counteract LLM-driven
  hate campaigns, especially when the adversary employs
  advanced techniques 
  3. Annotation. We manually annotate 11,016 LLM-generated
  samples to obtain the ground truth hate labels. Specifically,
  three authors of this study, who specialize in the field of hate speech,individually assign one of three labels to each sample:
  hate, non-hate, or not applicable(N/A).
Menlo.Beneficience: true
Menlo.Justice: true
Menlo.RespectForLawAndPublicInterest: true
Menlo.RespectForPersons: false
notes: Authors do not address Impact on Researchers, which could be necessary due to creation of the HateBenchSet (annotated 11,016 LLM samples to obtain ground truth hate labels). It is recognized that the authors specialize in the field of hate spee
pages: 221--240
Research Domain:
  - Large Language Models (LLM)
Research_Type:
  - System
Risk Benefit Analysis: true
Status: Data coded
Subdomain:
  - LLM Security
title: "HateBench: Benchmarking Hate Speech Detectors on LLM-Generated Content and Hate Campaigns"
url: https://www.usenix.org/conference/usenixsecurity25/presentation/shen
Usenix.DataPrivacy: false
Usenix.HarmMitigation: true
Usenix.HumanSubjects: false
Usenix.LiveTesting: true
Usenix.ResearcherSafety: false
Usenix.StakeholderImpact: true
Usenix.ToSViolation: false
Usenix.VulnDisclosure: false
---
