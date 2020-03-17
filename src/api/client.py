from src.api.dto import DTO


class BaseClient:

    def __init__(self, db_conn=None):
        self.db_conn = db_conn

    def _prepare_response(self, item: DTO):
        if item:
            return {
                "result": item.to_dict()
            }
        return {
            "error": "Could not find requested item"
        }
