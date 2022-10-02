from socket import *

msg = "\r\n I love computer networks!"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailServer = ('smtp.gmail.com', 587)

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect(mailServer)
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220': #220 is needed to ensure connectivity
    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250': #250 is used for an ack
 print('250 reply not received from server.')
 
# Send MAIL FROM command and print server response.
mailFrom = "MAIL FROM: <tringo831@gmail.com> \r\n"
clientSocket.send(mailFrom.encode())
recv2 = clientSocket.recv(1024).decode()
print("After MAIL FROM command: "+recv2)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send RCPT TO command and print server response.
rcptTo = "RCPT TO: <destination@gmail.com> \r\n"
clientSocket.send(rcptTo.encode())
recv3 = clientSocket.recv(1024).decode()
print("After RCPT TO command: "+recv3)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send DATA command and print server response.
data = "DATA\r\n"
clientSocket.send(data.encode())
recv4 = clientSocket.recv(1024).decode()
print("After DATA command: "+recv4)

if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send message data.
message = input('Enter message: ')
endmsg = "\r\n.\r\n"
clientSocket.send(message.encode() + endmsg.encode())
recv5 = clientSocket.recv(1024).decode()

print("Send Message Command: "+recv4)

print(recv1)
if recv1[:3] != '250': #250 is used for an ack
 print('250 reply not received from server.')

# Send QUIT command and get server response.
clientSocket.send("QUIT\r\n".encode())
message=clientSocket.recv(1024)
print (message)
clientSocket.close()