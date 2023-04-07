# STARDEW VALLEY APP

## Description

This is a simple app that allows you to view the Stardew Valley wiki in a simple and easy to use interface. It also
allows you to view the wiki offline.

## Installation

### Requirements

- [python3](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installing/)
- [git](https://git-scm.com/downloads)
- [poetry](https://python-poetry.org/docs/#installation)
- [django](https://www.djangoproject.com/download/)
- [docker](https://docs.docker.com/get-docker/)
- [flyctl](https://fly.io/docs/getting-started/installing-flyctl/)

### Steps

#### Deploy en local
1. Clone the repository
2. Navigate to the directory
3. Run `poetry install`
4. Run `poetry shell`
5. Run `python3 manage.py runserver`
6. Navigate to `localhost:8000` in your browser
7. Enjoy!
8. To exit the virtual environment, run `exit`
9. To re-enter the virtual environment, run `poetry shell`

#### Deploy en docker
1. Clone the repository
2. Navigate to the directory
3. Run `docker-compose up -d`
4. Navigate to `localhost:8000` in your browser
5. Enjoy!
6. To stop the docker container, run `docker-compose down`
7. To re-start the docker container, run `docker-compose up -d`
8. To re-build the docker container, run `docker-compose up -d --build`
9. To re-build the docker container without using cache, run `docker-compose up -d --build --no-cache`