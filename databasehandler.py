import sqlite3

connection = sqlite3.connect('data_base.db')
c = connection.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS data_base(names TEXT,ages TEXT,phone TEXT,cities TEXT,email TEXT)')
    connection.commit()
create_table()