.PHONY: clean clean-cache predict training

PROJECT ?= classifier

COVERAGE_DIR := htmlcov
COVERAGE_REPORT := $(COVERAGE_DIR)/index.html
PYTEST_ARGS := --flakes --pep8 --pylint -s -vv --cov-report term-missing


clean clean-cache:
	cd ../.. && PROJECT=ml/classifier make clean-cache

prediction pr:
	@echo
	PYTHONPATH=../.. python prediction.py
	@echo
	@echo “- DONE: $@”


training tr:
	@echo
	PYTHONPATH=../.. python training.py
	@echo
	@echo “- DONE: $@”
