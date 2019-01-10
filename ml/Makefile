.PHONY clean clean-cache

PROJECT ?= ml

COVERAGE_DIR := htmlcov
COVERAGE_REPORT := $(COVERAGE_DIR)/index.html
PYTEST_ARGS := --flakes --pep8 --pylint -s -vv --cov-report term-missing


clean clean-cache:
	cd .. && make clean-cache


############################################################
# sub-projects Makefile redirection
############################################################
classifier-prediction cpr:
	cd classifier && make prediction
	@echo “- DONE: $@”

classifier-training ctr:
	cd classifier && make training
	@echo “- DONE: $@”
