import threading
import socket

LocalHost = '127.0.0.1'
port = 42069
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((LocalHost,port))
print('Server is up and listening')
message = server.recvfrom(1024)
client_address = message[1]
str1 = str(message[0].decode())
server.sendto(f"Server: Welcome to the server {str1},may I help you?".encode(), client_address)
def receive() :
    while True :
        try :
            message = server.recvfrom(1024)
            print("{name}: {message}".format(name = str1, message = str(message[0].decode())))
            reply = input('server : ')
            client_address = message[1]
            server.sendto(reply.encode(), client_address) 
        except :
            print("Client has left the server")
        
receive()
