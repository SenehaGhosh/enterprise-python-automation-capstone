# Enterprise Python Automation Capstone Project

An end-to-end Python automation application that integrates external REST APIs, processes market intelligence data, and generates formatted PDF reports on-demand or via automated background scheduling.

---

## Architecture Overview

```text
[ CoinGecko API ] ──( HTTP GET )──> [ api_client.py ]
                                           │
                                     ( Raw JSON Data )
                                           ▼
[ User CLI / Scheduler ] ──( Click )──> [ pdf_generator.py ] ──> [ PDF Report ]
## Features
- Real-time API data fetching with structured error handling.
- PDF generation using `reportlab` with customized table styles.
- Command Line Interface (CLI) built with `click`.
- Automated recurring task execution via `schedule`.
- Standard Python packaging setup via `pyproject.toml`.

## Installation & Setup
```bash
pip install .