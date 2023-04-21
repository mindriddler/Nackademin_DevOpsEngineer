# Echo client program from https://docs.python.org/3/library/socket.html#example

import socket
from threading import Thread


def recv_and_print(connection):
    while True:
        data = connection.recv(1024)
        if not data:
            break
        print('Received', data.decode())


def main():
    HOST = '127.0.0.1'    # The remote host
    PORT = 50008              # The same port as used by the server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        Thread(target=recv_and_print, args=(s,)).start()
        while True:
            to_send = input("Text please: ").encode()
            s.sendall(to_send)


if __name__ == '__main__':
    main()
