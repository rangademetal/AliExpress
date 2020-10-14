import unittest
import os
from pathlib import Path
from Database.Secret import DB_DATABASE, DB_HOST, DB_USERNAME, DB_PASSWORD


# Test database parameters and
class InputTest(unittest.TestCase):
    def setUp(self):
        pass

    # Check enviroment parameters with database connection
    def test_database(self):
        self.assertEqual(DB_USERNAME, 'aliexpress')
        self.assertEqual(DB_HOST, 'localhost')
        self.assertEqual(DB_PASSWORD, 'aliexpress')
        self.assertEqual(DB_DATABASE, 'emag')

    # Check webdriver is located in project file
    def test_location(self):
        path = os.getcwd()
        path = Path(path)
        os.chdir(path.parent)
        self.assertEqual(True, os.path.exists('chromedriver.exe'), 'Put your chromrdriver.exe in AliExpress folder !!!')


if __name__ == '__main__':
    unittest.main()