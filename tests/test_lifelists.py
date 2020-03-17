import unittest

from src.api.lifelists import LifeListClient


class TestLifeListsClient(unittest.TestCase):

    def setUp(self):
        self.client = LifeListClient()

    def test_get_life_list(self):
        data = self.client.get_life_list("1")
        self.assertIn("result", data)
        self.assertEqual(data["result"], {"list_id": "1", "title": "Corona Prep List",
                                          "description": "List preparing for coronavirus isolation", "user_id": "1234"})
