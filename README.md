# Life Lists - Server

This repository contains the server-side API for the Life-Lists App.

The server is written in Python and uses the Flask framework.

This server communicates with a MySQL database which is hosted by Heroku (as well as the server itself).

# Contributing

Ensure you have Docker installed

Ensure you have `mysql` installed. On mac run
```
brew install mysql
```

To use the production MYSQL database run
```
eval $(make mysql-env)
```

To use a local dev MySQL database then
```
export JAWSDB_URL=my-database-creds
```

Clone the repository

To run the server, run
```
make run
```

To test that the server is running and the API is setup, try hitting the healthcheck from your browser
```
GET localhost:5000/healthcheck
```

To develop locally first make sure all the tests are passing
```
make test-local
```

Make any relevant changes, and make sure to add tests.

Ensure the code follows our formatting standards
```
make lint-local
```

Submit a Merge Request to be reviewed.

Once it is reviewed the app can be published


# Deploying

This server is deployed to heroku, using the Container Registry with Heroku CLI.

First ensure that Heroku CLI is installed on your machine, and you are logged into Dennis' account, and the container registry
```
brew tap heroku/brew && brew install heroku
heroku login
heroku container:login
```

Next, simply run
```
make lint-local test-local build publish deploy
```

This will trigger a new deployment of the latest code changes, but will ensure the test pipeline passes before then, as we currently do not have CI/CD setup for this code repository.


# Logs and Metrics

You can tail the production logs locally by running
```
make get-prod-logs
```

And you can see app metrics by logging into the Heroku console