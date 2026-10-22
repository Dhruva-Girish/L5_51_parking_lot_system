# Lab 5 — Static Code Analysis: Reflection

### 1. What did you learn about static code analysis?

Static code analysis examines source code without executing it to identify potential bugs, security vulnerabilities, and coding-standard violations. Using Pylint, Bandit, and Flake8 demonstrated that different tools detect different categories of problems and complement one another.

### 2. Which issues were the most important, and why?

The most important issues were the use of `eval()`, shell command execution through `os.system()`, and weak MD5 hashing. These patterns can create security risks when used in inappropriate contexts. The mutable default argument and broad exception handler were also important because they could cause unexpected behavior and make debugging difficult.

### 3. How did you verify that your fixes worked?

I ran the parking lot program after making the changes to check that it still produced the expected output. I then reran Pylint, Bandit, and Flake8. The final Pylint score was 10.00/10, Bandit reported no issues, and Flake8 produced no violations.

### 4. How do static analysis tools contribute to code quality and maintainability?

Pylint helps identify code-quality problems and questionable programming practices. Bandit focuses on common security risks, while Flake8 detects formatting and style violations. Using all three makes code easier to review, maintain, and improve. However, static analysis does not replace functional testing or a thorough security review.
