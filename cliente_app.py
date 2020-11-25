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
        while 1:
            tipo = input("Escoja el tipo de rutina:\n 1: Cardio\n 2: Masa muscular \n Ingrese número: ")
            if ( tipo == 1 or tipo == 2 ):
                break
            else:
                print("Esta opción no es válida")

        while 1:
            zona_cuerpo = input("Músculo predominante en rutina:\n 1: Ninguno\n 2: Piernas y glúteos\n 3: Torso y brazos\n 4: Abdomen y lumbares \nIngrese número: ")
            if ( zona_cuerpo == 1 or zona_cuerpo == 2 or zona_cuerpo == 3 or zona_cuerpo == 4):
                break
            else:
                print("Esta opción no es válida")

        while 1:
            intensidad = input("Intensidad de la rutina:\n 1: Baja\n 2: Media\n 3: Alta \nIngrese número: ")
            if ( intensidad == 1 or intensidad == 2 or intensidad == 3):
                break
            else:
                print("Esta opción no es válida")

        while 1:
            tiempo_total = input("Tiempo de la rutina \nIngrese número: ")
            if ( tiempo_total > 0 and tiempo_total < 31 and tiempo_total % 1 == 0 ):
                if (tiempo_total < 10):
                    tiempo_total = "0"+ str(tiempo_total)
                break
            else:
                print("Esta opción no es válida")

        data = "00009newrt"+ str(tipo) + str(zona_cuerpo) + str(intensidad) + str(tiempo_total)
        s.send(data.encode())

    elif (servicio == "9"):
        break

s.close ()
