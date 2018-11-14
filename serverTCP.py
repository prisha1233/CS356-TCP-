#Priyanka Shah  HTTP PROGRAMMING ASSIGNEMENT
#ucid - pps48
#CS356 002  

import sys
from socket import*
#import urllib.request
#import requests 
import time,os,datetime
from datetime import datetime
from time import timezone

# any local IP address
serverIP= ''
serverPort= 8000
dataLen= 1000000


serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind((serverIP, serverPort))

serverSocket.listen(2)
print('The server is ready to receive on port:' + str(serverPort)+'\nPriyanka Shah Http Assignment')

LastModifiedTime = 0      
# loop forever listening for incoming connection requests
while True:
# Accept incoming connection requests, and allocate a new socket
    connectionSocket,address = serverSocket.accept()
    print("Socket created for client " + address[0] + ", " + str(address[1]))
   
# Receive and print the client data in bytes from "data" socket
    Getdata = connectionSocket.recv(dataLen).decode()
    print("Received Get Request from Client: \n" + Getdata)
    modifydata =" "
    #parsing geet request in lines
    data = Getdata.split('\r\n')[0]
    newdata  = Getdata.split('\r\n')[1]
    modifydata = Getdata.split('\r\n')[2]
    print (data + " " + newdata+ " modifydata" +modifydata)

    #parser 1st line of request
    method =data.split(' ')[0]
    filename = data.split(' ')[1]
    file =filename.split('/')[1]
    aversion = data.split(' ')[2]
    version =aversion.split('\r\n')[0]
    #print ("method: "+ method+ " file"+file +" version "+ version)

    #parsed 2nd line of request
    localhostport = newdata.split(' ')[1]
    host = localhostport.split(':')[0]
    port = (localhostport.split(':')[1]). split("\r\n")[0]
    #print ("host "+ host+ " port "+ port)
    oldTimeSecs= 0
    #pased 3rd line of conditional request 
    if (len(modifydata) > 7):
	modifyDate = modifydata.replace("If-Modified-Since: ","")
	modifyDate=((modifyDate)+"\r\n")
	#print(modifyDate)
	ifModTime =time.strptime(modifyDate,"%a, %d %b %Y %H:%M:%S %Z\r\n")
	oldTimeSecs =time.mktime(ifModTime)
	#print ("oldTimeSecs: "+str(oldTimeSecs))
	
    #check the file is exist or not code 200 
    try:
        #r = open (file,'r')
        r = open ("filename.html",'r')
        string =r.read()
        
	#file size 
        size = os.path.getsize(file)
        #modification time in secs 
        secs = os.path.getmtime(file)
        mtime= time.gmtime(secs)
        #modifited time in format
        modifiedTime =time.strftime("%a, %d %b %Y %H:%M:%S %Z\r\n", mtime)
	amodifiedTime =time.strptime(modifiedTime,"%a, %d %b %Y %H:%M:%S %Z\r\n")
	asecs= time.mktime(amodifiedTime)
	print(asecs)
        
        # get local time
        l = time.gmtime()
        date= time.strftime("%a, %d %b %Y %H:%M:%S EST GMT", l)

	#print ("secs"+str(asecs))
        if (int(oldTimeSecs) == int (asecs)):
            code = "304"
            #print ("secs"+str(asecs)+" oldTimeSecs"+str(oldTimeSecs))
        else:
            code ="200"

    except OSError:
        code = "404"
        l = time.gmtime()
        date= time.strftime("%a, %d %b %Y %H:%M:%S GMT", l)


        
    #checking that what time of request is this 
    if (code == "200"):
        header = (version +" " + code +" OK\r\n"+"DATE: "+ date + "\r\nLast-Modified: "+modifiedTime +"\r\nContent-Length"+ str(size)+"\r\nContent-Type: text/html; charset = UTF-8\r\n\r\n"+string+"\n")
        
    elif (code == "404"):
        header = ( version +" "+code + " NOT FOUND\r\n"+"DATE: " +date+ "\r\n\r\n")
    elif (code == "304"):
        header = (version +" "+code + " NOT Modified\r\n"+"DATE: " +date + "\r\n\r\n")

    
    connectionSocket.send(str(header).encode())
    #print ("sent size" + str(header))

    connectionSocket.close()
    #conn.close()
