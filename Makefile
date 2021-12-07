all: clean-pyc test

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

lines:
	find . -name "*.py"|xargs cat|wc -l

test:
	@pytest -vv --tb=short -x --ds=tests.settings tests --nomigrations --cov-config=./.coveragec --cov

flake8:
	@flake8 django_ddd_framework tests

test-cov:
	coverage erase
	@pytest -vv --tb=short -x --ds=tests.settings tests --nomigrations --cov-config=./.coveragec --cov-report html --cov-fail-under=95 --cov
