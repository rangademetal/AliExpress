from Emag.WebDriver import Initialization
from Database.ConnectionDatabase import ConnectionDatabase
from Database.Secret import *
from mysql.connector.errors import Error
import time


class Timer:
    def __init__(self, source, pages):
        self.source = source
        self.pages = pages

    def timer(self):
        database = ConnectionDatabase(DB_DATABASE)
        scanner = Initialization()
        db = database.connect_database()
        scanner.driver.get(self.source)
        category = scanner.driver.find_element_by_xpath('//*[@id="main-container"]/section[1]/div/div[3]/div[2]/div[2]/div[1]/h1/span/span[1]')
        category = category.text

        cursor = db.cursor()
        sql = 'SELECT id from category where name_category = %s'
        val = (category, )
        cursor.execute(sql, val)
        res = cursor.fetchone()
        id_cat = res
        print(id_cat[0])

        total = []
        for i in range(1, self.pages):
            start = time.perf_counter()
            scanner.driver.get(f'https://www.emag.ro/search/laptopuri/laptop/p{i}/c')
            stop = time.perf_counter()
            timer = f'{stop - start:0.4f}'
            timer = float(timer)
            total.append(timer)
            print(f'Page {scanner.driver.current_url} have {stop - start:0.4f} seconds')
            try:
                sql = 'INSERT INTO timer(timer, id_category, source) values(%s, %s, %s)'
                val = (timer, id_cat[0], scanner.driver.current_url)
                cursor.execute(sql, val)
                db.commit()
            except Error as e:
                print('Update in Database')
                sql = 'UPDATE timer SET timer = %s WHERE source = %s'
                val = (timer, scanner.driver.current_url)
                cursor.execute(sql, val)
                db.commit()

        print(f'Total loading time is: {sum(map(float, total))}')