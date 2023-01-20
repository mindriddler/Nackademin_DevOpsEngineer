# TCP_NODELAY# Echo client program from https://docs.python.org/3/library/socket.html#example

import socket
from time import sleep

HOST = '127.0.0.1'    # The remote host
PORT = 50012              # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.send(b'hello')

    # Add short sleep to trigger the issue
    # This may need adjustment depending on OS and hardware
    sleep(0.00006)
    s.send(b'world')

    # What the servers first recv
    data1 = s.recv(1024)
    print('Received', repr(data1))
