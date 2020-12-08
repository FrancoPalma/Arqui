#!/usr/bin/env python
# -- coding: utf-8 --

import socket
import sqlite3
import time

def iniciar(m=0,s=0):
    global tiempo_activo
    global tiempo_descanso
    global tiempo_total
    global count
    global sock
    while True:
        time.sleep(1)
        s += 1
        sock.send("00010start"+str(s))
        print(s)
        if s >= 60:
            s=0
            m=m+1

        if(s == tiempo_activo and m != tiempo_total):
            data = "COMENZANDO DESCANSO"
            aux = len(data)
            data = "000"+str(aux)+"start"+data
            sock.send(data.encode())

        if (m == tiempo_descanso and m != tiempo_total):
            data = "EJERCICIO "+str(count+1)+": "+lista_ejercicios[count]
            aux = len(data)
            data = "000"+str(aux)+"start"+data
            sock.send(data.encode())
            count+=1
            tiempo_descanso+=1

        if (count == 0):
            data = "EJERCICIO "+str(count+1)+": "+lista_ejercicios[count]
            aux = len(data)
            data = "000"+str(aux)+"start"+ data
            sock.send(data.encode())
            count+=1
            tiempo_descanso = 1

        """if(s + 10 == tiempo_activo):
            data = "FALTAN 10 SEGUNDOS PARA EL DESCANSO"
            aux = len(data)
            data = "000"+str(aux)+"start"+data
            sock.send(data.encode())

        elif(s + 10 == 60):

            data = "10 SEGUNDOS PARA EL SIGUIENTE EJERCICIO"
            aux = len(data)
            data = "000"+str(aux)+"start"+data
            sock.send(data.encode())"""

        if (m == tiempo_total):
            sock.send("00020startFIN")
            break



sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host ="200.14.84.235"
port =5000
sock.connect((host,port))

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
        id = id[10:]
        lista_ejercicios = []
        cursor.execute('SELECT Exercise.name FROM Exercise, Routine_exercise, Routine WHERE Exercise.id = Routine_exercise.id_ex AND Routine_exercise.id_routine = Routine.id AND Routine.id = ?',(id,))
        rows = cursor.fetchall()
        print(rows)
        for row in rows:
            lista_ejercicios.append(row[0])


        lista_detalle = []
        cursor.execute('SELECT Exercise.detail FROM Exercise, Routine_exercise, Routine WHERE Routine_exercise.id_ex = Exercise.id AND Routine_exercise.id_routine = Routine.id AND Routine.id = ?',(id,))
        rows = cursor.fetchall()
        print(rows)
        for row in rows:
            lista_detalle.append(row[0])

        cursor.execute('SELECT active_time FROM Routine WHERE Routine.id = '+str(id))
        active_time = cursor.fetchall()
        tiempo_activo = active_time[0][0]

        cursor.execute('SELECT rest_time FROM Routine WHERE Routine.id = '+str(id))
        rest_time = cursor.fetchall()
        print(rest_time)
        tiempo_descanso = rest_time[0][0]

        cursor.execute('SELECT total_time FROM Routine WHERE Routine.id = '+str(id))
        total_time = cursor.fetchall()
        print(total_time)
        tiempo_total = total_time[0][0]

        data = "Iniciando la rutina "+str(id)
        aux = len(data)
        data = "000"+str(aux)+"start"+data
        sock.send(data.encode())
        print("LARGO LISTA: " + str(len(lista_ejercicios)))
        iniciar()