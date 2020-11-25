import sqlite3
import socket

conn = sqlite3.connect('hashes_4.sqlite')
cur = conn.cursor()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "200.14.84.235"
port = 5000
sock.connect((host, port))
sock.send('02000sinitedirt'.encode())
data = sock.recv(2010).decode()
if(data):
    print(data)

while True:
    data = sock.recv(2010).decode()

    if (data):
        print(data)
        ide = data[10:17]
        ide = int(ide)
        cur.execute('SELECT * FROM Exercises WHERE id=(?)', ide)
        rut = cur.fetchall()
        if rut:
            new_rut = ""
            tipo = input(
                "Escoja el tipo de rutina:\n 1: Cardio\n 2: Masa muscular \n Ingrese número: ")
            zona_cuerpo = input(
                "Músculo predominante en rutina:\n 1: Ninguno\n 2: Piernas y glúteos\n 3: Torso y brazos\n 4: Abdomen y lumbares \nIngrese número: ")
            intensidad = input(
                "Escoja la intensidad:\n 1: Baja\n 2: Media\n 3: Alta\n Ingrese número: ")
            tiempo_total = input(
                "Ingrese la cantidad de minutos que desee que dure la rutina: ")
            tiempo_activo = input(
                "Ingrese la cantidad de segundos de tiempo activo por ejercicio: ")
            tiempo_descanso = input(
                "Ingrese la cantidad de segundos para descansar entre ejercicios: ")
            new_rut = "00009updrt" + str(tipo) + str(zona_cuerpo) + str(intensidad) + str(
                tiempo_total) + str(tiempo_activo) + str(tiempo_descanso)
            # hay que llamar a eliminar rutina con el id ide
            # hay que llamar a crear rutina, que a su vez implica un nuevo servicio que verifique que si la rutina nueva ya existe
            s.send(new_rut.encode())
        else:
            print("No existe dicha rutina, intente nuevamente")
            sock.send('02000selrut')
    else:
        break


sock.close()


conn.commit()
conn.close()
