import socket
import threading
from datetime import datetime

def handle_client(client_socket, username):
    while True:
        client_text = client_socket.recv(1024).decode('utf-8')
        if not client_text or client_text.lower() == 'exit':
            break

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{timestamp} {username}: {client_text}")

        server_response = input("Reply: ")
        client_socket.send(server_response.encode('utf-8'))

    print(f"Connection with {username} closed.")
    client_socket.close()

server_ip = '127.0.0.1'
server_port = 54321

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))
server_socket.listen(5)
print(f"Server is listening {server_ip}:{server_port}")

while True:
    client_socket, client_address = server_socket.accept()
    username = client_socket.recv(1024).decode('utf-8')
    print(f"{username} connected.")

    client_thread = threading.Thread(target=handle_client, args=(client_socket, username))
    client_thread.start()
