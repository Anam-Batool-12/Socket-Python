import socket

client = socket.socket()
client.connect(('localhost', 9999))

name = input("Enter your name: ")
client.send(name.encode())

print(client.recv(1024).decode())  # Welcome message from server

while True:
    message = input("Client: ")
    client.send(message.encode())
    if message.lower() == 'exit':
        print("Client is exiting...")
        break

    reply = client.recv(1024).decode()
    print("Server:", reply)

client.close()
print("Client disconnected.")
