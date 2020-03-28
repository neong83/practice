.PHONY: build run

build: docker

docker:
	docker-compose build

run:
	docker-compose run app
