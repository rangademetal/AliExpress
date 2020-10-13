import mysql.connector


class ConnectionServer(object):
    def __init__(self, DB_HOST, DB_USERNAME, DB_PASSWORD):
        self.DB_HOST = DB_HOST
        self.DB_USERNAME = DB_USERNAME
        self.DB_PASSWORD = DB_PASSWORD

    def connect_server(self):
        server = mysql.connector.connect(
            host=self.DB_HOST,
            user=self.DB_USERNAME,
            password=self.DB_PASSWORD
        )
        return server
