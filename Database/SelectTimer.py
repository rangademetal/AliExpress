from Database.Secret import *
from Database.ConnectionDatabase import ConnectionDatabase
from prettytable import PrettyTable

database = ConnectionDatabase(DB_DATABASE)
db = database.connect_database()
table = PrettyTable()

try:
    cursor = db.cursor()
    sql = "SELECT id, source, timer FROM timer WHERE timer > 1.500"
    cursor.execute(sql)
    result = cursor.fetchall()
    table.field_names = ['Source', 'Time']
    for i in result:
        table.add_row([i[0], i[1]])
    print(table)
except Exception as e:
    print(f'ERROR - {e}')
