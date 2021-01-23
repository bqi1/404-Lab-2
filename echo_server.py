#!/usr/bin/env python3
import socket, time
import multiprocessing
# Most code here is taken from TA's code in eClass, with minor adjustments

PORT = 8001
BUFFER_SIZE = 1024
HOST = "localhost"
def function1(addr,conn):
    # receive data, wait a bit then send it back
    full_data = conn.recv(BUFFER_SIZE)
    time.sleep(0.5)
    conn.sendall(full_data)
    conn.close()
if __name__ == "__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print("Instantiated server. Waiting for connections...")
        s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) # Able to reuse bind port
        # bind socket to adddress
        s.bind((HOST,PORT))
        # set to listening mode
        s.listen()
        while True:
            conn, addr = s.accept()
            multiprocessing.Process(target=function1,args=(addr,conn)).start() # Fork processes
            conn.close()
