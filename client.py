#!/usr/bin/env python3
import socket, sys
# Most of this code is taken from the TA's code on eClass with minor adjustments.
def create_tcp_socket():
    # Instantiate and return a client socket. Sock stream tells us we want a TCP socket
    return socket.socket(socket.AF_INET,socket.SOCK_STREAM)
def send_data(serversocket,payload):
    # Send payload, but must try to encode first
    serversocket.sendall(payload.encode())
def main():
    try:
        host = 'www.google.com'
        port = 80
        payload = f'GET / HTTP/1.0\r\nHost: {host}\r\n\r\n' # Gets the page
        buffer_size = 4096
        s = create_tcp_socket() # Make socket, get IP, and connect
        remote_ip = socket.gethostbyname(host) # Get IP address of hostname
        # Now connect
        s.connect((remote_ip, port))
        print(f'Socket connected to {host} on ip {remote_ip}\n')
        # Send data and shut down
        send_data(s,payload)
        s.shutdown(socket.SHUT_WR)
        # Continue accepting data until no more is left
        full_data = b""
        while True:
            data = s.recv(buffer_size) # Receieves one thing as a byte string, but use while loop to keep receiving until nothing else
            if not data:
                break
            full_data += data
        print(full_data)
    except Exception as e:
        print(e)
    finally:
        # Finally, always close
        s.close()

main()
