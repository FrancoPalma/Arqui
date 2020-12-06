import socket

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

cursor.execute('SELECT * FROM Routine')
rows = cursor.fetchall()
for row in rows:
    print(row)
