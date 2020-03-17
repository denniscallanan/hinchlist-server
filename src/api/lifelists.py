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


class LifeListClient(BaseClient):

    def __init__(self):
        super(LifeListClient, self).__init__("", "")

    def get_life_list(self, list_id):
        mock_lists = [
            LifeList("1", "Corona Prep List", "List preparing for coronavirus isolation", "1234"),
            LifeList("2", "Bathroom Cleaning", "List getting all the spots when cleaning your bathroom", "1234"),
            LifeList("3", "Workout list", "List of basic exercises for a home workout", "1234")
        ]
        life_list = next((x for x in mock_lists if x.list_id == list_id), None)
        return self._prepare_response(life_list)
