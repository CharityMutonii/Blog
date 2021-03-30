import unittest
from app.models import Quotes

class testQuotes(unittest.TestCase):
    def setUp(self):
        self.new_quote = Quotes('charity','loving is all',"http://github.com/CharityMutonii")

    def test_instance_variables(self):
        self.assertTrue(isinstance(self.new_quote,Quotes))