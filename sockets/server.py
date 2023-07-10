import socket

HOST = '192.168.XXXX'
PORT = 9293

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP 
server.bind((HOST, PORT))

server.listen(6)

while True:
    communication_socket, address = server.accept()
    print(f"Connected to {address}")
    message = communication_socket.recv(548).decode('utf-8')
    print(f"Message from client is {message}")
    communication_socket.send(f"Got your message, thanks".encode('utf-8'))
    communication_socket.close()
    print(f"Connection with {address} ended!")

