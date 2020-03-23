from src.api.client import BaseClient


class FavouritesClient(BaseClient):

    def __init__(self, db_client):
        super(FavouritesClient, self).__init__(db_client=db_client)

    def upsert_favourite(self, authorized_user_id, list_id):
        res = self.db_client.execute_get("SELECT id, title FROM tasks WHERE lifelist_id=%s and user_id=%s",
                                         (list_id, authorized_user_id,))
        return self._build_succesful_response({
            "items": [{"id": row[0], "title": row[1]} for row in res]
        })

    def is_favourited(self, authorized_user_id, list_id):
        res = self.db_client.execute_get("SELECT * FROM favourites WHERE lifelist_id=%s and user_id=%s LIMIT 1",
                                         (list_id, authorized_user_id,), limit_one=True)
        return self._build_succesful_response({"favourited": res is not None})
