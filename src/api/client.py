from src.api.dto import DTO


class BaseClient:

    def __init__(self, db_host, db_pass, db_conn=None):
        self.db_conn = db_conn
        self.db_host = db_host
        self.db_pass = db_pass

    def _prepare_response(self, item: DTO):
        if item:
            return {
                "result": item.to_dict()
            }
        return {
            "error": "Could not find requested item"
        }
