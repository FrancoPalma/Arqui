import socket
import sqlite3

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host ="200.14.84.235"
port =5000
sock.connect((host,port))

sock.send('00005sinitnewrt'.encode())
data = sock.recv(2010).decode()
if(data):
    print(data)

connection = sqlite3.connect('mrmuscle.sqlite')
cursor = connection.cursor()

while True:
        data = sock.recv(2010).decode()
        if(data):
            routine_id = data[10:15]
            print(routine_id)
            cursor.execute("SELECT * FROM Routine?", (routine_id,))
            routine = cursor.fetchall()
            if(len(routine) == 0 or routine == None):
                data = "00009svrut" + str(data[10:15])
                sock.send(data.encode())
            else:
                print("Rutina ya existe")
                sock.send("00030newrtEsta rutina ya existe.".encode())

sock.close ()
conn.close()
