from src.api.client import BaseClient


class TaskClient(BaseClient):

    def __init__(self, db_client):
        super(TaskClient, self).__init__(db_client=db_client)

    def get_tasks(self, list_id):
        res = self.db_client.execute_get("SELECT id, title FROM tasks WHERE lifelist_id=%s", (list_id,))
        return self._build_succesful_response({
            "items": [{"id": row[0], "title": row[1]} for row in res]
        })
