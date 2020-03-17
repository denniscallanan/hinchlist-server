APP_NAME			= hinchlist
IMAGE               = life-list-app
TAG                 = latest
DOCKER_REPOSITORY   = registry-app.eng.qops.net:5001/profserv/projects/$(IMAGE)

PYTEST_OPTIONS  ?= --cov src.api --cov-report html --cov-report xml:./htmlcov/coverage.xml
PORT            ?= 5000

clean:
	docker rm -f $(DOCKER_REPOSITORY) || true
	docker rmi -f $(DOCKER_REPOSITORY):$(TAG) || true

build:
	docker build -t $(IMAGE) .

run:
	docker run -u :1000 -p $(PORT):5000 $(IMAGE)

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
