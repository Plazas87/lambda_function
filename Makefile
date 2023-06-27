-include .env
export

.SILENT:

# Extract arguments of the subcommand
.PHONY: _run_args
_run_args:
  # use the rest as arguments for the subcommand
  RUN_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
  # ...and turn them into do-nothing targets

  $(eval $(RUN_ARGS):;@:)
#
# Generic subcommands
#

# target: help - Display callable targets
.PHONY: help
help:
	egrep "^# target:" [Mm]akefile

#
# Docker
#

# target: logs - Show live logs
.PHONY = logs
logs: _run_args
	docker logs --tail=100 --follow $(RUN_ARGS)

# target: shell <service> - open a shell in the specified service container
.PHONY: shell
shell: _run_args
	docker exec -it $(RUN_ARGS) bash

#
# Tests
#


# target: test - Run all available test (exclude load tests)
.PHONY: test
test:
	poetry run pytest

#
# Poetry
#

# target: deps - create the requirements.txt from the pyproject.toml
.PHONY: deps
deps:
	poetry export -f requirements.txt --output requirements.txt --without-hashes

#
# Lambda Function
#

# target: build - Build the lambda function image.
.PHONY: build
build:
	docker build --no-cache -t galeo-lambda .

# target: run - Run the lamba function and mongoDB containers
.PHONY: run $(RUN_ARGS)
run:
	docker compose up -d

# target: down - Stop and Remove the lamba function and mongoDB containers
.PHONY: down $(RUN_ARGS)
down:
	docker compose down

# target: invoke - Invoke the lambda function locally.
.PHONY: invoke
invoke:
	curl --header "Content-Type: application/json" --request POST "http://localhost:9000/2015-03-31/functions/function/invocations" --data @events/event.json

#
# MongoDB
#

# target: mongo-init - Check that your Mongo database is working by inserting a test document.
.PHONY: mongo_init
mongo_init:
	python scripts/init_db.py




