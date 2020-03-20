from flask import Flask
from flask import request
from src.api.lifelists import LifeListClient
from src.api.constants import Environment
from src.auth.fb_auth import get_authorized_user
import os
import MySQLdb
from src.api.constants import EnvVars, RequestHeaders
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


@app.route('/api/lists/<list_id>')
def get_list(list_id):
    authorized_user_id = get_authorized_user(request.headers.get(RequestHeaders.ACCESS_TOKEN))
    if not authorized_user_id:
        return {"error": "Unauthorized"}, 401
    return life_list_client.get_life_list(list_id)


@app.route('/api/lists/favourites')
def get_favourite_lists():
    authorized_user_id = get_authorized_user(request.headers.get(RequestHeaders.ACCESS_TOKEN))
    if not authorized_user_id:
        return {"error": "Unauthorized"}, 401
    return life_list_client.get_favourite_lists(authorized_user_id)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=os.environ.get("PORT", 5000))
