import mysql.connector
from Database.ConnectionServer import ConnectionServer
from Database.Secret import *


class ConnectionDatabase(ConnectionServer):

    def __init__(self, DB_DATABASE):
        super().__init__(DB_HOST, DB_USERNAME, DB_PASSWORD)
        self.DB_DATABASE = DB_DATABASE

    def connect_database(self):
        database = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USERNAME,
            password=DB_PASSWORD,
            database=self.DB_DATABASE
        )
        return database
