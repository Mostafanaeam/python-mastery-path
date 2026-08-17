# Python Mastery Path

A personal, practical Python learning and software-engineering repository — from fundamentals to problem solving, automation, and project work — with the long-term goal of building the technical foundation needed for Master's-level study.

The learning source is a ~160-lesson Python playlist. This repository is organized around **concepts, not videos**: the videos are the learning source, the repository is the engineering evidence.

## Why I Am Learning Python

Write your own motivation here: why Python, what you want to build with it, and what "mastery" means to you.

## Learning Philosophy

This repository reflects **real** learning only:

- No copied solutions, no fake progress, no invented results.
- Understand before moving on — be able to *explain* it in writing.
- Mistakes are evidence: log them, find the root cause, learn the lesson.
- Every topic follows the same cycle:

```text
Learn
↓
Implement
↓
Practice
↓
Break
↓
Debug
↓
Explain
↓
Document
↓
Repeat
```

## Repository Structure

```text
python-mastery-path/
│
├── 01_basics/          Topic-by-topic basics (variables → functions)
├── 02_problem_solving/ LeetCode / HackerRank / Codewars problems
├── 03_projects/        mini/ and major/ projects
├── 04_automation/      scripts/ for daily tasks, experiments/
├── 05_notes/           mistakes, debugging, questions, summaries, concepts
├── .gitignore
├── README.md
└── requirements.txt
```

## Learning Roadmap

The ~160 lessons map onto concepts. Topics beyond the basics live as notes in `05_notes/concepts/` until they grow into their own area.

| Concept (curriculum) | Where it lives in this repo |
|----------------------|-----------------------------|
| Fundamentals, Variables, Data Types, Strings, Lists, Tuples, Sets, Dictionaries, Booleans, Operators, Type Conversion, User Input, Control Flow, Loops, Functions | `01_basics/01_variables` … `01_basics/14_functions` |
| Scope, Recursion, Lambda, Files, Built-in Functions, Modules, Date & Time, Iterators, Generators, Decorators, Debugging, Type Hinting, Regular Expressions, OOP, `__name__`/`__main__`, Timing, Logging | `05_notes/concepts/` — one note per concept |
| Unit Testing, Databases, SQLite | `05_notes/concepts/` + practice in `03_projects/` |
| Flask | `03_projects/` |
| Web Scraping | `04_automation/experiments/` → `03_projects/` |
| NumPy | `05_notes/concepts/` + `04_automation/experiments/` |
| Virtual Environments | documented in this README |
| Practical projects | `03_projects/` |
| Problem solving | `02_problem_solving/` |

## Problem-Solving Approach

Every problem gets its own folder with three files:

```text
problem-name/
├── solution.py
├── tests.py
└── README.md
```

- Solve on your own first; write down your first attempt even if it is wrong.
- Write tests and run them before claiming success.
- Record time/space complexity and edge cases honestly.
- No copied solutions. If you later study a known solution, note what you learned from it.
- Copy the template from `02_problem_solving/_template/`.

## Projects

- `03_projects/mini/` — small, single-file projects that practice a concept cluster.
- `03_projects/major/` — larger, multi-file projects with modules, tests, and docs.

## Automation

- `04_automation/scripts/` — real scripts for real, repeated tasks.
- `04_automation/experiments/` — quick explorations of libraries and ideas (messy allowed, but annotated).

## Notes

- `05_notes/mistakes.md` — long-term mistakes journal (root cause + lesson).
- `05_notes/debugging.md` — debugging session journal (symptom → root cause → prevention).
- `05_notes/questions.md` — open and answered questions.
- `05_notes/summaries.md` — topic summaries in your own words (the "Explain" step).
- `05_notes/concepts/` — one note per advanced concept.

## Environment Setup

Requires Python 3.x.

```bash
python --version
```

Create a virtual environment (recommended):

```bash
python -m venv .venv
```

Activate it (PowerShell):

```powershell
.venv\Scripts\Activate.ps1
```

Activate it (Command Prompt):

```cmd
.venv\Scripts\activate.bat
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## How to Run Python Files

```bash
python path/to/file.py
```

Examples:

```bash
python 01_basics/01_variables/examples.py
python 02_problem_solving/two-sum/tests.py
```

## Git Workflow

Recommended commit style — short, prefixed, lowercase:

```text
learn: variables and assignment
learn: string indexing and slicing
practice: conditional statements
solve: two sum
fix: handle empty input
docs: update functions notes
refactor: simplify calculator implementation
test: add edge cases for palindrome
```

Rules: commit often, one idea per commit, never commit secrets, never commit fake progress.

## How to Contribute to My Own Learning

1. Study a topic → write notes in its `README.md`.
2. Write and run your own examples and exercises.
3. Solve problems and record them honestly in `02_problem_solving/`.
4. Log every mistake in `05_notes/mistakes.md`.
5. Log every debugging session in `05_notes/debugging.md`.
6. Keep open questions in `05_notes/questions.md`; answer them as you learn.
7. Summarize each finished topic in `05_notes/summaries.md`.
8. Commit with the prefix style above.

## Progress Tracking

Update this table only when work is genuinely done.

| Area | Status |
|------|--------|
| Python Basics | Not Started |
| Problem Solving | Not Started |
| OOP | Not Started |
| Databases | Not Started |
| Testing | Not Started |
| Automation | Not Started |
| Projects | Not Started |

## 👨‍💻 About The Developer | عن المطور

<div align="center">
  <img src="https://github.com/Mostafanaeam.png" width="100" style="border-radius: 50%" alt="Developer Photo" />

  <br>

  <h3>Mostafa Abd El-naeam</h3>

  <p><strong>Front-End Engineer (Angular & React)</strong></p>

  <p align="center">
    Specializing in modern JavaScript ecosystems with a focus on clean architecture, performance, and premium user experiences. Currently mastering the React ecosystem to build scalable, high-impact front-end systems.
  </p>

  <!-- Social Badges -->

  <a href="https://github.com/Mostafanaeam">
    <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" />
  </a>

  <a href="https://linkedin.com/in/mostafanaeam/">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
  </a>

  <a href="https://mostafa-naeam.vercel.app/">
    <img src="https://img.shields.io/badge/Portfolio-000000?style=for-the-badge&logo=vercel&logoColor=white" alt="Portfolio" />
  </a>

  <a href="mailto:mnaeam10@gmail.com">
    <img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" />
  </a>

  <a href="https://wa.me/201114938410">
    <img src="https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp" />
  </a>
</div>

---

<div align="center">
  Built with ❤️ by <strong>Mostafa</strong> during the Python Mastery Journey
</div>

## 📄 License

This project is licensed under the MIT License.

You are free to use, modify, and distribute the code according to the terms of the license.

See the [LICENSE](LICENSE) file for the complete license text.