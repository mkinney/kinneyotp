test: FORCE
	pytest

cov:
	pytest --cov-report term-missing --cov=src test/

FORCE: ;
