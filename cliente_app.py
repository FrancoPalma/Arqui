#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host ="200.14.84.235"
port =5000
s.connect((host,port))
print("Conectado al bus")

while True:
    print("\nEscoja un servicio")
    print("1. Crear rutina")
    print("2. Ver rutinas guardadas")
    print("9. Salir")
    servicio = input("Ingrese un numero: ")
    servicio = str(servicio)
    if(servicio == "1"):
        data = ""
        tipo = input("Escoja el tipo de rutina:\n 1: Cardio\n 2: Masa muscular \n Ingrese número: ")
        zona_cuerpo = input("Músculo predominante en rutina:\n 1: Ninguno\n 2: Piernas y glúteos\n 3: Torso y brazos\n 4: Abdomen y lumbares \nIngrese número: ")
        intensidad = input("Escoja la intensidad:\n 1: Baja\n 2: Media\n 3: Alta\n Ingrese número: ")
        tiempo_total = input("Ingrese la cantidad de minutos que desee que dure la rutina: ")
        tiempo_activo = input("Ingrese la cantidad de segundos de tiempo activo por ejercicio: ")
        tiempo_descanso = input("Ingrese la cantidad de segundos para descansar entre ejercicios: ")
        data = "00009newrt"+ str(tipo) + str(zona_cuerpo) + str(intensidad) + str(tiempo_total) + str(tiempo_activo) + str(tiempo_descanso)
        s.send(data.encode())

    elif (servicio == "9"):
        break

    data = s.recv(1024).decode()
    print(data)
    s.close ()
