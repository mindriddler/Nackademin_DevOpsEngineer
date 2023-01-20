# Echo client program from https://docs.python.org/3/library/socket.html#example

import socket
from threading import Thread, Event
from time import sleep


def recv_and_print(connection, stop):
    while not stop.is_set():
        try:
            data = connection.recv(1024)
            if not data:
                stop.set()
                break
            print('Received', data.decode())
        except Exception:
            pass


def main():
    HOST = '127.0.0.1'    # The remote host
    PORT = 50010              # The same port as used by the server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        stop = Event()
        Thread(target=recv_and_print, args=(s, stop)).start()
        while not stop.is_set():
            sleep(0.7)
            to_send = input("Text please: ").encode()
            if to_send == b'q':
                stop.set()
                s.close()
            else:
                s.sendall(to_send)


if __name__ == '__main__':
    main()
