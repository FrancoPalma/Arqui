import socket
import sqlite3
import time


def iniciar(tiempo_activo, tiempo_descanso, tiempo_total, lista_ejercicios, lista_detalle, sock):
    segundo_actual = 0
    minuto_actual = 0
    pos_lista = 0
    print(lista_ejercicios)
    print(lista_detalle)
    while (minuto_actual < tiempo_total):
        while(segundo_actual < tiempo_activo):
            if(segundo_actual == 0):
                data = "00300startEJERCICIO "+str(lista_ejercicios[pos_lista])
                print(data)
                sock.send( data.encode() )
            segundo_actual += 1
            data = "00010start"+str(segundo_actual)
            sock.send(data.encode())

        segundo_actual = 0
        while(segundo_actual < tiempo_descanso):
            if(segundo_actual == 0):
                data = "00300startCOMIENZA EL DESCANSO"
                sock.send( data.encode() )
            segundo_actual += 1
            data = "00010start"+str(segundo_actual)
            sock.send(data.encode())
        segundo_actual = 0
        minuto_actual += 1
        pos_lista += 1

    sock.send("00020startFIN".encode())


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "200.14.84.235"
port = 5000
sock.connect((host, port))

sock.send('02000sinitstart'.encode())
data = sock.recv(2010).decode()
if(data):
    print(data)

conn = sqlite3.connect('mrmuscle.sqlite')
cursor = conn.cursor()

count = 0

while True:

    id = sock.recv(2010).decode()
    if(id):
        id = 4 #id[10:]
        lista_ejercicios = []
        cursor.execute('SELECT Exercise.name FROM Exercise, Routine_exercise, Routine WHERE Exercise.id = Routine_exercise.id_ex AND Routine_exercise.id_routine = Routine.id AND Routine.id = ?', (id,))
        rows = cursor.fetchall()
        print(rows)
        for row in rows:
            lista_ejercicios.append(row[0])

        print("LARGO DE LISTA: ", len(lista_ejercicios))
        lista_detalle = []
        cursor.execute('SELECT Exercise.detail FROM Exercise, Routine_exercise, Routine WHERE Routine_exercise.id_ex = Exercise.id AND Routine_exercise.id_routine = Routine.id AND Routine.id = ?', (id,))
        rows = cursor.fetchall()
        print(rows)
        for row in rows:
            lista_detalle.append(row[0])


        cursor.execute(
            'SELECT active_time, rest_time, total_time FROM Routine WHERE Routine.id = '+str(id))
        time = cursor.fetchall()
        tiempo_activo = int(time[0][0])
        tiempo_descanso = int(time[0][1])
        tiempo_total = int(time[0][2])

        iniciar(tiempo_activo, tiempo_descanso, tiempo_total, lista_ejercicios, lista_detalle, sock)
        count = 0
