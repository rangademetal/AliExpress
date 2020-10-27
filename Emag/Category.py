from Database.ConnectionDatabase import ConnectionDatabase
from Emag.WebDriver import Initialization
from Database.Secret import *
from mysql.connector.errors import Error


class Category:
    def __init__(self):
        self.scanner = Initialization()
        self.database = ConnectionDatabase(DB_DATABASE)

    def get_category(self, source):
        db = self.database.connect_database()
        self.scanner.driver.get(source)
        category = self.scanner.driver.find_element_by_class_name('title-phrasing-xl')
        print(category.text)
        try:
            cursor = db.cursor()
            sql = 'INSERT INTO category(name_category) values (%s)'
            val = (category.text,)
            cursor.execute(sql, val)
            db.commit()
        except Error as e:
            print(f'Error - {e}')

    def __del__(self):
        self.scanner.driver.quit()