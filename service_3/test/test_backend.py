import pytest
import unittest
from flask_testing import TestCase
from flask import url_for
import app
# import roll_dice

# class TestBase(unittest.TestCase):
#     def create_app(self):
#         config_name = 'testing'
#         return app

# class testApp(TestBase):
def test_page(self):
    response = self.client.get(url_for('service_3'))
    self.assertEqual(response.status_code, 200)

    # def test_roll_dice():
    #     self.assertEqual(roll_dice())
