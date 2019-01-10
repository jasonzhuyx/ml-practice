.PHONY: clean clean-cache

PROJECT ?= ml

COVERAGE_DIR := htmlcov
COVERAGE_REPORT := $(COVERAGE_DIR)/index.html
PYTEST_ARGS := --flakes --pep8 --pylint -s -vv --cov-report term-missing


clean clean-cache:
	@echo
	@echo “--- Removing pyc and log files”
	find . -name ‘.DS_Store’ -type f -delete
	find . -name \*.pyc -type f -delete -o -name \*.log -delete
	rm -Rf .cache
	rm -Rf .vscode
	rm -Rf $(PROJECT)/.cache
	rm -Rf $(PROJECT)/__pycache__
	rm -Rf $(PROJECT)/tests/__pycache__
	@echo
	@echo “--- Removing coverage files”
	find . -name ‘.coverage’ -type f -delete
	rm -rf .coveragerc
	rm -rf cover
	rm -rf $(PROJECT)/cover
	rm -Rf $(PROJECT)/$(COVERAGE_DIR)
	rm -Rf $(COVERAGE_DIR)
	@echo
	@echo “--- Removing *.egg-info”
	rm -Rf *.egg-info
	rm -Rf $(PROJECT)/*.egg-info
	@echo
	@echo “--- Removing tox virtualenv”
	rm -Rf $(PROJECT)/.tox*
	@echo
	@echo “--- Removing build”
	rm -rf $(PROJECT)_build.tee
	@echo
	@echo “- DONE: $@”


############################################################
# sub-projects Makefile redirection
############################################################
classifier-prediction cpr:
	cd ml/classifier && make prediction
	@echo “- DONE: $@”

classifier-training ctr:
	cd ml/classifier && make training
	@echo “- DONE: $@”
