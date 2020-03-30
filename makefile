.PHONY: build run test coverage

build: docker

docker:
	docker-compose build

run:
	docker-compose run --rm app

test:
	docker-compose run --rm app pytest tests/${args}

coverage:
	docker-compose run --rm app pytest --cov-report term-missing --cov=. tests/