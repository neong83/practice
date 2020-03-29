# Practice  [![Build Status](https://travis-ci.org/neong83/practice.svg?branch=master)](https://travis-ci.org/neong83/practice)

## Description
This is a practice repo for myself to learn couple key features
1. how to break story into small tasks to provide incremental value for business
2. how to build docker and setup test environment for continuous integration
3. how to provide better introduction and PR standard in GitHub

## Trello link
https://trello.com/b/wBaHaEPa/practices

## Getting started

### Build image

Build image prior to running this application with either one of the follow commands
1. `docker build`
2. or `make`

### Run code

Run `docker-compose run app` or `make run` to execute code from docker

## Contribution

### Install developer tools

1. Install `vs code`
2. Install formatting tools `pip3 install black isort pre-commit`
3. Install Git pre-commit hooks with `pre-commit install`

** if you having trouble locating `pre-commit` after pip3 install, you can either manually add `/usr/local/bin/pre-commit` to `.bash_profile` or reinstall it with `brew install pre-commit`

### Test

Full commands to run unit and coverage tests

1. `docker-compose run app pytest` Multi unit tests in `tests` folder 
2. `docker-compose run app pytest args=[PATH_TO/FILE_NAME]` Single unit test file 
3. `docker-compose run app pytest --cov=. [FOLDER_NAME]/` Coverage tests 

You can use the following alias to run unit and coverage tests
1. `make test [args=PATH_TO/FILE_NAME]` section inside `[]` is optional.  It will run test in a single file if `args=PATH_TO/FILE_NAME` is given, otherwise, it will run through all tests in code base
2. `make coverage` It will provide you code coverage for entire code base


### Travis CI

Life cycle reference: https://docs.travis-ci.com/user/job-lifecycle
