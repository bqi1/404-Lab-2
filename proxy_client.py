import socket

def send_data(serversocket,payload):
    # Send payload, but must try to encode first
    serversocket.sendall(payload.encode())
def create_tcp_socket():
    # Instantiate and return a client socket. Sock stream tells us we want a TCP socket
    return socket.socket(socket.AF_INET,socket.SOCK_STREAM)
def main():
    host = 'localhost'
    payload = f'GET / HTTP/1.0\r\nHost: www.google.com\r\n\r\n'
    port = 8001
    buffer_size = 4096
    remote_ip = socket.gethostbyname(host) # Get IP address of proxy server
    s = create_tcp_socket() # Make socket, get IP, and connect
    s.connect((remote_ip, port))
    send_data(s,payload)
    full_data = b"" # Data returned by proxy server
    while True:
        data = s.recv(buffer_size) # Receieves one thing as a byte string, but use while loop to keep receiving until nothing else
        if not data:
            break
        full_data += data
        break
    print(full_data)
main()