# Practice

## Description
This is a practice for myself to learn on how to break story into small tasks to provide incremental value for business 

## Trello link
https://trello.com/b/wBaHaEPa/practices

## Getting started

### Build image

Build image prior to running this application with either one of the follow commands
1. `docker build`
2. or `make`

### Run code

Run `docker-compose run app` to execute code from docker

## Contribution

### Install developer tools

1. Install `vs code`
2. Install formatting tools `pip3 install black isort pre-commit`
3. Install Git pre-commit hooks with `pre-commit install`

** if you having trouble locating `pre-commit` after pip3 install, you can either manually add `/usr/local/bin/pre-commit` to `.bash_profile` or reinstall it with `brew install pre-commit`

### Test

Full commands to run unit and coverage tests

1. `docker-compose run app pytest [FILE_NAME]` Single unit test file 
2. `docker-compose run app pytest [FOLDER_NAME]/` Multi unit tests in folder 
3. `docker-compose run app pytest --cov=. [FOLDER_NAME]/` Coverage tests 

You can use the following alias to run unit and coverage tests
1. `make test [FILE_NAME]` file name in this command is optional.  It will run test in a single file if `FILE_NAME` is given, otherwise, it will run through all tests in code base
2. `make coverage` It will provide you code coverage for entire code base
