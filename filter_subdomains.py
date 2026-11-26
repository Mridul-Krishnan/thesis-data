''' # This script filters unique subdomains from a CSV file containing a list of subdomains
'''


import pandas as pd

path = "Your_CSV_File_Path_Here"

df = pd.read_csv(path)
# Remove numbers and strip whitespace from subdomains
print("Number of unique subdomains:", len(df.drop_duplicates()))

# Order matters, primarily to prevent Privacy which is applicable to multiple domains from being matched too early.

RULES = [
    ("Large Language Models (LLM)", [
        "LLM Security", "LLM Privacy", "Vulnerabilities in LLMs",
        "Jailbreaking and Prompt Stealing", "Privacy Safety and Defense",
    ]),
    ("Machine Learning & AI (non-LLM)", [
        "ML and AI Security", "ML and AI Privacy", "Backdoors Poisoning Unlearning",
        "Robustness", "Federated Learning and Protecting Data",
    ]),
    ("Cryptography & Formal Verification", [
        "Crypto", "Zero Knowledge and Multi-Party Computation",
        "Formal Methods and Private Computation", "HE MPC Oblivious Computation",
        "Systems and Protocols", "Privacy-Preserving Computation",
        "Private Information Retrieval and Computation",
    ]),
    ("Usable Security & Privacy", [
            "Social Issues and Usable Security and Privacy",
            "Usable Privacy and Security", "Images",
        ]),
    ("Blockchain & Distributed Ledger Security", [
        "Blockchain Security Attacks and Defenses",
        "Infrastructure Protocol Design and Governance",
    ]),
    ("Hardware & Embedded Systems Security", [
        "Embedded and Hardware Security", "Hardware Security", "Microarchitectures",
        "Side-Channel and Fault Injection Attacks", "Trusted and Robust Computing",
    ]),
    ("Network Security & Infrastructure", [
        "Network Security", "Censorship Evasion and Trustworthy Infrastructure",
        "Routing and DoS", "BLE and Cellular", "Internet and Beyond",
    ]),
    ("System Security & Threat Detection", [
        "System Security", "Threat Detection Exploitation and Adaptive Defenses",
        "Attacks", "Fraud Malware Spam", "Kernel and Low-Level System Security",
        "Authentication", "Securing Systems and Protocols",
    ]),
    ("Software Security & Development Lifecycle", [
        "Software Security", "Software Security and Usable Security",
        "Software and Experts", "Web and Mobile Security", "Mobile Platforms",
        "Patching and Repair", "Fuzzing", "Fuzzing and Other Software Analysis",
        "Web Security",
    ]),
    ("Privacy (Data Security & Analytics)", [
            "Privacy", "Differential Privacy and Audit",
            "Consent Compliance and Provable Privacy",
        ]),
    
]


def consolidate(subdomain):
    text = str(subdomain)
    for domain, keywords in RULES:
        if any(k in text for k in keywords):
            return domain
    return ""


df["Consolidated Domain"] = df["Subdomain"].apply(consolidate)

counts = df["Consolidated Domain"].replace("", "(unmatched)").value_counts().sort_index()
print(counts.to_string())
print("Total rows:", len(df))
print("Total classified:", (df["Consolidated Domain"] != "").sum())

# df.to_csv("track_subdomain_consolidated.csv", index=False)
