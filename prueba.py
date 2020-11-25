import sqlite3

connection = sqlite3.connect('mrmuscle.sqlite')
cursor = connection.cursor()

dato = str(1)

cursor.execute("SELECT * FROM Routine ")
aux = cursor.fetchall()
print(aux)
