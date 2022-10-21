lint:
	poetry run flake8
test:
	poetry run pytest
test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml
b:
	poetry build
package-install:
	python3 -m pip install --user dist/*.whl