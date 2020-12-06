from tkinter import Tk,Label,Button,Frame
import socket
import sqlite3
import time
import winsound
'''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host ="200.14.84.235"
port =5000
s.connect((host,port))

s.send('02000sinitstart'.encode())
'''
def iniciar(m=0,s=0):
    global proceso
    global active_time
    global rest_time
    global total_time
    global count
  

    if s >= 60:
        s=0
        m=m+1

    if (s == active_time and m != total_time):
        winsound.Beep(1000,1000)
        etiqueta = Label(root, text = "Comenzando descanso",font = "times 24 bold", fg = "blue")
        etiqueta.pack()

    if (m == rest_time):
        winsound.Beep(1000,1000)
        etiqueta = Label(root, text = "Ejercicio "+str(count+1)+": "+lista_ejercicios[count],font = "times 24 bold", fg = "green")
        etiqueta.pack()
        etiqueta = Label(root, text = "Descripción: "+lista_detalle[count],font = "times 24 bold", fg = "green")
        etiqueta.pack()
        count+=1

        

    if (count == 0):
        winsound.Beep(1000,1000)
        rest_time = 1
        etiqueta = Label(root, text = "Comenzando rutina",font = "times 24 bold", fg = "blue")
        etiqueta.pack()        
        etiqueta = Label(root, text = "Ejercicio "+str(count+1)+": "+lista_ejercicios[count],font = "times 24 bold", fg = "green")
        etiqueta.pack()
        etiqueta = Label(root, text = "Descripción: "+lista_detalle[count],font = "times 24 bold", fg = "green")
        etiqueta.pack()
        count+=1

    if (m == total_time):
        etiqueta = Label(root, text = "Has terminado la rutina",font = "times 24 bold", fg = "blue")
        etiqueta.pack()
        winsound.Beep(1000,1000)
        time.sleep(5)
        root.destroy()
 
    else:
        times['text'] = str(m)+":"+str(s)
        proceso=times.after(1000, iniciar, (m), (s+1))



while True:
    '''
    id = s.recv(2010).decode()


    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    

    lista_ejercicios = []
    cursor.execute('SELECT name FROM exercise, routine_exercise, routine WHERE id_exercise.routine_exercise = id.exercise AND '+str(id)+'= id_routine.routine_exercise ')
    rows = cursor.fetchall()

    for row in rows:
        lista_ejercicios.append(row[0])
    

    lista_detalle = []
    cursor.execute('SELECT detail FROM exercise, routine_exercise, routine WHERE id_exercise.routine_exercise = id.exercise AND '+str(id)+'= id_routine.routine_exercise ')
    rows = cursor.fetchall()

    for row in rows:
        lista_detalle.append(row[0])    

    cursor.execute('SELECT active_time FROM routine WHERE id.routine = '+str(id))
    active_time = cursor.fetchall()
    active_time = active_time[0]

    cursor.execute('SELECT rest_time FROM routine WHERE id.routine = '+str(id))
    rest_time = cursor.fetchall()
    rest_time = rest_time[0]

    cursor.execute('SELECT total_time FROM routine WHERE id.routine = '+str(id))
    total_time = cursor.fetchall()
    total_time = total_time[0]

    cursor.execute('SELECT type FROM routine WHERE id.routine = '+str(id))
    types = cursor.fetchall()
    types = types[0]
    
    count = 0
    proceso = 0
    inicio = 0

    lista_ejercicios = ['hola','mundo','xd']
    lista_detalle = ['aloh','donmu','dx']

    root = Tk()
    root.title('Cronometro')
 
    times = Label(root, fg='red', width=20, font=("","18"))
    times.pack()
    
    iniciar()
 
    root.mainloop()
'''
count = 0
proceso = 0
inicio = 0
active_time = 30
rest_time = 30
total_time = 2

lista_ejercicios = ['hola','mundo','xd']
lista_detalle = ['aloh','donmu','dx']

root = Tk()
root.title('Cronometro')
 
times = Label(root, fg='red', width=20, font=("","18"))
times.pack()
    
iniciar()
 
root.mainloop()