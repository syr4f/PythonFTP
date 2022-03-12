#FTP Server Side Code

import socket
import os


s = socket.socket()  #create socket
print("Socket created")

port = 8888

s.bind(('', port)) #bind the connection
print("Successfully bind to port " + str(port))
 
s.listen(5) #listen
print("Waiting for client...")



while True:
       conn, addr = s.accept()     # Establish connection with client.

       print("List of files in directory")

       for root, dirs, files in os.walk("."): #this part of code will print all avalaible fail in our current directory
              for list in files:
                   print(list)


       filename = input(str("Please enter the name of the file to be transfer : ")) #enter name of file that about to be transfer including it file type

       file = open(filename , 'rb')  #this part of code will read and then send file to client
       file_data = file.read(1024)
       while (file_data) :
             conn.send(file_data)
             print("Sending...")
             file_data = file.read(1024)
       file.close()
       print("Data transfer successfull")

       print('Done sending') 
       conn.close() #connection closed

