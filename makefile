run:
	uv run fastapi dev --reload

check:
	uv run ruff check --fix .

format:
	uv run ruff format .
