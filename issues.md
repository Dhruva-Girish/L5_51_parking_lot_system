# Lab 5 — Static Code Analysis: Issue Log

| Issue | Type | Original line(s) | Description | Fix Approach |
|---|---|---:|---|---|
| Mutable default argument | Code quality / Bug | 15 | `entry_logs=[]` reused the same list across function calls, potentially sharing log entries unexpectedly. | Changed the default to `None` and initialized a new list inside the function. |
| Bare exception | Code quality / Bug | 32–33 | A bare `except` with `pass` silently suppressed all exceptions, making errors difficult to diagnose. | Added an explicit slot-existence check and removed the broad exception handler. |
| Unsafe `eval()` | Security | 48 | `eval(surge_expr)` executed a supplied expression, creating a risk of arbitrary code execution. | Replaced expression evaluation with a numeric surge multiplier and direct arithmetic. |
| Weak MD5 hashing | Security | 53 | MD5 is unsuitable when collision resistance is required for security-sensitive hashing. | Replaced MD5 with SHA-256 using `hashlib.sha256()`. |
| Shell command execution | Security | 64 | `os.system()` invoked a shell to display a message, creating an unnecessary command-injection risk. | Removed shell execution and used Python's `print()` function instead. |
| Insecure PIN generation | Security | 57 | `random.randint()` is not designed for security-sensitive random values. | Replaced it with `secrets.randbelow()` to generate a four-digit PIN. |
| Missing function docstrings and naming violations | Code quality | Multiple | Functions lacked documentation and used camelCase names rather than Python's snake_case convention. | Added docstrings and renamed functions to use snake_case. |
| Formatting and unused code | Style / Code quality | Multiple | The original file contained long lines, an unused import, unused variables, and a missing final newline. | Removed unused code, formatted expressions, and corrected the file's formatting. |

## Verification Results

- **Pylint:** 10.00/10.
- **Bandit:** No issues identified.
- **Flake8:** No violations reported.
- **Program execution:** Successful after the changes.

The three static analysis tools were rerun after the fixes to verify the results.
