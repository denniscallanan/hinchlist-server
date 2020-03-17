APP_NAME			= hinchlist
IMAGE               = life-list-app
TAG                 = latest

PYTEST_OPTIONS  ?= --cov src.api
PORT            ?= 5000
JAWSDB_URL      ?= unset

clean:
	docker rm -f $(DOCKER_REPOSITORY) || true
	docker rmi -f $(DOCKER_REPOSITORY):$(TAG) || true

build:
	docker build -t $(IMAGE) .

run:
	docker run -e JAWSDB_URL=$(JAWSDB_URL) -u :1000 -p $(PORT):5000 $(IMAGE)

run-local:
	python3 run_server.py

lint-local:
	python3 -m pip install -r src/dev-requirements.txt --user
	python3 -m pip install -r src/requirements.txt --user
	python3 -m pylint src

test-local:
	python3 -m pip install -r src/dev-requirements.txt --user
	python3 -m pip install -r src/requirements.txt --user
	python3 -m pytest $(PYTEST_OPTIONS) tests/test_*

get-prod-logs:
	heroku logs --tail -a $(APP_NAME)

publish:
	heroku container:push web -a $(APP_NAME)

deploy:
	heroku container:release web -a $(APP_NAME)

mysql-env:
	export $(shell heroku config -s -a hinchlist | grep JAWSDB_URL)