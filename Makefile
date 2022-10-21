lint:
	poetry run flake8
test:
	poetry run pytest
test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml
restart: install build package-install
install:
	poetry install
build:
	poetry build
package-reinstall:
	python3 -m pip install --force-reinstal dist/*.whl
package-install:
	python3 -m pip install --user dist/*.whl