from Database.Secret import *
from Database.ConnectionDatabase import ConnectionDatabase
from mysql.connector.errors import Error


class Query:
    def __init__(self):
        self.database = ConnectionDatabase(DB_DATABASE)
        self.db = self.database.connect_database()
        self.cursor = self.db.cursor(buffered=True)

    def select_id(self, category):
        sql = 'SELECT id from category where name_category = %s'
        val = (category, )
        self.cursor.execute(sql, val)
        res = self.cursor.fetchone()
        return res[0]

    def insert_update(self, timer, id_category, source):
        try:
            sql = 'INSERT INTO timer(timer, id_category, source) values(%s, %s, %s)'
            val = (timer, id_category, source)
        except Error:
            print('Update in Database')
            sql = 'UPDATE timer SET timer = %s WHERE source = %s'
            val = (timer, source)
        self.cursor.execute(sql, val)
        self.db.commit()
