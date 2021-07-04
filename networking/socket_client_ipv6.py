#!/usr/bin/env python3

import socket

HOST = "::1"    # The server's hostname or IP address
PORT = 6969     # The port used by the server

# In comparison to the server, the client is pretty simple.
# It creates a socket object, connects to the server and
# calls s.sendall() to send message. Lastly, it calls s.recv()
# to read the server’s reply and then prints it.

if __name__ == "__main__":
    with socket.socket(socket.AF_INET6, socket.SOCK_STREAM) as soc:
        soc.connect((HOST, PORT))
        soc.sendall(b'Hello, world')
        data = soc.recv(1024)

    print('Received', repr(data))
