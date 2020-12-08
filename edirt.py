#!/usr/bin/env python
# -- coding: utf-8 --
import sqlite3
import socket


def actualizarRutina(cursor, connection, tipo, zona, intensidad, tiempo_total):
    if(zona == "2"):
        zona_cuerpo = "Piernas"
    elif(zona == "3"):
        zona_cuerpo = "Torso"
    elif(zona == "4"):
        zona_cuerpo = "Abdominales"

    if(tipo == "1"):  # caso de carido
        if (int(intensidad) == 1):
            active_time = 20
            rest_time = 40
        elif (int(intensidad) == 2):
            active_time = 30
            rest_time = 30
        else:
            active_time = 40
            rest_time = 20

        routine_id = cursor.execute("INSERT INTO Routine (active_time, rest_time, total_time, type) values (?,?,?,?)", (
            active_time, rest_time, tiempo_total, 0)).lastrowid
        cursor.execute("SELECT id FROM Exercise WHERE ex_zone = 'Otros'")
        ejercicios_generales = cursor.fetchall()
        cursor.execute(
            "SELECT id FROM Exercise WHERE ex_zone=? AND type = '0'", (zona_cuerpo,))
        ejercicios_especificos = cursor.fetchall()
        pos_ejercicios_generales = 0
        pos_ejercicios_especificos = 0
        min_actual = 0
        tiempo_total = int(tiempo_total)

        while min_actual < tiempo_total:

            # si se acaban los ejercicios los utilizo de nuevo
            if (len(ejercicios_generales) == pos_ejercicios_generales):
                pos_ejercicios_generales = 0

            if (len(ejercicios_especificos) == pos_ejercicios_especificos):
                pos_ejercicios_especificos = 0

            if min_actual % 2 != 0:
                cursor.execute("INSERT INTO Routine_exercise (id_routine, id_ex, minute) values (?,?,?)", (
                    routine_id, ejercicios_generales[pos_ejercicios_generales][0], min_actual))
                pos_ejercicios_generales += 1
            else:
                cursor.execute("INSERT INTO Routine_exercise (id_routine, id_ex, minute) values (?,?,?)", (
                    routine_id, ejercicios_especificos[pos_ejercicios_especificos][0], min_actual))
                pos_ejercicios_especificos += 1

            min_actual += 1

        connection.commit()

    elif(tipo == "2"):
        routine_id = cursor.execute(
            "INSERT INTO Routine (active_time, rest_time, total_time, type) values (?,?,?,?)", (30, 30, tiempo_total, 1)).lastrowid
        intensidad_aux = int(intensidad) - 1
        cursor.execute("SELECT id FROM Exercise WHERE ex_zone=? AND (level = ? OR level = ?) AND type = '1'",
                       (zona_cuerpo, intensidad, intensidad_aux))
        ejercicios = cursor.fetchall()
        pos_ejercicios = len(ejercicios) - 1
        min_actual = 0
        tiempo_total = int(tiempo_total)

        while min_actual < tiempo_total:
            if (pos_ejercicios == -1):
                pos_ejercicios = len(ejercicios) - 1

            cursor.execute("INSERT INTO Routine_exercise (id_routine, id_ex, minute) values (?,?,?)",
                           (routine_id, ejercicios[pos_ejercicios][0], min_actual))
            pos_ejercicios -= 1

            min_actual += 1

        connection.commit()


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
        ide = data[10:13]
        ide = int(ide)
        cur.execute('SELECT * FROM Exercises WHERE id=(?)', ide)
        rut = cur.fetchall()
        print(rut)
        if rut:
            print(data)
            tipo = data[14]
            zona_cuerpo = data[15]
            intensidad = data[16]
            tiempo_total = data[17:19]
            sock.send("00050delrt" + ide)

            while True:
                data = sock.recv(2010).decode()
                if(data):
                    break

            sock.send("00050newrt" + data[14:19].encode())

            while True:
                data = sock.recv(2010).decode()
                if(data):
                    break

            print("Rutina actualizada")
            sock.send("00050edirtRutina actualizada".encode())
        else:
            print("No existe dicha rutina, intente nuevamente")
            sock.send('02000selrut')
    else:
        break


sock.close()


conn.commit()
conn.close()
