VENV_PATH := .venv/bin/activate
PYTHON := python3

.PHONY: help venv run

help:
	@echo " Available Commands:"
	@echo " venv         - Creates and activates the virtual environment and installs dependencies"
	@echo " run          - Starts the FastAPI application"

venv:
	@echo " Checking for virtual environment..."
	@if [ ! -d .venv ]; then \
		echo " Creating virtual environment..."; \
		$(PYTHON) -m venv .venv; \
	fi
	@echo " Installing dependencies..."
	@.venv/bin/pip install --upgrade pip
	@.venv/bin/pip install -r requirements.txt
	@echo " Virtual environment ready!"

run:
	@echo " > Running FastAPI application..."
	@PYTHONPATH=. .venv/bin/uvicorn src.app.main:app --reload
