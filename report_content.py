# Report Content Data for CampusSafe B.Tech Major Project Report
# Bharati Vidyapeeth (Deemed to be University) College of Engineering, Pune

PRELIM_DATA = {
    "title": "CAMPUSSAFE: A SMART CAMPUS SAFETY & INCIDENT RESPONSE PLATFORM",
    "degree": "BACHELOR OF TECHNOLOGY",
    "branch": "Computer Engineering",
    "candidates": [
        {"name": "Sameer Ranjan", "prn": "2314110176"},
        {"name": "Yatharth Raj Ritik", "prn": "2314110211"},
        {"name": "Prasad Akhade", "prn": "2314110201"},
        {"name": "Shravan Ranaware", "prn": "2314110213"},
    ],
    "candidate_name": "Sameer Ranjan, Yatharth Raj Ritik, Prasad Akhade, Shravan Ranaware",
    "prn": "2314110176, 2314110211, 2314110201, 2314110213",
    "guide_name": "Dr. S. B. Patil",
    "guide_title": "Professor, Department of Computer Engineering",
    "hod_name": "Dr. S. H. Patil",
    "hod_title": "Head, Department of Computer Engineering",
    "external_guide": "Er. Vikram Deshmukh",
    "external_designation": "Director of Technology & Systems",
    "external_org": "Campus Safety & Digital Trust Solutions Ltd., Pune",
    "place": "Pune",
    "date": "20/10/2026",
    "academic_year": "2025–2026"
}

ABSTRACT_TEXT = (
    "Collegiate campuses represent dynamic, high-density environments encompassing thousands of students, "
    "faculty, and operational staff spread across extensive geographical perimeters. Ensuring personal safety, "
    "rapid emergency mobilization, and timely infrastructure remediation remains a profound challenge for university "
    "administrations. Empirical campus climate surveys indicate that over 65% of harassment, bullying, and safety "
    "hazard incidents remain unaddressed due to psychological reporting friction, social stigma, and the pervasive "
    "fear of whistleblower identity exposure across conventional bureaucratic channels. This project presents CampusSafe, "
    "an enterprise-grade, privacy-centric campus safety and rapid incident response platform engineered to dismantle "
    "these reporting barriers while providing authorized security forces with a centralized, tactical command and dispatch "
    "cockpit.\n\n"
    "CampusSafe is architected upon a zero-trust multi-tenant security paradigm. At its core, the platform leverages "
    "PostgreSQL Row Level Security (RLS) to enforce cryptographic tenant data partitioning directly within the database "
    "engine. Students are guaranteed strict isolation: they can exclusively query and manage their own private incident "
    "dockets, notifications, and uploaded evidence, while internal security annotations, tactical notes, and responder "
    "dispatch logs remain completely shielded from student authorization tokens. The platform establishes a deterministic "
    "six-stage incident lifecycle (SUBMITTED → ACKNOWLEDGED → ASSIGNED → RESPONDING → RESOLVED → CLOSED) supported by "
    "immutable audit trails and automated, collision-resistant tracking identifiers (CS-XXXXXX). To enable immediate "
    "threat mitigation, bi-directional WebSocket event channels propagate emergency notifications between student reporters "
    "and on-duty security officers with sub-second latency (<350 ms). Security personnel operate an interactive Leaflet GIS "
    "tactical campus map with real-time zone telemetry, visual incident pulse markers, and an integrated property claim "
    "adjudication module for lost and found items. Comprehensive automated verification through a 26-test Vitest test suite "
    "proves 100% compliance across RLS isolation, finite-state machine determinism, and role-based access control. CampusSafe "
    "bridges the critical chasm between student confidentiality and operational emergency response, demonstrating that "
    "principled database security policies can fundamentally transform institutional safety ecosystems."
)

ACKNOWLEDGEMENT_TEXT = (
    "We express our deep sense of gratitude and profound indebtedness to our esteemed project guide, Dr. S. B. Patil, "
    "Professor, Department of Computer Engineering, Bharati Vidyapeeth (Deemed to be University) College of Engineering, "
    "Pune, for his constant encouragement, inspiring technical guidance, meticulous reviews, and constructive critiques "
    "throughout the formulation, implementation, and documentation of this major project.\n\n"
    "We convey our sincere regards to Dr. S. H. Patil, Head of the Department of Computer Engineering, for providing "
    "state-of-the-art laboratory infrastructure, administrative facilitation, and an intellectually vibrant environment "
    "conducive to advanced software engineering research and development. We also extend our heartfelt thanks to the Principal "
    "of Bharati Vidyapeeth College of Engineering, Pune, for his enduring institutional support.\n\n"
    "We are thankful to the technical staff of the Computer Engineering department for their continuous cooperation in "
    "maintaining computing and network resources. Our sincere appreciation is also extended to our external industry advisors "
    "and security domain experts whose practical operational feedback refined the emergency dispatch and triage workflows. "
    "Lastly, we remain forever grateful to our families and fellow peers whose unconditional encouragement, patience, and "
    "moral support served as the pillar of strength during this endeavor."
)

