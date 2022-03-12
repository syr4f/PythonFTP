#FTP Client Side Code

import socket

s = socket.socket() #declare socket variable

port = 8888

s.connect(('192.168.56.101', port)) #established connection to the server
print("connected to server:")

filename = input(str("Rename file as : ")) #enter what name file you want to save, you can rename it
file = open(filename, 'wb')
file_data = s.recv(1024) #will receive file
file.write(file_data)   #will write it on client storage

file.close() #close file  function
print("File has been received successfully.")

s.close() #close socket
print('Server-Client Connection End')
