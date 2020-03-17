from flask import Flask
from src.api.lifelists import LifeListClient
import os

app = Flask(__name__)

life_list_client = LifeListClient()


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
