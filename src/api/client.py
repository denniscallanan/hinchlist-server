class BaseClient:

    def __init__(self, db_conn=None):
        self.db_conn = db_conn

    def _prepare_response(self, item):
        if item:
            return {
                "result": item
            }
        return {
            "error": "Could not find requested item"
        }
