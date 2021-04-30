import socket
import threading 
nickname = input("Nickname: ").encode()
localIP = '127.0.0.1'
localPort = 42069
ClientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Connected to the server')

def writemessage() :
    while True :
        try : 
            message = input('{}: '.format(str(nickname).decode("utf-8")))
            ClientSock.sendto(message.encode(), (localIP,localPort))
            reply = ClientSock.recvfrom(1024)
            print("Server: {}".format(str(reply[0])))
        except :
            print("Error!!")
            ClientSock.close()
            break
ClientSock.sendto(nickname, (localIP,localPort))
message = ClientSock.recvfrom(1024)
print(str(message[0].decode()))
writemessage()
