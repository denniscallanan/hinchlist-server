import unittest

from src.api.lifelists import LifeListClient


class MockCursor:
    def execute(self, *args):
        return None

    def fetchone(self):
        return 1, 'Corona Preparation', 'List preparing for corona virus - includes shopping, and sanitization', None


class MockDB:
    def cursor(self):
        return MockCursor()


class TestLifeListsClient(unittest.TestCase):

    def setUp(self):
        self.client = LifeListClient(MockDB())

    def test_get_life_list(self):
        data = self.client.get_life_list("1")
        self.assertIn("result", data)
        self.assertEqual(data["result"], {"list_id": 1, "title": "Corona Preparation",
                                          "description": "List preparing for corona virus - includes "
                                                         "shopping, and sanitization",
                                          "user_id": None})
