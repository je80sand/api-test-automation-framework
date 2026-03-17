install:
	pip install -r requirements.txt

test:
	pytest -v --env=dev

smoke:
	pytest -v -m smoke --env=dev

regression:
	pytest -v -m regression --env=dev

api-suite:
	pytest -v -m api --env=dev

parallel-test:
	pytest -n 2 -v --env=dev

report:
	pytest -v --html=report.html --env=dev

allure:
	pytest --alluredir=allure-results --env=dev

allure-report:
	allure generate allure-results -o allure-report --clean

allure-open:
	allure open allure-report

clean:
	rm -rf __pycache__
	rm -rf .pytest_cache
	rm -rf report.html
	rm -rf reports
	rm -rf allure-results
	rm -rf allure-report
	rm -rf htmlcov
	rm -rf .coverage
	rm -rf coverage.xml

coverage:
	pytest -v --cov=src --cov-report=term-missing --cov-report=xml --env=dev

coverage-html:
	pytest -v --cov=src --cov-report=html --cov-report=term-missing --env=dev