from getpass import getpass
from socket import *
from base64 import *
import ssl
import json

Main_Email = input ("Enter Your Email Address : ")
Main_Email_Password = getpass("Enter Your Email Password : ")
Main_Email_Destination = input("Enter Email Destination : ")
Main_Email_Subject = input("Enter Subject : ")
Main_Email_BodyMessage = input("Enter Message : ")

msg = '{}. \r\n\nThis message is sent by the sender for the Individual Assignment ITT440 pur>
endmsg = '\r\n.\r\n'

# Choose a mail server (e.g Google mail server) and call it mailserver
mailServer = 'smtp.gmail.com'
mailPort = 587

# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start
clientSocket = socket (AF_INET, SOCK_STREAM)
clientSocket.connect ((mailServer, mailPort))
#Fill in end

recv = clientSocket.recv(1024)
print (recv)
if recv[:3] != '220':
   print ('220 no reply from server.')

# Send Helo command and print server response.
heloCommand = 'HELO Alice\r\n'.encode()
clientSocket.send(heloCommand)
recvl = clientSocket.recv(1024)
print (recvl)
if recvl[:3] != '250':
   print ('250 no reply from server.')

# Account Authentication
# Fill in start
strtlscmd = "STARTTLS\r\n".encode()
clientSocket.send(strtlscmd)
recv2 = clientSocket.recv(1024)

sslClientSocket = ssl.wrap_socket(clientSocket)

Sender_Email = b64encode(Main_Email.encode())
Sender_Password = b64encode(Main_Email_Password.encode())

authorizationcmd = "AUTH LOGIN\r\n"

sslClientSocket.send(authorizationcmd.encode())
recv2 = sslClientSocket.recv(1024)
print(recv2)

sslClientSocket.send(Sender_Email + "\r\n".encode())
recv3 = sslClientSocket.recv(1024)
print(recv3)

sslClientSocket.send(Sender_Password + "\r\n".encode())
recv4 = sslClientSocket.recv(1024)
print(recv4)
# Fill in end

# Send MAIL FROM command and print server response.
# Fill in start
mailfrom = "MAIL FROM: <{}>\r\n".format(Main_Email)
sslClientSocket.send(mailfrom.encode())
recv5 = sslClientSocket.recv(1024)
print(recv5)
# Fill in end

# Send RCPT TO command and print server response.
# Fill in start
rcptto = "RCPT TO: <{}>\r\n".format(Main_Email_Destination)
sslClientSocket.send(rcptto.encode())
recv6 = sslClientSocket.recv(1024)
# Fill in end

# Send DATA command and print server response.
# Fill in start
data = 'DATA\r\n'
sslClientSocket.send(data.encode())
recv7 = sslClientSocket.recv(1024)
print(recv7)
# Fill in end

# Send message data.
# Fill in start
sslClientSocket.send("Subject: {}\n\n{}".format(Main_Email_Subject, msg).encode())
# Fill in end

# Message ends with a single period.
# Fill in end
sslClientSocket.send(endmsg.encode())
recv8 = sslClientSocket.recv(1024)
print(recv8)
# Fill in end

# Send QUIT command and get server response.
# Fill in start
quitcommand = 'QUIT\r\n'
sslClientSocket.send(quitcommand.encode())
recv9 = sslClientSocket.recv(1024)
print(recv9)

sslClientSocket.close()
print('The Email is sent successfully!')
# Fill in end


