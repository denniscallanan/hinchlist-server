from src.api.client import BaseClient


class VotesClient(BaseClient):

    def __init__(self, db_client):
        super(VotesClient, self).__init__(db_client=db_client)

    def give_vote(self, authorized_user_id, list_id):
        self.db_client.execute_amend("INSERT INTO votes (user_id, lifelist_id) VALUES (%s, %s)",
                                     (authorized_user_id, list_id,))

        return self._build_succesful_response({
            "status": "success"
        })

    def take_vote(self, authorized_user_id, list_id):
        self.db_client.execute_amend("DELETE FROM votes WHERE user_id=%s AND lifelist_id=%s",
                                     (authorized_user_id, list_id,))

        return self._build_succesful_response({
            "status": "success"
        })

    def count_likes(self, list_id):
        res = self.db_client.execute_get("SELECT COUNT(*) FROM votes WHERE lifelist_id=%s", (list_id,))
        return self._build_succesful_response({"count": res[0][0]})

    def is_liked(self, authorized_user_id, list_id):
        res = self.db_client.execute_get("SELECT * FROM votes WHERE lifelist_id=%s and user_id=%s LIMIT 1",
                                         (list_id, authorized_user_id,), limit_one=True)
        return self._build_succesful_response({"liked": res is not None})
