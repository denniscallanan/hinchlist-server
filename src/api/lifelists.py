from src.api.client import BaseClient
from src.api.dto import DTO


class LifeList(DTO):

    def __init__(self, list_id, title, description, user_id):
        self.list_id = list_id
        self.title = title
        self.description = description
        self.user_id = user_id

    def to_dict(self):
        return {
            "list_id": self.list_id,
            "title": self.title,
            "description": self.description,
            "user_id": self.user_id
        }

    @staticmethod
    def from_tuple(tpl):
        if not tpl:
            return None
        return LifeList(*tpl)


class LifeListClient(BaseClient):

    def __init__(self, db_conn):
        super(LifeListClient, self).__init__(db_conn=db_conn)

    def get_life_list(self, list_id):
        cur = self.db_conn.cursor()
        cur.execute("SELECT * FROM lifelists WHERE id=%s", (list_id,))
        res = cur.fetchone()
        return self._prepare_response(LifeList.from_tuple(res))
