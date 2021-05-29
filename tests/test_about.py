# -*- coding: utf-8 -*-
from app import app
import unittest

class AboutPageShould(unittest.TestCase):
    def setUp(self):
        app.config['TESTING']=True
        app.config['DEBUG']=True
        self.app = app.test_client()
        self.result = self.app.get('/about')


    def test_return_200_status_code(self):
        self.assertEqual(self.result.status_code, 200)

    def test_contain_text_in_body(self):
        self.assertIn("JobaDiniz", self.result.data.decode('utf-8'))

if __name__ == "__main__":
    unittest.main(verbosity=2)

