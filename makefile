.PHONY: build run test coverage

build: docker

docker:
	docker-compose build

run:
	docker-compose run app

test:
	docker-compose run app pytest tests/${argv}

coverage:
	docker-compose run app pytest --cov=tests tests/