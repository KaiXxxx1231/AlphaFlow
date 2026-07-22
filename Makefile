.PHONY: dev test lint

dev:
	docker compose up

test:
	pytest backend/tests

lint:
	python -m compileall backend/app
