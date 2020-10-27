from Emag.WebDriver import Initialization
from Database.QueryDatabase import Query
from selenium.common.exceptions import NoSuchElementException
import time


class Timer:
    def __init__(self, ):
        self.scanner = Initialization()
        self.database = Query()

    def timer_(self, source, pages, url):
        self.scanner.driver.get(source)
        category = self.scanner.driver.find_element_by_class_name('title-phrasing-xl')
        id_category = self.database.select_id(category.text)

        for i in range(1, pages):
            start = time.perf_counter()
            self.scanner.driver.get(f'{url}/p{i}/c')
            stop = time.perf_counter()
            timer = f'{stop - start:0.4f}'
            timer = float(timer)
            print(f'Page {self.scanner.driver.current_url} have {stop - start:0.4f} seconds')
            self.database.insert_update(timer, id_category, self.scanner.driver.current_url)

    def __del__(self):
        self.scanner.driver.quit()
