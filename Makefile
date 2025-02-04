
# Command to show help
APP_NAME = Landbot Backend Challengue
HELP = Show this help.
START = Start the application with uvicorn.
UP = Start the application with docker.
DOWN = Down the docker service.
RM = Remove containers.
LINT = Check code style with flake8.
FORMAT = Format code with black.
TEST = Run unit tests.

define MENU

$(APP_NAME)
====================

Available commands:
  make help    - $(HELP)
  make start   - $(START)
  make up      - $(UP)
  make down    - $(DOWN)
  make rm      - $(RM)
  make lint    - $(LINT)
  make format  - $(FORMAT)
  make test    - $(TEST)

endef
export MENU

help:
	@echo "$$MENU"

# Command to start the application
start:
	@echo $(START)
	poetry install --no-root --no-interaction --no-ansi
	poetry run python3 manage.py runserver

# docker commands
up:
	@echo $(UP)
	docker compose up -d --build

down:
	@echo $(DOWN)
	docker compose stop

rm:
	@echo $(RM)
	docker compose rm --stop -v --force


# Command to check code style with flake8
lint:
	@echo $(LINT)
	poetry run flake8 .

# Command to format code with black
format:
	@echo $(FORMAT)
	poetry run black .

# Command to run unit tests
test:
	@echo "Installing dependencies..."
	poetry install --no-root --no-interaction --no-ansi --with dev
	@echo $(TEST)
	poetry run pytest -vvv tests/
