import os
from urllib.parse import urlparse
import MySQLdb
from src.api.constants import EnvVars


class DBClient:

    def __init__(self):
        environment = os.environ.get("ENV", "test")
        db_url = os.environ[EnvVars.DATABASE_URL]

        if environment == 'prod' or environment == 'test':
            url = urlparse(db_url)
            self.db_conn = MySQLdb.connect(host=url.hostname, port=url.port, db=url.path[1:], passwd=url.password,
                                           user=url.username)

    def execute_get(self, query, params, limit_one=False):
        if not self.db_conn:
            self.__init__()
        cur = self.db_conn.cursor()
        cur.execute(query, params)
        if limit_one:
            return cur.fetchone()
        return cur.fetchall()

    def execute_post(self, query):
        pass
