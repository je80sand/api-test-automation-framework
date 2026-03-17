# API Test Automation Framework

![CI](https://github.com/je80sand/api-test-automation-framework/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.14-blue)
![Pytest](https://img.shields.io/badge/testing-pytest-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)
![Allure](https://img.shields.io/badge/reporting-allure-purple)

A scalable **API test automation framework** built with **Python + Pytest** designed for CI pipelines and production-level QA environments.

This framework demonstrates **modern test automation architecture used by SDET teams** and emphasizes:

• maintainability  
• environment portability  
• modular design  
• CI/CD integration  
• scalable test execution  

---

# Key Features

✔ Modular API client abstraction  
✔ Environment-based configuration (`dev`, `stage`, `prod`)  
✔ Test suite segmentation (`smoke`, `regression`, `api`)  
✔ Parallel test execution with `pytest-xdist`  
✔ CI integration via GitHub Actions  
✔ Allure reporting for test analytics  
✔ Makefile automation commands  
✔ Structured project architecture  

---

# Framework Architecture

```
api-test-automation-framework
│
├── .github/workflows
│ └── ci.yml # CI pipeline
│
├── config
│ └── settings.py # environment configuration
│
├── data
│ └── users_payloads.py # test data payloads
│
├── schemas
│ └── login_schema.py # response validation schemas
│
├── src
│ ├── api
│ │ ├── api_client.py # reusable HTTP client
│ │ ├── endpoints.py # endpoint definitions
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
├── conftest.py # fixtures + environment loader
├── pytest.ini # pytest configuration
├── Makefile # automation shortcuts
├── requirements.txt
└── README.md
```

---

# Design Principles

This framework follows several key automation engineering principles.

### Test Isolation
Each test is independent and does not rely on execution order.

### API Client Abstraction
All HTTP interactions are routed through a reusable client to ensure:

• consistent request handling  
• centralized headers  
• easier authentication handling  
• logging and debugging capability

### Environment Configuration
Environment variables are separated from code using `.env` files.

This allows tests to run against:

```
dev
stage
prod
```

without code modification.

### Test Suite Segmentation

Tests are categorized for CI pipeline efficiency.

| Marker | Purpose |
|------|------|
| smoke | quick validation checks |
| regression | deeper validation |
| api | all API tests |

---

# Installation

Clone the repository.

```bash
git clone https://github.com/je80sand/api-test-automation-framework.git
cd api-test-automation-framework
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

# Running Tests

Run the entire suite.

```bash
pytest -v
```

---

# Test Suite Execution

Run smoke tests:

```bash
pytest -v -m smoke
```

Run regression tests:

```bash
pytest -v -m regression
```

Run all API tests:

```bash
pytest -v -m api
```

---

# Environment Switching

Tests can run against different environments.

Example:

```bash
pytest -v --env=dev
```

Example running smoke tests against staging:

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

Run tests concurrently using `pytest-xdist`.

```bash
pytest -n 2
```

Parallel execution significantly reduces pipeline execution time in CI environments.

---

# Makefile Commands

The Makefile provides simple command shortcuts.

Run smoke tests:

```bash
make smoke
```

Run regression tests:

```bash
make regression
```

Run full API suite:

```bash
make api-suite
```

Run tests in parallel:

```bash
make parallel-test
```

Generate HTML report:

```bash
make report
```

Generate Allure report:

```bash
make allure
make allure-report
make allure-open
```

Clean artifacts:

```bash
make clean
```

---

# Allure Reporting

Generate Allure results.

```bash
pytest --alluredir=allure-results
```

Generate report.

```bash
allure generate allure-results -o allure-report --clean
```

Open report.

```bash
allure open allure-report
```

Allure provides:

• execution history  
• step-level reporting  
• test analytics  
• failure debugging  

---

# Continuous Integration

GitHub Actions automatically executes tests on every push.

Pipeline stages:

1. Install dependencies
2. Execute test suite
3. Validate build status

CI workflow location:

```
.github/workflows/ci.yml
```

---

# Example Output

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

# Future Enhancements

Potential improvements include:

• API schema validation using Pydantic  
• request/response logging middleware  
• flaky test retry handling  
• coverage reporting  
• test data factories  
• Dockerized execution  

---

## 📊 Logging

All API requests and responses are logged to:

logs/test_run.log

Includes:
- HTTP method and endpoint
- Request headers and payload
- Response status codes
- Response body

This enables debugging and traceability similar to real-world QA environments.

---

# Author

Jose Sandoval  
Automation Engineer | Python Developer