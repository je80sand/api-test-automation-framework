# API Test Automation Framework

[![CI](https://github.com/je80sand/api-test-automation-framework/actions/workflows/ci.yml/badge.svg)](https://github.com/je80sand/api-test-automation-framework/actions)

A scalable, production-style API test automation framework built with **Python, Pytest, and Requests**, designed with **senior-level QA engineering practices**.

---

## 🚀 Features

- ✅ Pytest-based test framework  
- ✅ Environment switching (dev / stage / prod)  
- ✅ API client abstraction layer  
- ✅ JSON schema validation (centralized)  
- ✅ Request/response logging system  
- ✅ Dynamic test data generation  
- ✅ Test categorization (smoke, regression)  
- ✅ CLI test runner (`run_tests.py`)  
- ✅ Allure reporting integration  
- ✅ Code coverage reporting  
- ✅ CI/CD with GitHub Actions  

---

## 🏗️ Project Structure

```
api-test-automation-framework/
│
├── src/
│ ├── api/
│ │ ├── api_client.py
│ │ ├── endpoints.py
│ │ └── response_validator.py
│ │
│ ├── utils/
│ │ ├── helpers.py
│ │ ├── logger.py
│ │ └── data_factory.py
│
├── schemas/
│ ├── user_schema.py
│ └── users_list_schema.py
│
├── tests/
│ ├── test_users.py
│ └── test_health.py
│
├── run_tests.py
├── pytest.ini
├── Makefile
└── requirements.txt
```

---

## ⚙️ Setup

```bash
git clone https://github.com/je80sand/api-test-automation-framework.git
cd api-test-automation-framework

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

---

## ▶️ Running Tests

### Run all tests

```bash
pytest -v --env=dev
```

### Run smoke tests

```bash
pytest -v -m smoke --env=dev
```

### Run via CLI

```bash
python3 run_tests.py --env dev --suite smoke
```

---

## 📊 Coverage

```bash
make coverage
```

---

## 📈 Allure Reports

```bash
pytest --alluredir=allure-results
allure serve allure-results
```

---

## 🔄 CI/CD

- GitHub Actions pipeline runs on:
  - push to `main`
  - pull requests

Pipeline includes:
- smoke test execution  
- coverage report generation  
- Allure artifact upload  

---

## 🧠 Design Highlights

- **Separation of concerns**
  - API logic separated from test logic  
- **Reusable API client**  
- **Centralized schema validation**  
- **Extensible architecture for scaling tests**  
- **Clean logging for debugging failures**  

---

## 👨‍💻 Author

**Jose Sandoval**  
Python Automation | QA Engineering | API Testing