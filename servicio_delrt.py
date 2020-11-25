import socket

def delete_task(conn, id):
    cur = conn.cursor()
    cur.execute('DELETE FROM Routine WHERE id='+id))
    conn.commit()

def delete_all_tasks(conn):
    cur = conn.cursor()
    cur.execute('DELETE FROM Routine')
    conn.commit()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("200.14.84.235",5000))
sock.send('02000sinitdelrt'.encode())
data = sock.recv(2010).decode()

try:
    con = sqlite3.connect('Arqui.bd')
    print("Connection is established: Database is created in memory")
except Error:
    print(Error)

if data[10] = '1':
    delete_task(con,data[11:])
elif data[10] = '2':
    delete_all_tasks(con)
