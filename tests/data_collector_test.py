# Danny Salib
# Aug 17 2024
# Python 3.12.3

import unittest 
from src import DataCollector

class DataCollector(unittest.TestCase):

    def setUp(self) -> None:
        self.dc = DataCollector()
    
    def test_init_DataCollector(self):
        self.assertIsInstance(self.dc, DataCollector)
