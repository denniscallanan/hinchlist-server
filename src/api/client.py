from src.database.db import DBClient


class BaseClient:

    def __init__(self, db_client: DBClient = None):
        self.db_client = db_client

    def _build_succesful_response(self, item):
        if item:
            return {
                "result": item
            }
        return {
            "error": "Could not find requested item"
        }

    def _build_failed_response(self, err_code, error_msg):
        return {"error": error_msg}, err_code

    def _wildcard_pad(self, query):
        return "%" + query + "%"
