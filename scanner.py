#! bin/python
import sys
import socket
from datetime import datetime

#define our target
if len(sys.argv) == 2:
       target = socket.gethostbyname(sys.argv[1]) #Translating hostname to IPv4
else:
       print("Invalid amount of agruments.")
       print("Syntax: Python3 scanner.py <IP>")
       
#Adding Banner
print("-" * 50)
print("Scanning the Target "+target)
print("Time started: "+str(datetime.now()))
print("-" * 50)

try:
       for port in range (10,500):
               s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
               socket.setdefaulttimeout(1)
               result = s.connect_ex((target,port)) #returns an error indicator
               if result == 0:
                        print("Port {} is open".format(port))
               s.close()
                
except KeyboardInterrupt:
        print("\nExiting Program.") 
        sys.exit()
        
except socket.gaierror:
         print("Host could not be resolved")
         sys.exit()
         
except socket.error:
	print("Couldn't connect to server")
	sys.exit()

   
