.PHONY: clean clean-cache

PROJECT ?= ml

COVERAGE_DIR := htmlcov
COVERAGE_REPORT := $(COVERAGE_DIR)/index.html
PYTEST_ARGS := --flakes --pep8 --pylint -s -vv --cov-report term-missing
PYVENV_MAKE := ../tools/make_venv.sh
PYVENV_NAME ?= .venv


clean clean-cache:
	cd .. && make clean-cache


# setup and dev-setup targets
dev-setup-venv: requirements-dev.txt
	cd .. && make dev-setup-venv
	@echo "- DONE: $@"

dev-setup: dev-setup-venv
	@echo "----------------------------------------------------------------------"
	@echo "Python environment: ../$(PYVENV_NAME)"
	@echo "- Activate command: source ../$(PYVENV_NAME)/bin/activate"
	@echo


############################################################
# sub-projects Makefile redirection
############################################################
classifier-prediction cpr:
	cd classifier && make prediction
	@echo “- DONE: $@”

classifier-training ctr:
	cd classifier && make training
	@echo “- DONE: $@”
