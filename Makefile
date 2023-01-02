test: FORCE
	pytest

prep:
	pip install pytest pytest-cov
	python3 -m pip install --upgrade build
	python3 -m pip install --upgrade twine

cov:
	pytest --cov-report term-missing --cov=kinneyotp test/

build: test
	rm -rf dist/
	python -m build . --wheel

release: build
	python3 -m twine upload dist/*

clean:
	rm -rf build/ dist/ .coverage __pycache__/ kinneyotp.egg-info/ .pytest_cache/ test/__pycache__

FORCE: ;
