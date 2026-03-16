# API Test Automation Framework

![CI](https://github.com/je80sand/api-test-automation-framework/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.14-blue)
![Pytest](https://img.shields.io/badge/testing-pytest-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)
![Allure](https://img.shields.io/badge/reporting-allure-purple)

A scalable **API automation testing framework** built with **Python and Pytest**.

This project demonstrates modern QA automation architecture used by SDET teams including:

• API client abstraction  
• Environment switching (dev / stage / prod)  
• Test suite segmentation (smoke / regression / api)  
• CI integration with GitHub Actions  
• Parallel execution  
• Allure reporting  
• Makefile automation commands  

---

# Project Architecture

```
api-test-automation-framework
│
├── .github/workflows
│ └── ci.yml
│
├── config
│ └── settings.py
│
├── data
│ └── users_payloads.py
│
├── schemas
│ └── login_schema.py
│
├── src
│ ├── api
│ │ ├── api_client.py
│ │ ├── endpoints.py
│ │ └── response_validator.py
│ │
│ └── utils
│ ├── helpers.py
│ └── logger.py
│
├── tests
│ ├── test_health.py
│ └── test_users.py
│
├── .env.dev
├── .env.stage
├── .env.prod
│
├── conftest.py
├── pytest.ini
├── Makefile
├── requirements.txt
└── README.md
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/je80sand/api-test-automation-framework.git
cd api-test-automation-framework
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Running Tests

Run all tests

```bash
pytest -v
```

---

# Test Suites

This framework supports **test suite levels** used in CI pipelines.

### Smoke Tests

Quick health checks used for fast validation.

```bash
pytest -v -m smoke
```

---

### Regression Tests

Full validation suite.

```bash
pytest -v -m regression
```

---

### API Tests

Runs all API test cases.

```bash
pytest -v -m api
```

---

# Environment Switching

Tests can run against multiple environments.

Available environments

```
dev
stage
prod
```

Run tests in a specific environment:

```bash
pytest -v --env=dev
```

Example

```bash
pytest -v -m smoke --env=stage
```

Environment variables are loaded from:

```
.env.dev
.env.stage
.env.prod
```

---

# Parallel Execution

Run tests in parallel using **pytest-xdist**.

```bash
pytest -n 2
```

---

# Makefile Commands

Common commands can be executed using Make.

Run smoke tests

```bash
make smoke
```

Run regression tests

```bash
make regression
```

Run all API tests

```bash
make api-suite
```

Run tests in parallel

```bash
make parallel-test
```

Generate HTML report

```bash
make report
```

Generate Allure report

```bash
make allure
make allure-report
make allure-open
```

Clean test artifacts

```bash
make clean
```

---

# Allure Reporting

Generate test results

```bash
pytest --alluredir=allure-results
```

Generate report

```bash
allure generate allure-results -o allure-report --clean
```

Open report

```bash
allure open allure-report
```

Allure provides:

• test history  
• step tracing  
• screenshots  
• attachments  
• failure debugging  

---

# Continuous Integration

GitHub Actions automatically runs tests on every push.

Pipeline steps:

1. Install dependencies  
2. Run pytest  
3. Generate reports  
4. Validate build status  

CI configuration located at:

```
.github/workflows/ci.yml
```

---

# Technologies Used

Python  
Pytest  
Requests  
Allure Reporting  
pytest-xdist  
GitHub Actions  

---

# Example Test Output

```
tests/test_health.py::test_api_health_check PASSED
tests/test_users.py::test_get_users_list PASSED
tests/test_users.py::test_get_single_user PASSED
tests/test_users.py::test_create_user PASSED
tests/test_users.py::test_update_user PASSED
tests/test_users.py::test_delete_user PASSED

6 passed in 1.05s
```

---

# Author

Jose Sandoval

Python Developer | Automation Engineer