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

    def get_favourite_lists(self, authorized_user_id):
        print("Getting favourite lists for " + authorized_user_id)
        return self._prepare_response({"items": [
            LifeList.from_tuple((
                1, 'Corona Preparation 1',
                'List preparing for corona virus - includes shopping, and sanitization', None,)).to_dict(),
            LifeList.from_tuple((
                2, 'Corona Preparation 2',
                'List preparing for corona virus - includes shopping, and sanitization', None,)).to_dict(),
            LifeList.from_tuple((
                3, 'Corona Preparation 3',
                'List preparing for corona virus - includes shopping, and sanitization', None,)).to_dict(),
            LifeList.from_tuple((
                4, 'Corona Preparation 4',
                'List preparing for corona virus - includes shopping, and sanitization', None,)).to_dict()
        ]})
