import socket

port = 5000
server = socket.socket()

server.listen(10)

while True:
    client, clientConnetion = server.accept()

