test: FORCE
	pytest

cov:
	pytest --cov-report term-missing --cov=src test/

build: test
	rm -rf dist/
	python3 -m build

release: build
	python3 -m twine upload dist/*

FORCE: ;