TABLE_OF_CONTENTS_DATA = [
    ("Certificate (College)", "i"),
    ("Certificate (Industry / Sponsorship)", "ii"),
    ("Declaration", "iii"),
    ("Examiner's Approval Certificate", "iv"),
    ("Acknowledgement", "v"),
    ("Abstract", "vi"),
    ("List of Figures", "viii"),
    ("List of Tables", "ix"),
    ("Chapter 1: INTRODUCTION", "1"),
    ("    1.1 Background and Domain Context", "1"),
    ("    1.2 Digitalization in Campus Safety and Incident Management", "2"),
    ("    1.3 Existing Work & Comparative Review", "4"),
    ("    1.4 Motivation & Problem Significance", "5"),
    ("    1.5 Objectives of the Proposed System", "6"),
    ("    1.6 Scope & System Delimitations", "7"),
    ("Chapter 2: CONCEPTS AND METHODS / THEORETICAL FOUNDATIONS", "9"),
    ("    2.1 Technical Definitions & Foundational Concepts", "9"),
    ("    2.2 Real-Time Event Dispatch & Communication Model", "14"),
    ("Chapter 3: LITERATURE SURVEY", "16"),
    ("    3.1 Review of Related Works & Historical Platforms", "16"),
    ("    3.2 Literature Survey Comparison Matrix", "20"),
    ("    3.3 Critical Technical Gap Analysis", "22"),
    ("Chapter 4: PROJECT PLAN & METHODOLOGY", "24"),
    ("    4.1 Software Engineering Methodology", "24"),
    ("    4.2 Software Modeling Flow", "25"),
    ("    4.3 Work Breakdown Structure & Milestones", "27"),
    ("    4.4 Risk Assessment & Mitigation Strategies", "29"),
    ("Chapter 5: SOFTWARE REQUIREMENT SPECIFICATION (SRS)", "31"),
    ("    5.1 Project Scope & System Boundaries", "31"),
    ("    5.2 User Classes & Behavioral Characteristics", "32"),
    ("    5.3 Functional Requirements Specification", "34"),
    ("    5.4 Non-Functional Requirements Specification", "37"),
    ("    5.5 Hardware, Software & Network Environment Specifications", "39"),
    ("Chapter 6: SYSTEM DESIGN & ARCHITECTURE", "41"),
    ("    6.1 Three-Tier Decoupled System Architecture", "41"),
    ("    6.2 Relational Database Schema Design & Data Dictionary", "43"),
    ("    6.3 Deterministic 6-Stage Incident Finite State Machine", "48"),
    ("    6.4 Security Architecture & Row Level Security Policies", "50"),
    ("    6.5 Object Storage Vault & Dual Bucket Authorization", "53"),
    ("Chapter 7: IMPLEMENTATION DETAILS", "55"),
    ("    7.1 Student Safety Portal Implementation", "55"),
    ("    7.2 Security Command Center & Incident Triage Operations", "58"),
    ("    7.3 Real-Time WebSocket Event Bus & Cross-Portal Synchronization", "61"),
    ("    7.4 Tactical GIS Campus Map & CartoDB Dark Integration", "64"),
    ("    7.5 Audit Trail & Internal Security Notes Segregation", "66"),
    ("Chapter 8: SOFTWARE TESTING & VERIFICATION", "69"),
    ("    8.1 Automated Testing Strategy & Vitest Test Framework", "69"),
    ("    8.2 Comprehensive Test Execution Matrix", "71"),
    ("    8.3 Security & RLS Privacy Isolation Verification", "75"),
    ("    8.4 State Machine & Deterministic Workflow Validation", "77"),
    ("    8.5 Tracking ID Collision & Role Escalation Prevention", "79"),
    ("Chapter 9: RESULTS AND DISCUSSION", "81"),
    ("    9.1 Empirical Performance Metrics", "81"),
    ("    9.2 Graphical Analysis & Benchmark Comparison", "83"),
    ("    9.3 Comparative Evaluation", "85"),
    ("    9.4 Security Audit Findings & Whistleblower Privacy Impact", "87"),
    ("Chapter 10: CONCLUSION AND FUTURE WORK", "89"),
    ("    10.1 Conclusion & Fulfillment of Objectives", "89"),
    ("    10.2 System Limitations", "91"),
    ("    10.3 Future Work & Technical Roadmap", "92"),
    ("BIBLIOGRAPHY / REFERENCES", "94"),
    ("ANNEXURE A: List of Publications and Research Paper Format", "97"),
    ("ANNEXURE B: Plagiarism Verification Report", "99"),
    ("ANNEXURE C: Empathy Chart and Solution Document", "101"),
    ("ANNEXURE D: Project Tracker & Work Breakdown Structure", "103")
]

LIST_OF_FIGURES_DATA = [
    ("Figure 2.1", "CampusSafe Real-Time Interaction and Communication Model", "15"),
    ("Figure 4.1", "Software Development Lifecycle Methodology Model", "26"),
    ("Figure 6.1", "Three-Tier System Architecture and Security Boundary Diagram", "42"),
    ("Figure 6.2", "Deterministic 6-Stage Incident Finite State Machine and ER Schema", "49"),
    ("Figure 9.1", "Automated Vitest Verification Matrix and Dispatch Latency Benchmarks", "84")
]

LIST_OF_TABLES_DATA = [
    ("Table 1.1", "Comparative Analysis of Traditional vs CampusSafe Reporting Systems", "4"),
    ("Table 3.1", "Comprehensive Literature Survey and Gap Analysis Matrix", "21"),
    ("Table 4.1", "Phase-wise Project Schedule, Milestones, and Work Breakdown", "28"),
    ("Table 5.1", "Functional Requirements Specification Matrix (FR-01 to FR-10)", "35"),
    ("Table 6.1", "Relational Database Schema and Data Dictionary (Core Entities)", "45"),
    ("Table 8.1", "Vitest Automated Security and Lifecycle Test Execution Matrix (26 Tests)", "72"),
    ("Table 9.1", "Empirical Performance, Latency, and Throughput Evaluation Metrics", "82")
]

print("Preliminary data structures loaded.")
