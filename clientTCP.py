#Priyanka Shah  HTTP PROGRAMMING ASSIGNEMENT
#ucid - pps48
#CS356 002   
import socket
#import urllib.request
import sys
from socket import*
#import http.client
#import requests

#accepting arguments then parsed them from the format of
    #localhost:8000/filename.html
argv = sys.argv
localhostport = argv[1]
time= argv[2]
host = localhostport.split(":")[0]
port = (localhostport.split(":")[1]). split("/")[0]
url = (localhostport.split(":")[1]). split("/")[1]
print (host + " "+port+ " " + url+ "\n")
host = "localHost"
port = 8000
count = 1000000
#url = 'C:/Users/HP/AppData/Local/Programs/Python/Python36-32/filename.html'

# Create TCP client socket. Note the use of SOCK_STREAM for TCP packet
clientSocket= socket(AF_INET, SOCK_STREAM)

# Create TCP connection to server
print("Connecting to " + host + ", " + str(port))
serverAddress= (host,port)
clientSocket.connect (serverAddress)
#conn = http.client.HTTPSConnection(host,port)
crab ="\r\n"


if (len(time) < 2 ):
	header = ("GET /"+url+" HTTP/1.1" + crab+"Host: "+host+":"+str(port)+crab+crab)
elif (len(time)>2):
	day= time[:4]
	#print (day)
	date=time[4:6]
	#print (date)
	month = time[6:9]
	#print(month)
	year =time[9:13]
	#print(year)
	hourlytime=time[13:21]
	#print(hourlytime)
	
	atime=day+" "+date+" "+month+" "+year+" "+hourlytime+" GMT"
	header = ("GET /"+url+" HTTP/1.1" +crab+"Host: "+host+":"+str(port)+crab+
"If-Modified-Since: "+ atime +crab+crab) 
# Send data through TCP
h1= clientSocket.send(header.encode())
print (header)


# Receive the server response
response= clientSocket.recv(count).decode()
print (response)

# Close the client socket
clientSocket.close()



       
