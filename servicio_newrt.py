import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host ="200.14.84.235"
port =5000
sock.connect((host,port))

sock.send('02000sinitnewrt'.encode())
data = sock.recv(2010).decode()
if(data):
    print(data)
while True:
        data = sock.recv(2010).decode()
        if (data):
            print(data)
            tipo = data[10]
            zona_cuerpo = data[11]
            intensidad = data[12]
            tiempo_total = data[13:15]
            tiempo_activo = data[15:16]
            tiempo_descanso = data[16:17]
            sock.send('02000newrtRutina creada'.encode())
            sock.send('02000svrut123456789')
            data = sock.recv(2010)
            print(data)
        else:
            break
sock.close ()
