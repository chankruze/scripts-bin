import socket
import sys


def port_listener():
    host = '0.0.0.0'
    port = 5500

    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print("Socket created")

    # Bind socket to local host and port
    try:
        soc.bind((host, port))
    except socket.error as msg:
        print(f"Bind failed.\nError Code: {str(msg[0])}\nMessage: {msg[1]}")
        sys.exit()

    print("Socket bind complete")

    # Start listening on socket
    soc.listen(10)
    print(f"Socket now listening on: {port}")

    # client connection
    while 1:
        # wait to accept a connection - blocking call
        conn, addr = soc.accept()
        print(f"Connected.\nAddress: {addr[0]}\n{str(addr[1])}")

    soc.close()


if __name__ == '__main__':
    port_listener()
