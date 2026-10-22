# Lab 5: Static Code Analysis — Parking Lot System

A Python parking lot management program analyzed and improved using **Pylint, Bandit, and Flake8**.

## Overview

This project demonstrates how static code analysis can improve Python code quality, security, readability, and maintainability.

The original program contained several issues, including unsafe expression evaluation, weak hashing, insecure random number generation, broad exception handling, mutable default arguments, and style violations.

The code was refactored to address these findings while preserving the core parking lot functionality.

## Features

- Park vehicles in available parking slots.
- Release occupied parking slots.
- Check parking slot availability.
- Calculate parking fees using a surge multiplier.
- Generate SHA-256 hashes for vehicle registration numbers.
- Generate four-digit ticket PINs using Python's `secrets` module.
- Export parking slot information to a manifest file.
- Count available parking slots.

## Technology Stack

- **Language:** Python 3
- **Static analysis:** Pylint, Bandit, Flake8
- **Version control:** Git and GitHub

## Project Structure

```text
L5_51_parking_lot_system/
├── parking_lot_system.py
├── issues.md
├── reflection.md
├── pylint_report_before.txt
├── pylint_report_after.txt
├── bandit_report_before.txt
├── bandit_report_after.txt
├── flake8_report_before.txt
├── flake8_report_after.txt
├── README.md
└── parking_manifest.txt   # Generated at runtime
```

## Setup and Execution

### 1. Clone the repository

```bash
git clone https://github.com/Dhruva-Girish/L5_51_parking_lot_system.git
cd L5_51_parking_lot_system
```

### 2. Create and activate a virtual environment

On macOS or Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install the analysis tools

```bash
python -m pip install pylint bandit flake8
```

### 4. Run the program

```bash
python parking_lot_system.py
```

The program demonstrates parking operations, availability checks, surge fee calculation, vehicle hashing, ticket PIN generation, and manifest export.

## Static Code Analysis

The program was analyzed using three tools.

### Pylint — Code Quality

Pylint identifies code-quality issues, naming violations, unused variables, missing documentation, and potentially error-prone programming practices.

Run:

```bash
pylint parking_lot_system.py
```

### Bandit — Security Analysis

Bandit detects common security issues in Python source code.

Run:

```bash
bandit -r parking_lot_system.py
```

### Flake8 — Style and Formatting

Flake8 checks Python style conventions, whitespace, line length, and related violations.

Run:

```bash
flake8 parking_lot_system.py
```

## Issues Identified and Fixed

The original code was improved by addressing the following issues:

| Issue | Fix |
|---|---|
| Mutable default argument | Replaced the shared list default with `None` and initialized the list inside the function. |
| Bare exception handler | Removed broad exception suppression and explicitly checked whether a parking slot exists. |
| Unsafe `eval()` usage | Replaced arbitrary expression evaluation with direct arithmetic using a surge multiplier. |
| Weak MD5 hashing | Replaced MD5 with SHA-256. |
| Shell command execution | Removed `os.system()` and used Python's `print()` function. |
| Insecure random number generation | Replaced `random.randint()` with `secrets.randbelow()`. |
| Naming and documentation issues | Renamed functions using `snake_case` and added docstrings. |
| Formatting and unused code | Removed unused imports and variables and corrected formatting issues. |

For more details, see [`issues.md`](issues.md).

## Final Analysis Results

| Tool | Final Result |
|---|---|
| Pylint | **10.00/10** |
| Bandit | **0 issues identified** |
| Flake8 | **0 violations reported** |

The program was executed after the changes to verify that its demonstrated functionality continued to work.

The before-and-after report files are included in the repository for comparison.

## Reflection

This lab demonstrated how different static analysis tools complement one another:

- Pylint helps improve code quality and maintainability.
- Bandit helps identify potentially insecure coding patterns.
- Flake8 enforces consistent formatting and style.

Using these tools together makes code easier to review and maintain. Static analysis complements, but does not replace, functional testing and security review.

See [`reflection.md`](reflection.md) for the lab reflection.

## Learning Outcomes

- Understand the purpose of static code analysis.
- Identify and fix common Python programming issues.
- Use Pylint, Bandit, and Flake8 to analyze source code.
- Interpret analysis reports and prioritize findings.
- Verify improvements through repeated analysis and program execution.

---

**Lab:** 5 — Static Code Analysis  
**Program:** Parking Lot System  
**Status:** Completed
