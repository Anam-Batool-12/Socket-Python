import socket
from _thread import *

s = socket.socket()
host = '127.0.0.1'
port = 12345
threadCount = 0

try:
    s.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waiting for a Connection..')
s.listen(5)

def client_thread(connection):
    connection.send(str.encode('Welcome to the Server\n'))
    while True:
        data = connection.recv(2048)
        if not data:
            break
        reply = 'Server Says: ' + data.decode('utf-8')
        connection.sendall(str.encode(reply))
    connection.close()

while True:
    client, addr = s.accept()
    print('Connected to: ' + addr[0] + ':' + str(addr[1]))
    start_new_thread(client_thread, (client,))
    threadCount += 1
    print('Thread Number: ' + str(threadCount))

