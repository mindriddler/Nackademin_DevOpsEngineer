# Echo client program from https://docs.python.org/3/library/socket.html#example

import socket


def main():
    HOST = 'localhost'    # The remote host
    PORT = 50007              # The same port as used by the server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(bytes('rHello, world', 'utf-8'))
        data = s.recv(1024)
    print('Received', data.decode())


if __name__ == '__main__':
    main()
