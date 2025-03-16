import socket
import threading

host = "127.0.0.1"
port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(5)

print("Server is waiting for connections...")

clients = []  # List to store active clients
lock = threading.Lock()

def handle_client(client, addr):
    """Handles communication with a single client."""
    name = client.recv(1024).decode()
    print(f"{name} ({addr}) has joined the chat.")
    client.send(f"Welcome {name} to the chat room!".encode())

    while True:
        try:
            message = client.recv(1024).decode()
            if not message:
                break  # If message is empty, assume client disconnected
            if message.lower() == 'exit':
                print(f"{name} has left the chat.")
                client.send("Goodbye!".encode())
                break

            print(f"{name}: {message}")
            reply = input(f"Reply to {name}: ")  # Server responds to the client
            client.send(reply.encode())

        except:
            break

    with lock:
        clients.remove(client)  # Remove disconnected client
    client.close()
    print(f"Connection closed with {name} ({addr})")

while True:
    client, addr = server.accept()
    with lock:
        clients.append(client)
    threading.Thread(target=handle_client, args=(client, addr), daemon=True).start()
