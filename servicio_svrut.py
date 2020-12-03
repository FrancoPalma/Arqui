import socket
import sqlite3

def crearRutina(cursor, connection, routine_id, tipo, zona, intensidad, tiempo_total):
    if(zona == "2"):
        zona_cuerpo= "Piernas"
    elif(zona == "3"):
        zona_cuerpo = "Torso"
    elif(zona== "4"):
        zona_cuerpo = "Abdominales"

    if(int(tipo) == 1):                                      #caso de carido
        if (int(intensidad) == 1):
            active_time = 20
            rest_time = 40
        elif (int(intensidad) == 2):
            active_time = 30
            rest_time = 30
        else:
            active_time = 40
            rest_time = 20

        routine_id = cursor.execute("INSERT INTO Routine (active_time, rest_time, total_time, type) values (?,?,?,?)", (active_time, rest_time, tiempo_total, 0)).lastrowid
        cursor.execute("SELECT id FROM Exercise WHERE ex_zone = 'Otros'")
        ejercicios_generales = cursor.fetchall()
        cursor.execute("SELECT id FROM Exercise WHERE ex_zone=? AND type = '0'", (zona_cuerpo,))
        ejercicios_especificos = cursor.fetchall()
        pos_ejercicios_generales = 0
        pos_ejercicios_especificos = 0
        min_actual = 0
        tiempo_total = int(tiempo_total)

        while min_actual < tiempo_total:

            if (len(ejercicios_generales) == pos_ejercicios_generales):  #si se acaban los ejercicios los utilizo de nuevo
                pos_ejercicios_generales = 0

            if (len(ejercicios_especificos) == pos_ejercicios_especificos):
                pos_ejercicios_especificos = 0

            if min_actual % 2 != 0:
                cursor.execute("INSERT INTO Routine_exercise (id_routine, id_ex, minute) values (?,?,?)", (routine_id, ejercicios_generales[pos_ejercicios_generales][0], min_actual))
                pos_ejercicios_generales += 1
            else:
                cursor.execute("INSERT INTO Routine_exercise (id_routine, id_ex, minute) values (?,?,?)", (routine_id, ejercicios_especificos[pos_ejercicios_especificos][0], min_actual))
                pos_ejercicios_especificos += 1

            min_actual += 1

        connection.commit()

    elif(int(tipo) == 2):
        routine_id = cursor.execute("INSERT INTO Routine (active_time, rest_time, total_time, type) values (?,?,?,?)", (30, 30, tiempo_total, 1)).lastrowid
        intensidad_aux = int(intensidad) - 1
        cursor.execute("SELECT id FROM Exercise WHERE ex_zone=? AND (level = ? OR level = ?) AND type = '1'", (zona_cuerpo, intensidad, intensidad_aux ))
        ejercicios = cursor.fetchall()
        print(ejercicios)
        pos_ejercicios = len(ejercicios) - 1
        min_actual = 0
        tiempo_total = int(tiempo_total)

        while min_actual < tiempo_total:
            print("test 1")
            if (pos_ejercicios == -1):
                pos_ejercicios = len(ejercicios) - 1

            cursor.execute("INSERT INTO Routine_exercise (id_routine, id_ex, minute) values (?,?,?)", (routine_id, ejercicios[pos_ejercicios][0], min_actual))
            print("test 2")
            pos_ejercicios -= 1

            min_actual += 1

        connection.commit()



sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host ="200.14.84.235"
port =5000
sock.connect((host,port))

sock.send('02000sinitsvrut'.encode())
data = sock.recv(2010).decode()
if(data):
    print(data)

connection = sqlite3.connect('mrmuscle.sqlite')
cursor = connection.cursor()

while True:
        data = sock.recv(2010).decode()
        if (data):
            routine_id = data[10:15]
            tipo = data[10]
            zona_cuerpo = data[11]
            intensidad = data[12]
            tiempo_total = data[13:15]
            crearRutina(cursor, connection, routine_id, tipo, zona_cuerpo, intensidad, tiempo_total)
            sock.send("00050svrut".encode())


sock.close ()
conn.close()
