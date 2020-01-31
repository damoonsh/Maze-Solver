import sqlite3
from datetime import datetime
conn = sqlite3.connect('test.db')
c = conn.cursor()
# c.execute('''CREATE TABLE Deadends (col, row, number of moves, options, paths tried)''')

# Insert a row of data
c.execute("INSERT INTO Deadends VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()