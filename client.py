import socket
from datetime import datetime

server_ip = '127.0.0.1'
server_port = 54321

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))

username = input("Enter your username: ")
client_socket.send(username.encode('utf-8'))

while True:
    client_text = input("Type a message (type 'bye' to end the conversation): ")
    client_socket.send(client_text.encode('utf-8'))

    if client_text.lower() == 'bye':
        break

    server_response = client_socket.recv(1024).decode('utf-8')
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{timestamp} Server replied: {server_response}")

print("Connection Closed!")
client_socket.close()
