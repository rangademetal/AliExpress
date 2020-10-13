from Database.ConnectionServer import ConnectionServer
from Database.Secret import *

server = ConnectionServer(DB_HOST, DB_USERNAME, DB_PASSWORD)
server = server.connect_server()
cursor = server.cursor()
cursor.execute('CREATE DATABASE AliExpress')
