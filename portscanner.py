#! /bin/python
import sys
import socket
from datetime import datetime

#define the target
if len(sys.argv) ==4:
    target = socket.gethostbyname(sys.argv[1]) #translate hostname for ipv4
    startport = int(sys.argv[2])
    endport = int(sys.argv[3])
else:
    #help banner
    print("-"*50)
    print("PortScanner 1.0 (https://github.com/d4az) ")
    print("Usage : python3 portscanner.py <ip> <p1> <p2> ")
    print("     -ip The ip address of the target. ")
    print("     -p1 The Port To Start the Scan.")
    print("     -p2 The Port To Stop the Scan.")
    print("-"*50)

#banner
def banner():
    print("-"*50)
    print("PortScanner 1.0 (https://github.com/d4az) ")
    print("scanning target "+ target)
    print("time started "+ str((datetime.now())))
    print("-"*50)

try: 
    banner()
    for port in range(startport,endport):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))   #returns error
        if(result == 0):
            print("port {} is open".format(port))
        
except KeyboardInterrupt:
    print("\nbye...")
    sys.exit()
except socket.gaierror:
    print("Host name could not be Resolved")
    sys.exit
except socket.error:
    print("Could not Connect to Server")
    sys.exit
