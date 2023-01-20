# https://docs.python.org/3/library/socket.html#socket.socket.recv

import socket

HOST = '127.0.0.1'
PORT = 50012  # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        # buf size is usually a power of 2 i.e 1024, 2048, 4096 or 8192
        # Read 4096 bytes
        data = conn.recv(4096)
