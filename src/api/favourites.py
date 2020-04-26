from src.api.client import BaseClient


class FavouritesClient(BaseClient):

    def __init__(self, db_client):
        super(FavouritesClient, self).__init__(db_client=db_client)

    def make_favourite(self, authorized_user_id, list_id):
        self.db_client.execute_amend("INSERT INTO favourites (user_id, lifelist_id) VALUES (%s, %s)",
                                     (authorized_user_id, list_id,))

        return self._build_succesful_response({
            "status": "success"
        })

    def take_favourite(self, authorized_user_id, list_id):
        self.db_client.execute_amend("DELETE FROM favourites WHERE user_id=%s AND lifelist_id=%s",
                                     (authorized_user_id, list_id,))

        return self._build_succesful_response({
            "status": "success"
        })

    def is_favourited(self, authorized_user_id, list_id):
        res = self.db_client.execute_get("SELECT * FROM favourites WHERE lifelist_id=%s and user_id=%s LIMIT 1",
                                         (list_id, authorized_user_id,), limit_one=True)
        return self._build_succesful_response({"favourited": res is not None})
