import sqlite3

connection = sqlite3.connect('movies.db')

cursor = connection.cursor()

# cursor.execute("INSERT INTO Movies VALUES ('Taxi Driver', 'Martin Scorsese', 1976) ")

# cursor.execute("SELECT * FROM Movies")

famousFilms = [('Pulp Fiction', 'Tarantino', 1994),
               ('Back to the Future', 'Spielberg', 1985),
               ('Moonrise Kingdom', 'Anderson', 2012)]
# first insert data into Movies DB
cursor.executemany('Insert INTO Movies VALUES (?,?,?)', famousFilms)

# second call data from Movies DB and put in records variable
records = cursor.execute("SELECT * FROM Movies")

# use fetchall
print(cursor.fetchall())

# use for loop
for record in records:
    print(record)


connection.commit()
connection.close()
