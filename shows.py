import socket
import sqlite3
import time
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "200.14.84.235"
port = 5000
sock.connect((host, port))

sock.send('02000sinitshows'.encode())
data = sock.recv(2010).decode()
if data:
    print(data)
connection = sqlite3.connect('mrmuscle.sqlite')
cursor = connection.cursor()
while True:
    data = sock.recv(2010).decode()
    if data:
        #cursor.execute("SELECT Routine.id, Exercise.ex_zone, Exercise.level FROM Routine, Routine_exercise, Exercise WHERE  Routine.id = Routine_exercise.id_routine AND Routine_exercise.id_ex = Exercise.id")
        cursor.execute("SELECT Routine.id, Routine.total_time, Routine.active_time, Routine.rest_time,  Exercise.ex_zone, max(Exercise.level) as intensidad, Routine.type FROM Routine, Routine_exercise, Exercise WHERE  Routine.id = Routine_exercise.id_routine AND Routine_exercise.id_ex = Exercise.id GROUP BY Routine.id, Exercise.ex_zone")
        rows = cursor.fetchall()
        sock.send('00055shows'+str(len(rows)).encode())
        time.sleep(0.5)
        for i in range(len(rows)):
            rutina = ""
            for j in rows[i]:
                rutina += " " + str(j)
            print(rutina)
            data = '01000shows' + rutina
            sock.send(data.encode())
            time.sleep(0.3)
        print("termine de pana")

sock.close()
conn.close()
