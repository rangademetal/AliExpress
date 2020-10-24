from Emag.WebDriver import Initialization
from Database.ConnectionDatabase import ConnectionDatabase
from Database.Secret import *
from mysql.connector.errors import Error
from selenium.common.exceptions import NoSuchElementException
import time


class Timer:
    def __init__(self, ):
        self.scanner = Initialization()
        self.database = ConnectionDatabase(DB_DATABASE)

    def timer_(self, source, pages, url):

        db = self.database.connect_database()
        self.scanner.driver.get(source)
        category = self.scanner.driver.find_element_by_class_name('title-phrasing-xl')
        category = category.text
        print(category)
        cursor = db.cursor(buffered=True)
        sql = 'SELECT id from category where name_category = %s'
        val = (category, )
        cursor.execute(sql, val)
        res = cursor.fetchone()
        id_cat = res

        for i in range(1, pages):
            start = time.perf_counter()
            self.scanner.driver.get(f'{url}/p{i}/c')
            stop = time.perf_counter()
            timer = f'{stop - start:0.4f}'
            timer = float(timer)
            print(f'Page {self.scanner.driver.current_url} have {stop - start:0.4f} seconds')
            try:
                sql = 'INSERT INTO timer(timer, id_category, source) values(%s, %s, %s)'
                val = (timer, id_cat[0], self.scanner.driver.current_url)
                cursor.execute(sql, val)
                db.commit()
            except Error as e:
                print('Update in Database')
                sql = 'UPDATE timer SET timer = %s WHERE source = %s'
                val = (timer, self.scanner.driver.current_url)
                cursor.execute(sql, val)
                db.commit()

    def __del__(self):
        self.scanner.driver.quit()