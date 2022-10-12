fmt: ## fmt
	black . && isort .

lint: ## lint
	black --check . && isort --check . && mypy .

test: ## test
	pytest