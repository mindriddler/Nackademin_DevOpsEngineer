# Echo server program from https://docs.python.org/3/library/socket.html#example
import socket

HOST = '127.0.0.1'
PORT = 50012  # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        # First attempt to read
        data = conn.recv(1024)

        # Send what was received
        conn.sendall(data)

        # what happens here?
        data = conn.recv(1024)
        print(data)
