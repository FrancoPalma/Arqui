import socket
import sqlite3
import time
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host ="200.14.84.235"
port =5000
sock.connect((host,port))

sock.send('02000sinitshows'.encode())
data = sock.recv(2010).decode()
if(data):
    print(data)
connection = sqlite3.connect('mrmuscle.sqlite')
cursor = connection.cursor()
while 1:
    data = sock.recv(2010).decode()
    cursor.execute('SELECT * FROM Routine')
    rows = cursor.fetchall()
    for i in range(len(rows)):
        rutina = ""
        for j in rows[i]:
            rutina += " " + str(j)
        data = '01000shows' + rutina
        sock.send(data.encode())
        data = sock.recv(2010).decode()
    sock.send("FIN".encode())
