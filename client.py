import socket
 
nickname = input("Nickname : ").encode()
localIP = '127.0.0.1'
localPort = 42069
ClientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def writemessage() :
    while True :
        try :
            message = input('{}: '.format(str(nickname)))
            ClientSock.sendto(message.encode(), (localIP,localPort))
            reply = ClientSock.recvfrom(1024)
            print("Server: {}".format(str(reply[0].decode())))
        except :
            print("Disconnected")
            ClientSock.close()
            break
def sendName():
    try :
        print('Connected to the server')
        ClientSock.sendto(nickname, (localIP,localPort))
        message = ClientSock.recvfrom(1024)
        print(str(message[0].decode()))
    except :
        print("Error!!")
        ClientSock.close()
        exit

if __name__ == "__main__" :
    sendName()
    writemessage()

