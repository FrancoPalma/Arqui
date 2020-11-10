import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host ="200.14.84.235"
port =5000
sock.connect((host,port))

sock.send('02000sinitsvrut'.encode())
while True:
    data = sock.recv(2010).decode()
    print(data)
    if (data):
        sock.send('02000svrutRutina guardada'.encode())
    else:
        break

sock.close ()
