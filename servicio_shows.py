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
sock.send('00055shows'+str(len(rows)).encode())
for i in range(len(rows)):
    sock.send('01000shows'+str(1+i)+") "+rows[i])
sock.send('00055showsListo'.encode())
