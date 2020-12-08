#!/usr/bin/env python
# -- coding: utf-8 --
import sqlite3
import socket

conn = sqlite3.connect('mrmuscle.sqlite')
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
        ide = data[10:15]
        ide = int(ide)
        print(ide)
        cur.execute('SELECT * FROM Exercise WHERE id=?', (ide,))
        rut = cur.fetchall()
        print(rut)
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

            delrt = "02000delrt"+ str(ide)
            s.send(delrt.encode())
            while True:
                data = sock.recv(2010).decode()
                if(data):
                    break
            new_rut = "00009newrt" + str(tipo) + str(zona_cuerpo) + str(intensidad) + str(
                tiempo_total) + str(tiempo_activo) + str(tiempo_descanso)
            s.send(new_rut.encode())
        else:
            print("No existe dicha rutina, intente nuevamente")
            sock.send('02000selrut')
    else:
        break


sock.close()


conn.commit()
conn.close()
