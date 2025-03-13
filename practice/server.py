import socket

s = socket.socket()
print("Socket successfully created")

s.bind(('localhost', 9999))
s.listen(3)
print("socket is waiting for connection")

c, addr = s.accept()
print("Got connection from", addr)


name = c.recv(1024).decode()
print("Client:", name)
c.send("Hello, I am server".encode())


while True:

    message = c.recv(1024).decode()
    if message.lower() == 'exit':
        print("Client is exiting")
        break
    print("Client:", message)

    replay = input("Server: ")
    c.send(replay.encode())

s.close()
c.close()



