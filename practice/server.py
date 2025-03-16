import socket

c = socket.socket()
c.connect(('localhost', 9999))

name = input("Enter your name: ")
c.send(name.encode())


print(c.recv(1024).decode())

while True:
    message = input("Client: ")
    c.send(message.encode())
    if message.lower() == 'exit':
        print("Client is exiting")
        break

    replay = c.recv(1024).decode()
    print("Server:", replay)


c.close()