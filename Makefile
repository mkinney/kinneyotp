test:
	pytest

cov:
	pytest --cov-report term-missing --cov=otp --cov=key tests/
