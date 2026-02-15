# CCNA Hybrid Professional Exam Simulator

A command-line based CCNA (200-301) exam simulator written in Python.

---

## Project Overview

The CCNA Hybrid Professional Exam Simulator is a structured exam preparation tool designed to simulate a realistic Cisco CCNA certification experience.

The simulator combines:

- 40 scenario-based static questions (exam-style)
- 20 dynamically generated questions (subnetting & routing interpretation)
- Randomized question and answer order
- Domain-based performance analysis

This project was developed as part of independent certification preparation and portfolio development.

---

## Key Features

- 60-question hybrid exam session
- Scenario-based and troubleshooting-focused questions
- Dynamic subnetting calculations
- Routing table metric interpretation
- Support for single-answer and multiple-answer questions
- Domain performance breakdown
- Clean CLI-based exam layout

---

## Covered CCNA Domains

- Network Fundamentals
- Network Access
- IP Connectivity
- IP Services
- Security Fundamentals
- Automation & Programmability

---

## Technologies Used

- Python 3
- Standard library modules (`random`, `ipaddress`, `collections`)

No external dependencies required.

---

## How to Run

Run the simulator from the project directory:

```
python ccna-hybrid-exam-simulator.py
```

---

## How It Works

- Questions are randomized for each session.
- Answer options are shuffled dynamically.
- Subnetting questions generate unique network ranges.
- Routing interpretation questions simulate real Cisco routing table output.
- Final score and percentage are displayed at the end of the exam.
- Domain analysis helps identify weak knowledge areas.

---

## Example Output

```
FINAL SCORE: 46/60
PERCENTAGE: 76.67%

DOMAIN ANALYSIS
Network Fundamentals: 8/10 (80%)
IP Connectivity: 12/15 (80%)
Security Fundamentals: 4/6 (66%)
```

---

## Future Improvements

- 90-minute timed exam mode
- Adaptive difficulty system
- CLI configuration simulation mode
- Result storage for long-term performance tracking
- Expanded question database (100+ unique scenarios)

---

## Educational Purpose

This project is intended for structured CCNA exam preparation.

It focuses on:

- Conceptual understanding
- Troubleshooting skills
- Subnetting speed improvement
- Routing table interpretation

This is not a certification dump tool.  
It is designed for learning and exam-style training.

---

## Author

Created as part of independent study and certification preparation.
