import socket

HOST = '192.168.XXXXX'
PORT = 9293

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP 
socket.connect((HOST, PORT))

socket.send("Hello World".encode('utf-8'))
print(socket.recv(548))
