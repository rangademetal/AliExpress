from Database.ConnectionDatabase import ConnectionDatabase
from Emag.WebDriver import Initialization
from Database.Secret import *
from mysql.connector.errors import Error


database = ConnectionDatabase(DB_DATABASE)
db = database.connect_database()
scanner = Initialization()
source = 'https://www.emag.ro/search/laptopuri/laptop/c?ref=autosuggest_category1'
scanner.driver.get(source)

category = scanner.driver.find_element_by_xpath('//*[@id="main-container"]/section[1]/div/div[3]/div[2]/div[2]/div[1]/h1/span/span[1]')
print(category.text)
source = scanner.driver.current_url
try:
    cursor = db.cursor()
    sql = 'INSERT INTO category(name_category, source) values (%s, %s)'
    val = (category.text, source)
    cursor.execute(sql, val)
    db.commit()
except Error as e:
    print(f'Error - {e}')