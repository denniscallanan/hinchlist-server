from flask import Flask
from src.api.lifelists import LifeListClient
from src.api.constants import Environment
import os
import MySQLdb
from src.api.constants import EnvVars
from urllib.parse import urlparse

app = Flask(__name__)

ENVIRONMENT = os.environ.get("ENV", "test")

if ENVIRONMENT == Environment.PROD:
    DATABASE_URL = os.environ[EnvVars.DATABASE_URL]
    url = urlparse(DATABASE_URL)
    db_conn = MySQLdb.connect(host=url.hostname, port=url.port, db=url.path[1:], passwd=url.password,
                              user=url.username)
else:
    DATABASE_URL = os.environ[EnvVars.DATABASE_URL]
    url = urlparse(DATABASE_URL)
    db_conn = MySQLdb.connect(host=url.hostname, port=url.port, db=url.path[1:], passwd=url.password,
                              user=url.username)

life_list_client = LifeListClient(db_conn)


@app.route('/')
def root():
    return {"result": "Use /healthcheck to check the health of the server"}


@app.route('/healthcheck')
def healthcheck():
    return {"status": "up"}


@app.route('/lists/<list_id>')
def hello_name(list_id):
    return life_list_client.get_life_list(list_id)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=os.environ.get("PORT", 5000))
