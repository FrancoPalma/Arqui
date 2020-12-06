from tkinter import Tk,Label,Button,Frame
import socket
import sqlite3
import time
import winsound

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host ="200.14.84.235"
port =5000
s.connect((host,port))

s.send('02000sinitstart'.encode())

def iniciar(m=0,s=0):
    global active_time
    global rest_time
    global total_time
    global count
  
    while True:
        if s >= 60:
            s=0
            m=m+1


        if(s == active_time and m != total_time):
            data = "COMENZANDO DESCANSO"
            aux = len(data)
            data = "000"+str(aux)+"start"+data
            s.send(data.encode())

        if (m == rest_time):
            data = "Ejercicio "+str(count+1)+": "+lista_ejercicios[count]
            aux = len(data)
            data = "000"+str(aux)+"start"+data
            s.send(data.encode())
            count+=1
            rest_time+=1

        if (count == 0):
            data = "EJERCICIO "+str(count+1)+": "+lista_ejercicios[count]
            aux = len(data)
            data = "000"+str(aux)+"start"+data
            s.send(data.encode())
            count+=1
            rest_time = 1

        if(s + 10 == active_time):
            data = "FALTAN 10 SEGUNDOS PARA EL DESCANSO"
            aux = len(data)
            data = "000"+str(aux)+"start"+data
            s.send(data.encode())

        elif(s + 10 == 60):

            data = "10 SEGUNDOS PARA EL SIGUIENTE EJERCICIO"
            aux = len(data)
            data = "000"+str(aux)+"start"+data
            s.send(data.encode())

        if (m == total_time):

            data = "HAS TERMINADO LA RUTINA"
            aux = len(aux)
            data = "000"+str(aux)+"start"+data
            s.send(data.encode())




while True:
    
    id = s.recv(2010).decode()


    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    

    lista_ejercicios = []
    cursor.execute('SELECT name FROM Exercise, Routine_exercise, Routine WHERE id_exercise.Routine_exercise = id.Exercise AND '+str(id)+'= id_routine.Routine_exercise ')
    rows = cursor.fetchall()

    for row in rows:
        lista_ejercicios.append(row[0])
    

    lista_detalle = []
    cursor.execute('SELECT detail FROM Exercise, Routine_exercise, Routine WHERE id_exercise.Routine_exercise = id.Exercise AND '+str(id)+'= id_routine.Routine_exercise ')
    rows = cursor.fetchall()

    for row in rows:
        lista_detalle.append(row[0])    

    cursor.execute('SELECT active_time FROM Routine WHERE id.Routine = '+str(id))
    active_time = cursor.fetchall()
    active_time = active_time[0]

    cursor.execute('SELECT rest_time FROM Routine WHERE id.Routine = '+str(id))
    rest_time = cursor.fetchall()
    rest_time = rest_time[0]

    cursor.execute('SELECT total_time FROM Routine WHERE id.Routine = '+str(id))
    total_time = cursor.fetchall()
    total_time = total_time[0]

    data = "Iniciando la rutina "+str(id)
    aux = len(data)
    data = "000"+str(aux)+"start"+data
    s.send(data.encode())

    iniciar()