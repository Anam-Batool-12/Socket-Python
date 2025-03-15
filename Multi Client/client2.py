import socket
from _thread import *

c = socket.socket()
host = '127.0.0.1'
port = 12345
threadCount = 0
print('Waiting for a Connection..')

try:
    c.connect((host, port))
except socket.error as e:
    print(str(e))

response = c.recv(2048)
print(response.decode('utf-8'))

while True:
    user_input = input('Say Something: ')
    c.send(str.encode(user_input))
    response = c.recv(2048)
    print(response.decode('utf-8'))
