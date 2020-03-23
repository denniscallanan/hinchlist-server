from flask import Flask
from flask import request
from src.api.lifelists import LifeListClient
from src.api.favourites import FavouritesClient
from src.api.tasks import TaskClient
from src.auth.fb_auth import get_authorized_user
import os
from src.api.constants import RequestFields
from src.database.db import DBClient

app = Flask(__name__)

db_client = DBClient()

life_list_client = LifeListClient(db_client)
task_client = TaskClient(db_client)
fav_client = FavouritesClient(db_client)


@app.route('/')
def root():
    return {"result": "Use /healthcheck to check the health of the server"}


@app.route('/healthcheck')
def healthcheck():
    return {"status": "up"}


@app.route('/api/lists/<list_id>')
def get_list(list_id):
    authorized_user_id = get_authorized_user(request.headers.get(RequestFields.ACCESS_TOKEN))
    if not authorized_user_id:
        return {"error": "Unauthorized"}, 401
    return life_list_client.get_life_list(list_id)


@app.route('/api/lists/favourites')
def get_favourite_lists():
    authorized_user_id = get_authorized_user(request.headers.get(RequestFields.ACCESS_TOKEN))
    if not authorized_user_id:
        return {"error": "Unauthorized"}, 401
    return life_list_client.get_favourite_lists(authorized_user_id)


@app.route('/api/lists/mine')
def get_my_lists():
    authorized_user_id = get_authorized_user(request.headers.get(RequestFields.ACCESS_TOKEN))
    if not authorized_user_id:
        return {"error": "Unauthorized"}, 401
    return life_list_client.get_my_lists(authorized_user_id)


@app.route('/api/lists/search')
def search_lists():
    authorized_user_id = get_authorized_user(request.headers.get(RequestFields.ACCESS_TOKEN))
    if not authorized_user_id:
        return {"error": "Unauthorized"}, 401
    return life_list_client.search_lists(request.args.get(RequestFields.QUERY))


@app.route('/api/tasks/lists/<list_id>')
def get_tasks(list_id):
    authorized_user_id = get_authorized_user(request.headers.get(RequestFields.ACCESS_TOKEN))
    if not authorized_user_id:
        return {"error": "Unauthorized"}, 401
    return task_client.get_tasks(list_id)


@app.route('/api/favourites/lists/<list_id>')
def is_favourited(list_id):
    authorized_user_id = get_authorized_user(request.headers.get(RequestFields.ACCESS_TOKEN))
    if not authorized_user_id:
        return {"error": "Unauthorized"}, 401
    return fav_client.is_favourited(authorized_user_id, list_id)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=os.environ.get("PORT", 5000), threaded=True)
