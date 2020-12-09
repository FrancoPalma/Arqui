#!/usr/bin/env python
# -- coding: utf-8 --
import socket
import sqlite3
import time
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("200.14.84.235", 5000))

print("="*10+"Bienvenido a MrMuscle"+"="*10)
opcion = 0
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
            tipo = int(input(
                "\nEscoja el tipo de rutina:\n 1: Cardio\n 2: Masa muscular \n Ingrese número: "))
            if (tipo == 1 or tipo == 2):
                break
            else:
                print("\nEsta opción no es válida")
        while 1:
            zona_cuerpo = int(input(
                "\nMúsculo predominante en rutina:\n 1: Ninguno\n 2: Piernas y glúteos\n 3: Torso y brazos\n 4: Abdomen y lumbares \nIngrese número: "))
            if (zona_cuerpo == 1 or zona_cuerpo == 2 or zona_cuerpo == 3 or zona_cuerpo == 4):
                break
            else:
                print("\nEsta opción no es válida")

        while 1:
            intensidad = input(
                "\nIntensidad de la rutina:\n 1: Baja\n 2: Media\n 3: Alta \nIngrese número: ")
            if (intensidad == 1 or intensidad == 2 or intensidad == 3):
                break
            else:
                print("Esta opción no es válida")

        while 1:
            tiempo_total = input(
                "\nTiempo de la rutina \nIngrese los minutos a trabajar: ")
            if (tiempo_total > 0 and tiempo_total < 31 and tiempo_total % 1 == 0):
                if (tiempo_total < 10):
                    tiempo_total = "0" + str(tiempo_total)
                break
            else:
                print("Esta opción no es válida")

        data = "00009svrut" + str(tipo) + str(zona_cuerpo) + \
            str(intensidad) + str(tiempo_total)
        s.send(data.encode())
        data = s.recv(1024).decode()
    elif (servicio == "2"):
        data = "00000shows"
        s.send(data.encode())
        while True:
            number = s.recv(1024).decode()
            print("ha llegado:", number)
            if number:
                break
        number = int(number[12:14])
        rutinas = []
        for i in range(number):
            while True:
                data2 = s.recv(1024).decode()
                if data2:
                    print("pare")
                    break
            rutinas.append(data2)
        for rut in rutinas:
            aux = rut[12:]
            aux = aux.split()
            if len(aux) != 0:
                count = "Id de rutina: "+str(aux[0])+", Duración: " + \
                    str(aux[1])+" minutos, Tiempo de actividad: "+str(aux[2]) + \
                    " segundos, Tiempo de descanso: " + \
                    str(aux[3])+" segundos, Zona: "+str(aux[4]) + \
                    ", Intensidad: "+str(aux[5])+"\n"
                print(count)

        while(True):
            print("\nEscoja un servicio")
            print("1. Realizar rutina.")
            print("2. Editar rutina.")
            print("3. Eliminar")
            print("9. Volver atrás.")
            ver = int(input())
            # Realizar
            if ver == 1:
                id = int(input("Indique el id de la rutina: "))
                data = "00090start" + str(id)
                s.send(data.encode())
                count = 0
                while True:
                    data = s.recv(2010).decode()
                    if (data):
                        if(len(data) == 13 or len(data) == 14):
                            print(data[12:])

                        if(count == 0):
                            print(data[12:])
                            count += 1
                        else:
                            print(data[12:len(data)-12])

                        if(data[12:] == "FIN"):
                            print("RUTINA FINALIZADA")
                            break

            # Editar
            elif ver == 2:
                id = input("Indique el id de la rutina")

                data = ""
                while 1:
                    tipo = int(input(
                        "\nEscoja el tipo de rutina:\n 1: Cardio\n 2: Masa muscular \n Ingrese número: "))
                    if (tipo == 1 or tipo == 2):
                        break
                    else:
                        print("\nEsta opción no es válida")
                while 1:
                    zona_cuerpo = int(input(
                        "\nMúsculo predominante en rutina:\n 1: Ninguno\n 2: Piernas y glúteos\n 3: Torso y brazos\n 4: Abdomen y lumbares \nIngrese número: "))
                    if (zona_cuerpo == 1 or zona_cuerpo == 2 or zona_cuerpo == 3 or zona_cuerpo == 4):
                        break
                    else:
                        print("\nEsta opción no es válida")

                while 1:
                    intensidad = input(
                        "\nIntensidad de la rutina:\n 1: Baja\n 2: Media\n 3: Alta \nIngrese número: ")
                    if (intensidad == 1 or intensidad == 2 or intensidad == 3):
                        break
                    else:
                        print("Esta opción no es válida")

                while 1:
                    tiempo_total = input(
                        "\nTiempo de la rutina \nIngrese los minutos a trabajar: ")
                    if (tiempo_total > 0 and tiempo_total < 31 and tiempo_total % 1 == 0):
                        if (tiempo_total < 10):
                            tiempo_total = "0" + str(tiempo_total)
                        break
                    else:
                        print("Esta opción no es válida")
                id = str(id)
                ide = id.zfill(4)
                print(ide)
                data = "00020edirt" + \
                    str(ide) + str(tipo) + str(zona_cuerpo) + \
                    str(intensidad) + str(tiempo_total)
                s.send(data.encode())
                while True:
                    data = s.recv(1024).decode()
                    if(data):
                        print(data)
                        break

            # Eliminar
            elif ver == 3:
                id = str(input("Indique el id de la rutina"))
                data = "00020delrt1"+id
                s.send(data.encode())
                data = s.recv(1024).decode()
                print(data[10:])
            elif ver == 9:
                break
    elif (servicio == "9"):
        break
