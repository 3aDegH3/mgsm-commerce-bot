.PHONY: help build up down restart ps logs logs-api pull config \
	api-shell django-check migrate makemigrations db-shell redis-cli reset

help:
	@echo "Available commands:"
	@echo "  make build           Build Docker images"
	@echo "  make up              Start development services"
	@echo "  make down            Stop development services"
	@echo "  make restart         Restart development services"
	@echo "  make ps              Show service status"
	@echo "  make logs            Follow all service logs"
	@echo "  make logs-api        Follow Django logs"
	@echo "  make pull            Pull service images"
	@echo "  make config          Validate compose configuration"
	@echo "  make api-shell       Open shell in Django container"
	@echo "  make django-check    Run Django system checks"
	@echo "  make migrate         Apply Django migrations"
	@echo "  make makemigrations  Create Django migrations"
	@echo "  make db-shell        Open PostgreSQL shell"
	@echo "  make redis-cli       Open Redis CLI"
	@echo "  make reset           Remove containers and local data"

build:
	docker compose build

up:
	docker compose up -d --build

down:
	docker compose down

restart:
	docker compose restart

ps:
	docker compose ps

logs:
	docker compose logs -f

logs-api:
	docker compose logs -f core-api

pull:
	docker compose pull

config:
	docker compose config

api-shell:
	docker compose exec core-api sh

django-check:
	docker compose exec core-api python manage.py check

migrate:
	docker compose exec core-api python manage.py migrate

makemigrations:
	docker compose exec core-api python manage.py makemigrations

db-shell:
	docker compose exec postgres sh -c 'psql -U "$$POSTGRES_USER" -d "$$POSTGRES_DB"'

redis-cli:
	docker compose exec redis redis-cli

reset:
	docker compose down --volumes --remove-orphans
