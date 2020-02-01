import sqlite3
from datetime import datetime

# The db manager
class dbManage:
    def __init__(self, dbFile='test.db'):
        self.conn = sqlite3.connect(self.dbFile)
        self.c = conn.cursor()

    def getDate():
        return datetime.date(datetime.now()).year, datetime.date(datetime.now()).day, datetime.date(datetime.now()).month

conn = sqlite3.connect('test.db')
c = conn.cursor()
# c.execute(
#     '''CREATE TABLE Test (
#     col INTEGER,
#     row INTEGER,
#     x INTEGER,
#     y INTEGER,
#     number of moves INTEGER,
#     options INTEGER,
#     taken_options VARCHAR(4),
#     id VARCHAR(16),
#     year INTEGER,
#     month INTEGER,
#     day INTEGER)
# ''')
# sql_command = """CREATE TABLE emp (
# staff_number INTEGER PRIMARY KEY,
# fname VARCHAR(20),
# lname VARCHAR(30),
# gender CHAR(1),
# joining DATE);"""
# Insert a row of data
year, day, month = getDate()
x, y, cols, rows, idd = 100, 200, 30, 40, 'aafwfa'
command = f'INSERT INTO Test VALUES ({cols}, {rows}, {x}, {y}, 2, 3, LR, {idd}, {year}, {month}, {day})'
c.execute(command)

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
