#!/usr/bin/env python3
import socket
import multiprocessing
myPORT = 8001
BUFFER_SIZE = 4096
myHOST = "localhost"
googlePORT = 80
googleHOST = 'www.google.com'
googleS = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # Make socket, get IP, and connect
remote_ip = socket.gethostbyname(googleHOST)# Get IP address of hostname
# Now connect
googleS.connect((remote_ip, googlePORT))


def function1(addr,conn):
    # receive data, then send it back
    full_data = conn.recv(BUFFER_SIZE)
    googleS.sendall(full_data)
    reply_data = b"" # Get what is returned by GOogle, and give it to the proxy client process
    while True:
        data = googleS.recv(BUFFER_SIZE) # Receieves one thing as a byte string, but use while loop to keep receiving until nothing else
        if not data:
            break
        reply_data += data
    conn.sendall(reply_data)
    conn.close() # Remember to close the connection

if __name__ == "__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print("Instantiated server. Waiting for connections...")
        s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) # Reuse binding port
        #bind socket to adddress
        s.bind((myHOST,myPORT))
        # set to listening mode
        s.listen()
        while True:
            conn, addr = s.accept()
            multiprocessing.Process(target=function1,args=(addr,conn)).start() # Fork process
            conn.close()
        