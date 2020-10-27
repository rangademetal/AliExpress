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
            count = 1
            scroll = 0
            start = time.perf_counter()
            self.scanner.driver.get(f'{url}/p{i}/c')
            while count != 62:
                self.scanner.driver.execute_script('window.scrollTo(0, ' + str(scroll) + ')')
                print(count)
                try:
                    clickers = self.scanner.driver.find_element_by_xpath(
                        f'//*[@id="card_grid"]/div[{count}]/div/div/div[2]/h2/a')
                except NoSuchElementException as e:
                    continue

                start = time.perf_counter()
                clickers.click()
                stop = time.perf_counter()
                count += 1
                if count % 5 == 0:
                    count += 1

                scroll += 145
                timer = f'{stop - start:0.4f}'
                timer = float(timer)
                print(timer)
                self.scanner.driver.execute_script("window.history.go(-1)")
                time.sleep(1)

            stop = time.perf_counter()
            timer = f'{stop - start:0.4f}'
            timer = float(timer)
            print(f'Page {self.scanner.driver.current_url} have {stop - start:0.4f} seconds')
            self.database.insert_update(timer, id_category, self.scanner.driver.current_url)

    def __del__(self):
        self.scanner.driver.quit()