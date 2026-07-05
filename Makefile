.PHONY: help up down restart ps logs pull config db-shell redis-cli reset

help:
	@echo "Available commands:"
	@echo "  make up          Start development services"
	@echo "  make down        Stop development services"
	@echo "  make restart     Restart development services"
	@echo "  make ps          Show service status"
	@echo "  make logs        Follow service logs"
	@echo "  make pull        Pull service images"
	@echo "  make config      Validate compose configuration"
	@echo "  make db-shell    Open PostgreSQL shell"
	@echo "  make redis-cli   Open Redis CLI"
	@echo "  make reset       Remove containers and local data"

up:
	docker compose up -d

down:
	docker compose down

restart:
	docker compose restart

ps:
	docker compose ps

logs:
	docker compose logs -f

pull:
	docker compose pull

config:
	docker compose config

db-shell:
	docker compose exec postgres sh -c 'psql -U "$$POSTGRES_USER" -d "$$POSTGRES_DB"'

redis-cli:
	docker compose exec redis redis-cli

reset:
	docker compose down --volumes --remove-orphans
