# AGENTS.md — Mailroom Live

> Everything an AI coding agent (or a returning human) needs to know about this project.

## What Is This Project?

**Mailroom Live** is a command-line mailroom management system built in Python.
It tracks packages, letters, and deliveries for a building or office — who they are for,
when they arrived, whether they have been picked up, and basic statistics.

We are building it **incrementally** as a vehicle for learning programming fundamentals,
following the PRIMMAI curriculum at:
<https://agentfactory.panaversity.org/building-ai-workers/programming-fundamentals/>

## Curriculum Progress

We have covered **through Lesson 13.7**. The concepts available to us so far:

| Lesson | Title | Key Concepts |
|--------|-------|-------------- |
| 13.1 | You read, the agent writes | Reading agent-written code; predict-before-you-run; five steps for reading code |
| 13.2 | The workbench | Tests, type checker, linter; strict mode; understanding commands the agent runs |
| 13.3 | Values, types and variables | Variables in Python; value types (str, int, float, bool); text ≠ number; money in whole cents |
| 13.4 | Decisions and repetition | `if`/`elif`/`else`; `for` loops; stating logic as a sentence |
| 13.5 | Two conditions, empty values, while loops | `and`/`or`; `None` and empty values; `while` loop termination |
| 13.6 | Functions: the signature is the contract | Function signatures; return types; testing with one hand-checkable assertion |
| 13.7 | Lists and dictionaries | Lists, dicts, records (typed dicts); missing-key handling; sorting |

### What We May NOT Use Yet

- File I/O (Lesson 13.8)
- Date/time handling (Lesson 13.9)
- Error handling / try-except (Lesson 13.10)
- Test-driven development loop (Lesson 13.11)
- Advanced judgment / design patterns (Lesson 13.12+)

If a feature needs a concept from a later lesson, **teach the concept first** before writing the code.

## Project Structure

```
mailroom-live/
  main.py          # Entry point
  pyproject.toml   # Project config (uv / PEP 621)
  README.md        # User-facing readme
  AGENTS.md        # This file — project knowledge for agents
  .python-version  # Pinned Python version (3.14)
```

## Tech Stack

- **Language:** Python 3.14
- **Package manager:** uv
- **No external dependencies yet** — standard library only

## Conventions

1. **Every number comes from a tested function** (Lesson 13.6 rule).
2. **Predict before you run** — when showing new code, ask: "What do you think this prints?"
3. **Money is stored in whole cents** (integers), not floats (Lesson 13.3 rule).
4. **Use type hints** on every function signature — the signature is the contract.
5. **Keep functions small** — each does one thing and can be described in one sentence.
6. **Use `if __name__ == "__main__":`** to guard the entry point.

## Commands

```bash
# Run the project
uv run main.py

# Add a dependency (when needed later)
uv add <package-name>

# Run tests (when we add them)
uv run pytest
```

## Learning Approach

- We follow the PRIMMAI curriculum lesson by lesson.
- When a new concept is needed, the agent teaches it with a small example first,
  then applies it to the mailroom project.
- Code is written to be **readable** — clarity over cleverness.
- Every new feature gets at least one assertion or test to verify it works.
