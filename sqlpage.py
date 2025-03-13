import mysql.connector as sql

class connecting:
    def __init__(self):
        self.connection = sql.connect(
        host = 'localhost',
        user = 'root',
        passwd = '',
        database = 'loginpage'
        )
        print(self.connection)
        self.q1 = self.connection.cursor()

run = connecting()