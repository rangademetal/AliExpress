from Emag.WebDriver import Initialization
from selenium.common.exceptions import NoSuchElementException
from Database.QueryDatabase import Query
import time


class Product:

    def __init__(self):
        self.scanner = Initialization()
        self.database = Query()

    def product_timer(self, url):
        self.scanner.driver.get(url)
        count = 1
        scroll = 0
        category = self.scanner.driver.find_element_by_class_name('title-phrasing-xl')
        id_category = self.database.select_id(category.text)

        while count != 62:
            self.scanner.driver.execute_script('window.scrollTo(0, ' + str(scroll) + ')')
            print(count)
            try:
                clickers = self.scanner.driver.find_element_by_xpath(f'//*[@id="card_grid"]/div[{count}]/div/div/div[2]/h2/a')
            except NoSuchElementException:
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
            print(id_category)
            print(timer)
            print(self.scanner.driver.current_url)
            self.database.insert_update(timer, id_category, self.scanner.driver.current_url)
            # try:
            #     sql = 'INSERT INTO timer(timer, id_category, source) values(%s, %s, %s)'
            #     val = (timer, id_cat[0], self.scanner.driver.current_url)
            #     cursor.execute(sql, val)
            #     db.commit()
            # except Error as e:
            #     print('Update in Database')
            #     sql = 'UPDATE timer SET timer = %s WHERE source = %s'
            #     val = (timer, self.scanner.driver.current_url)
            #     cursor.execute(sql, val)
            #     db.commit()
            self.scanner.driver.execute_script("window.history.go(-1)")
            time.sleep(1)


product = Product()
product.product_timer('https://www.emag.ro/placi_video/c')