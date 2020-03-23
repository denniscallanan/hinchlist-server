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

    def __init__(self, db_client):
        super(LifeListClient, self).__init__(db_client=db_client)

    def get_life_list(self, list_id):
        res = self.db_client.execute_get("SELECT * FROM lifelists WHERE id=%s", (list_id,), limit_one=True)
        return self._build_succesful_response(LifeList.from_tuple(res))

    def get_favourite_lists(self, authorized_user_id):
        res = self.db_client.execute_get(
            "SELECT lifelists.id, lifelists.title, lifelists.description, lifelists.author_id FROM "
            "favourites left join lifelists on favourites.lifelist_id = lifelists.id where user_id=%s",
            (authorized_user_id,))
        return self._build_succesful_response({
            "items": [LifeList.from_tuple(x).to_dict() for x in res]
        })

    def get_my_lists(self, authorized_user_id):
        res = self.db_client.execute_get(
            "SELECT * FROM lifelists where author_id=%s", (authorized_user_id,))
        return self._build_succesful_response({
            "items": [LifeList.from_tuple(x).to_dict() for x in res]
        })

    def search_lists(self, query):
        if not query:
            return self._build_failed_response(400, "Please supply valid search query. Required: 'query' param")
        query = self._wildcard_pad(query)
        res = self.db_client.execute_get(
            """SELECT * from lifelists where title like %s or description like %s LIMIT 30""",
            (query, query,))
        return self._build_succesful_response({
            "items": [LifeList.from_tuple(x).to_dict() for x in res]
        })
