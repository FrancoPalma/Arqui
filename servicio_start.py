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
    print(tiempo_activo)
    print(tiempo_descanso)
    while True:
        time.sleep(1)
        s += 1
        print(s)
        if s >= 60:
            s=0
            m=m+1

        if(s == tiempo_activo and m != tiempo_total):
            data = "COMENZANDO DESCANSO"
            aux = len(data)
            data = "000"+str(aux)+"start"+data
            #s.send(data.encode())
            print(data)

        if (m == tiempo_descanso):
            data = "Ejercicio "+str(count+1)+": "+lista_ejercicios[count]
            aux = len(data)
            data = "000"+str(aux)+"start"+data
            #s.send(data.encode())
            print(data)
            count+=1
            tiempo_descanso+=1

        if (count == 0):
            data = "EJERCICIO "+str(count+1)+": "+lista_ejercicios[count]
            aux = len(data)
            data = "000"+str(aux)+"start"+data
            #s.send(data.encode())
            print(data)
            count+=1
            tiempo_descanso = 1

        if(s + 10 == tiempo_activo):
            data = "FALTAN 10 SEGUNDOS PARA EL DESCANSO"
            aux = len(data)
            data = "000"+str(aux)+"start"+data
            #s.send(data.encode())
            print(data)

        elif(s + 10 == 60):

            data = "10 SEGUNDOS PARA EL SIGUIENTE EJERCICIO"
            aux = len(data)
            data = "000"+str(aux)+"start"+data
            #s.send(data.encode())
            print(data)

        if (m == tiempo_total):

            data = "HAS TERMINADO LA RUTINA"
            aux = len(aux)
            data = "000"+str(aux)+"start"+data
            #s.send(data.encode())
            print(data)



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host ="200.14.84.235"
port =5000
s.connect((host,port))

s.send('02000sinitstart'.encode())
data = s.recv(2010).decode()
if(data):
    print(data)

conn = sqlite3.connect('mrmuscle.sqlite')
cursor = conn.cursor()

count = 0

while True:

    """id = s.recv(2010).decode()
    if(id):"""
    id = 3

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
    #s.send(data.encode())

    iniciar()
