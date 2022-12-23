lint:
	poetry run flake8 page_loader
test:
	poetry run pytest -vv
test-coverage:
	poetry run pytest --cov=page_loader --cov-report xml tests/
restart: install build package-reinstall
install:
	poetry install
build:
	poetry build
package-reinstall:
	python3 -m pip install --force-reinstal dist/*.whl
package-install:
	python3 -m pip install --user dist/*.whl