import sqlite3

connection = sqlite3.connect('mrmuscle.sqlite')
cursor = connection.cursor()

cursor.execute("DROP TABLE Exercise")
cursor.execute("DROP TABLE Routine_exercise")
cursor.execute("DROP TABLE Routine")
connection.commit()
