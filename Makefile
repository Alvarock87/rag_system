setup:
	uv venv
	uv sync --all-groups

lint:
	uv run ruff check .

format:
	uv run ruff format .

type:
	uv run mypy app/

test:
	uv run pytest

run:
	uv run python main.py

api:
	uv run uvicorn app.api.main:app --reload

precommit:
	pre-commit run --all-files