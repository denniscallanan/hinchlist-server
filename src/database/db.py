import os

from urllib.parse import urlparse

from mysql.connector.pooling import MySQLConnectionPool
from src.api.constants import EnvVars


class DBClient:

    def __init__(self):
        print("PID %d: initializing pool..." % os.getpid())
        environment = os.environ.get("ENV", "test")

        if environment in ('prod', 'test'):
            db_url = os.environ[EnvVars.DATABASE_URL]
            url = urlparse(db_url)

            dbconfig = {
                "host": url.hostname,
                "port": url.port,
                "user": url.username,
                "password": url.password,
                "database": url.path[1:],
            }
            self.pool = MySQLConnectionPool(pool_name="pool1", **dbconfig)

    def execute_get(self, query, params, limit_one=False):

        con = self.pool.get_connection()
        cur = con.cursor()
        cur.execute(query, params)
        if limit_one:
            result = cur.fetchone()
        else:
            result = cur.fetchall()
        con.close()

        return result

    def execute_post(self, query):
        pass
