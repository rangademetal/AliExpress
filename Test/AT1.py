import unittest

from Database.Secret import DB_DATABASE, DB_HOST, DB_USERNAME, DB_PASSWORD


class InputTest(unittest.TestCase):
    def setUp(self):
        pass

    # Database connection
    def test_database(self):
        self.assertEqual(DB_USERNAME, 'aliexpress')
        self.assertEqual(DB_HOST, 'localhost')
        self.assertEqual(DB_PASSWORD, 'aliexpress')
        self.assertEqual(DB_DATABASE, 'aliexpress')

    def test_location(self):
        pass

if __name__ == '__main__':
    unittest.main()
