init:
	pip install -r requirements.txt

test:
	pytest

coverage:
	pytest --cov=yama tests/
