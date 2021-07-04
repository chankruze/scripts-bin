#!/usr/bin/env python3

import socket

HOST = ""  # host ip
PORT = 6969  # host port to listen on

if __name__ == "__main__":
    """
    socket.socket() creates a socket object that supports the context manager type, 
    so we can use it in a with statement. There’s no need to call s.close()
    """
    """
    socket(address family, socket type)
    AF_INET = the Internet address family for IPv4.
    SOCK_STREAM = the socket type for TCP protocol
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
        # bind() associates the socket with a specific network interface and port number
        # Params depends upon address family
        # For socket.AF_INET (IPv4) it expects a 2-tuple: (host, port).
        soc.bind((HOST, PORT))

        # start listening for connections (has a backlog parameter also)
        soc.listen()
        print(f"Listening on {PORT}")

        """
        accept() blocks and waits for an incoming connection. When a client connects,
        it returns a new socket object representing the connection and a tuple holding
        the address of the client. The tuple will contain
        (host, port) for IPv4 connections
        (host, port, flowinfo, scopeid) for IPv6.
        """
        # con = client socket object
        con, adr = soc.accept()

        # infinite while loop to loop over blocking calls to con.recv()
        with con:
            print("Connected by: ", adr)
            while True:
                data = con.recv(1024)  # maximum amount of data to be received at once
                """
                If con.recv() returns an empty bytes object, b'',
                then the client closed the connection and the loop is terminated.
                The with statement is used with con to automatically close the socket at the end of the block.
                """
                if not data:
                    break
                con.sendall(data)
