import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor()

# Query all data based on condition
cursor.execute("SELECT * FROM events WHERE date='2088.10.15'")
rows = cursor.fetchall()
print(rows)

# Query certain data
cursor.execute("SELECT band,date FROM events WHERE date='2088.10.15'")
rows = cursor.fetchall()
print(rows)

# insert new rows
new_rows = [('Cats', 'Cat City', '2088.10.17'),
            ('Hens', 'Hen City', '2088.10.17')]

cursor.executemany("INSERT INTO events VALUES(?,?,?)", new_rows)
connection.commit()

# Query all data
cursor.execute("SELECT * FROM events")
rows = cursor.fetchall()
print(rows)
