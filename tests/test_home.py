# -*- coding: utf-8 -*-
from app import app
import unittest

class HomePageShould(unittest.TestCase):
    def setUp(self):
        app.config['DEBUG'] = True
        app.config['TESTING'] = True
        self.app = app.test_client()
        self.result = self.app.get('/')
                                                                                                                                                   
    def test_return_200_status_code(self):
        self.assertEqual(self.result.status_code, 200)

    def test_contain_welcome_in_body(self):
        self.assertIn("Welcome", self.result.data.decode("utf-8"))

if __name__ == "__main__":
    unittest.main(verbosity=2)
