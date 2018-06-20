.PHONY: clean clean-test clean-pyc clean-build clean-venv check-venv install-venv develop-venv help test test-all
.DEFAULT_GOAL := help

SHELL := /bin/bash
export VIRTUALENVWRAPPER_PYTHON := /usr/bin/python

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

check-venv: ## verify that the user is running in a Python virtual environment
	@if [ -z "$(VIRTUALENVWRAPPER_SCRIPT)" ]; then echo 'Python virtualenvwrapper not installed!' && exit 1; fi
	@if [ -z "$(VIRTUAL_ENV)" ]; then echo 'Not running within a virtual environment!' && exit 1; fi

clean: clean-test clean-pyc clean-build   ## remove all build, test, coverage, artifacts and wipe virtualenv

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/

clean-venv: check-venv ## remove all packages from current virtual environment
	@source virtualenvwrapper.sh && wipeenv || echo "Skipping wipe of environment"

test: ## run tests quickly with the default Python
	python -m unittest discover -s test

test-all: ## run tests on every Python version with tox
	tox

dist: clean ## builds source and wheel package
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l dist

install: clean ## install the package to the active Python's site-packages
	python setup.py install

install-editable: ## install the package in editable mode
	if pip list -e | grep 'rpc-qtest-swagger-client'; then echo 'Editable package already installed'; else pip install -e .; fi

install-venv: clean-venv install ## install the package after wiping the vitual environment

develop: clean ## install necessary packages to setup a dev environment
	pip install -r requirements.txt -r test-requirements.txt

develop-venv: clean-venv develop ## setup a dev environment after wiping the virtual environment

publish: ## publish package to PyPI
	twine upload dist/*.whl

build: ## build a wheel
	python setup.py bdist_wheel

bump-major: ## bumps the version of by major
	bumpversion major

bump-minor: ## bumps the version of by minor
	bumpversion minor

bump-patch: ## bumps the version of by patch
	bumpversion patch

release-major: clean-build build develop bump-major test publish ## package and upload a major release
	echo 'Successfully released!'
	echo 'Please push the newly created tag and commit to GitHub.'

release-minor: clean-build build develop bump-minor test publish ## package and upload a minor release
	echo 'Successfully released!'
	echo 'Please push the newly created tag and commit to GitHub.'

release-patch: clean-build build develop bump-patch test publish ## package and upload a patch release
	echo 'Successfully released!'
	echo 'Please push the newly created tag and commit to GitHub.'
