# Makefile for Django application

# Variables
VENV = venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip
MANAGE = $(PYTHON) manage.py

# Default target
all: run

# Create a virtual environment
venv:
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

# Run the development server
run:
	$(MANAGE) runserver

# Run tests
test:
	$(MANAGE) test

# Run migrations
migrate:
	$(MANAGE) makemigrations
	$(MANAGE) migrate

# Create a superuser
createsuperuser:
	$(MANAGE) createsuperuser

# Collect static files
collectstatic:
	$(MANAGE) collectstatic --noinput

# Run the application in production mode using gunicorn
prod:
	gunicorn --workers 3 your_project_name.wsgi:application --bind 0.0.0.0:8000

# Clean up the virtual environment
clean:
	rm -rf $(VENV)
	find . -type d -name "__pycache__" -exec rm -rf {} +

# Docker commands
docker-build:
	docker-compose build

docker-up:
	docker-compose up

docker-down:
	docker-compose down

docker-logs:
	docker-compose logs -f

# Help command
help:
	@echo "Available commands:"
	@echo "  make venv         - Create a virtual environment and install dependencies"
	@echo "  make run          - Run the development server"
	@echo "  make test         - Run tests"
	@echo "  make migrate      - Run migrations"
	@echo "  make createsuperuser - Create a superuser"
	@echo "  make collectstatic - Collect static files"
	@echo "  make prod         - Run the application in production mode using gunicorn"
	@echo "  make clean        - Clean up the virtual environment and pycache"
	@echo "  make docker-build - Build Docker containers"
	@echo "  make docker-up    - Start Docker containers"
	@echo "  make docker-down  - Stop Docker containers"
	@echo "  make docker-logs  - View Docker container logs"
	@echo "  make help         - Show this help message"

.PHONY: all venv run test migrate createsuperuser collectstatic prod clean docker-build docker-up docker-down docker-logs help