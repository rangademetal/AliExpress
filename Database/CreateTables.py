from mysql.connector.errors import Error
from Database.ConnectionDatabase import ConnectionDatabase
from Database.Secret import *

database = ConnectionDatabase(DB_DATABASE)

database = database.connect_database()
cursor = database.cursor()

try:
    cursor.execute(
        'CREATE TABLE category'
        '('
        'ID INTEGER AUTO_INCREMENT PRIMARY KEY,'
        'name_category VARCHAR(20) not null'
        ')'
    )
except Error as e:
    print(f'ERROR - {e}')

try:
    cursor.execute(
        'CREATE TABLE product'
        '('
        'ID INTEGER AUTO_INCREMENT PRiMARY KEY,'
        'name_product varchar(30) NOT NULL,'
        'source varchar(100) NOT NULL,'
        'time FLOAT NOT NULL,'
        'datetime DATE NOT NULL,'
        'id_category INTEGER NOT NULL,'
        'FOREIGN KEY(id_category) REFERENCES category(ID)'     
        ')'
    )
except Error as e:
    print(f'ERROR - {e}')