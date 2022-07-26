import unittest
import os

from WPTParser import WPTParser
from WPTParser.Fetch import Fetch

class FetchJSONTest(unittest.TestCase):

    def test_fetch_json(self):
        
        fetch = Fetch()
        self.assertNotEqual(fetch.json(), None) 

if __name__ == "__main__":
    unittest.main(verbosity=2)