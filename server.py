#import socket module
from socket import *
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
serverPort = 6789
serverSocket.bind(('127.0.0.1', serverPort))
serverSocket.listen(1)

while True:
    #Establish the connection
    print("Ready to serve...")
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]        
        f = open(filename[1:])        
        outputdata = f.read()    
        #Send one HTTP header line into socket    
        connectionSocket.send('HTTP/1.0 200 OK\r\n\r\n'.encode())
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.sendall(outputdata[i].encode())
        connectionSocket.sendall("\r\n".encode())
       
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        connectionSocket.send('404 Not Found'.encode())
        #Close client socket
        connectionSocket.close()
serverSocket.close() 
sys.exit()#Terminate the program after sending the corresponding data