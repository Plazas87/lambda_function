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

# target: shell <service - open a shell in the specified service container
.PHONY: shell
shell: _run_args
	docker exec -it $(RUN_ARGS) sh

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
	poetry export -f requirements.txt --output requirements.txt

#
# Clean up
#

#
# Lambda Function
#

# target: build - Build the lambda function image.
.PHONY: build
build:
	docker build --no-cache -t galeo-lambda .

# target: run - Run the Lambda function locally
.PHONY: run $(RUN_ARGS)
run:
	docker run -d --name $(RUN_ARGS) -p 9000:8080 --env-file .env galeo-lambda

# target: invoke - Invoke the lambda function locally.
.PHONY: invoke
invoke:
	curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d @src/events/event.json

# target: stop - stop the Lambda container
.PHONY: stop
stop:
	docker stop $(RUN_ARGS)

# target: remove - remove the Lambda container
.PHONY: remove
remove:
	docker rm $(RUN_ARGS)

# target: restart - stop, remove and run the Lambda container
.PHONY: restart
restart: stop remove run


#
# MongoDB
#
