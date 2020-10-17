import unittest
from Emag.WebDriver import Initialization

class TimeTest(unittest.TestCase):
    def setUp(self):
        self.tester = Initialization()
        source = 'https://www.emag.ro/search/laptopuri/laptop/c?ref=autosuggest_category1'
        self.tester.driver.get(source)

    def test_listpage(self):
        for i in range(1, 29):
            self.tester.driver.get(f'https://www.emag.ro/laptopuri/p{i}/c')


if __name__ == '__main__':
    unittest.main()