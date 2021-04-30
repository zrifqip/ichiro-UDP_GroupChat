# ichiro-UDP_GroupChat

Untuk membuat sebuah room chat akan digunakan UDP atau bisa disebut juga dengan User Data Protocol. disini terbagi dalam 2 file yaitu client.py untuk client dan server.py untuk servernya.

## Server
di server ini terdapat 2 fungsi yaitu `getname` untuk mendapatkan nama dari input client dan juga `ServerMessage` untuk mendapatkan mengirim message ke client dan juga mendapatkan message dari client. untuk membuat server ini pertama tama akan di masukkan ip address dan portnya 
```
LocalHost = '127.0.0.1'
port = 42069
```
lalu akan dibuat socket dari servernya dan bind socket ke adress
```
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((LocalHost,port))
```
#### getname
di fungsi ini akan didapatkan nama dari client untuk itu  pertama tama akan didaptkan inputan nama dari client 
```
message = server.recvfrom(1024)
client_address = message[1]
str1 = str(message[0].decode())
```
lalu server akan mengirim pesan berikut kepada client dan akan mengembalikan string nama dari client
```
server.sendto(f"Server: Welcome to the server {str1},may I help you?".encode(), client_address)
return str1
```
#### ServerMessage
di fungsi ini akan menerima pesan dari client lalu mengirim pesan ke client
```
message = server.recvfrom(1024)
print("{name}: {message}".format(name = nickname, message = str(message[0].decode())))
reply = input('server : ')
client_address = message[1]
server.sendto(reply.encode(), client_address) 
```
jika tidak bisa terkirim maka server akan server akan diclose dan exit dari program
```
print("Client has left the server")
server.close()
break
```
di main kedua fungsi tersebut akan dipanggil
```
Name = getName()
ServerMessage(Name)
```
## Client
di client ini terdapat 2 fungsi yaitu `writemessage` untuk menuliskan pesan yang inginn dikirimkan dan juga `sendName` untuk mengirimkan nama dari client yang sudah diinput<br/>
pertama tama disini akan didapatkan nama inputan dari client 
```
nickname = input("Nickname : ").encode()
```
lalu akan didapatkan ipadress ,portnya,dan juga socket dari client
```
localIP = '127.0.0.1'
localPort = 42069
ClientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

```
#### sendName
di fungsi ini akan dikirimkan nama dari inputan tadi ke server untuk intu perlu dicek terlebih dahulu servernya.<br/>
jika server tidak memiliki masalah maka nama tersebut akan dikirim ke server dan juga menerima pesan welcome dari server
```
print('Connected to the server')
ClientSock.sendto(nickname, (localIP,localPort))
message = ClientSock.recvfrom(1024)
print(str(message[0].decode()))
```
jika tidak terhubung ke server maka akan akan printing error dan akan mengeluarkan program
```
print("Error!!")
ClientSock.close()
exit(1)
```
#### writemessage
di fungsi ini akan dikirimkan pesan dari client ke server
```
message = input('{}: '.format(str(nickname)))
        ClientSock.sendto(message.encode(), (localIP,localPort))
        reply = ClientSock.recvfrom(1024)
        print("Server: {}".format(str(reply[0].decode())))
```
setelah itu kedua fungsi akan dipanggil di main
```
if __name__ == "__main__" :
    sendName()
    writemessage()
```
