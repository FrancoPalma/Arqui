#!/usr/bin/env python
# -- coding: utf-8 --

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("200.14.84.235",5000))
data = s.recv(2010).decode()

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

        data = "00009newrt"+ str(tipo) + str(zona_cuerpo) + str(intensidad) + str(tiempo_total)
        print(data)
        s.send(data.encode())
        data = s.recv(1024).decode()
    elif (servicio == "2"):
      data = "00000shows"
      print(data)
      s.send(data.encode())
      number = s.recv(1024).decode()
      for i in range(int(number[10:]):
          data = s.recv(1024).decode()
          print(data[10:])
      while(true):
          print("\nEscoja un servicio")
          print("1. Realizar rutina.")
          print("2. Editar rutina.")
          print("9. Volver atrás.")
          if ver == 1:
              print("hola")
          elif ver == 2:
              print("hola")
          elif ver == 9:
              break
    elif (servicio == "9"):
        break

    print(data)
