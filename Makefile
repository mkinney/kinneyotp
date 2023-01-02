test: FORCE
	pytest

cov:
	pytest --cov-report term-missing --cov=kinneyotp test/

build: test
	rm -rf dist/
	python -m build . --wheel

release: build
	python3 -m twine upload dist/*

FORCE: ;
