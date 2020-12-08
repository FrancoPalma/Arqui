#!/usr/bin/env python
# -- coding: utf-8 --
import socket
import sqlite3
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("200.14.84.235",5000))

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
            tipo = int(input("\nEscoja el tipo de rutina:\n 1: Cardio\n 2: Masa muscular \n Ingrese número: "))
            if ( tipo == 1 or tipo == 2 ):
              break
            else:
                print("\nEsta opción no es válida")
        while 1:
            zona_cuerpo = int(input("\nMúsculo predominante en rutina:\n 1: Ninguno\n 2: Piernas y glúteos\n 3: Torso y brazos\n 4: Abdomen y lumbares \nIngrese número: "))
            if ( zona_cuerpo == 1 or zona_cuerpo == 2 or zona_cuerpo == 3 or zona_cuerpo == 4):
                break
            else:
                print("\nEsta opción no es válida")

        while 1:
            intensidad = input("\nIntensidad de la rutina:\n 1: Baja\n 2: Media\n 3: Alta \nIngrese número: ")
            if ( intensidad == 1 or intensidad == 2 or intensidad == 3):
                break
            else:
                print("Esta opción no es válida")

        while 1:
            tiempo_total = input("\nTiempo de la rutina \nIngrese los minutos a trabajar: ")
            if ( tiempo_total > 0 and tiempo_total < 31 and tiempo_total % 1 == 0 ):
                if (tiempo_total < 10):
                    tiempo_total = "0"+ str(tiempo_total)
                break
            else:
                print("Esta opción no es válida")

        data = "00009svrut"+ str(tipo) + str(zona_cuerpo) + str(intensidad) + str(tiempo_total)
        s.send(data.encode())
        data = s.recv(1024).decode()
    elif (servicio == "2"):
        data = "00000shows"
        s.send(data.encode())
        number = s.recv(1024).decode()
        number = int(number[12:])
        rutinas = []
        for i in range(number):
            rutinas.append(s.recv(1024).decode())
        for rut in rutinas:
            imprimir = rut[12:]
            imprimir = imprimir.split()
            cout = imprimir[0]

            if imprimir[1] == "1":
                cout += "| Cardio |"
            else:
                cout += "| Masa Muscular |"

            if imprimir[2] == "1":
                cout += " Ninguno |"
            elif imprimir[2] == "2":
                cout += " Piernas y glúteos |"
            elif imprimir[2] == "3":
                cout += " Torso y brazos |"
            elif imprimir[2] == "4":
                cout += " Abdomen y lumbares |"

            if imprimir[3] == "1":
                cout += " Baja |"
            elif imprimir[3] == "2":
                cout += " Media |"
            elif imprimir[3] == "3":
                cout += " Alta |"

            cout += "Tiempo: "+imprimir[4]+" min|"
            print(cout)

        while(True):
            print("\nEscoja un servicio")
            print("1. Realizar rutina.")
            print("2. Editar rutina.")
            print("3. Eliminar")
            print("9. Volver atrás.")
            ver = int(input())
            #Realizar
            if ver == 1:
                id = int(input("Indique el id de la rutina: "))
                data = "00090start"+ str(id)
                s.send(data.encode())

                while True:
                    data = s.recv(2010).decode()
                    if(data):
                        data = data[12:]
                        if(data[12:21] == "EJERCICIO"):
                            print(data)
                        elif(len(data) > 2):
                            data1 = data[0:2]
                            data2 = data[12:]
                            if data2 == "FIN":
                                print("HAZ TERMINADO LA RUTINA")
                                break
                            else:
                                print(data1 + "     " + data2)
                        else:
                            print(data)

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

            #Eliminar
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
