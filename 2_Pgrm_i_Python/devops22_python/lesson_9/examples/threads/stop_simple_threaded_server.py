import socket
import threading
import signal
import sys

connections = []


def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    for conn in connections:
        conn.close()
    sys.exit(0)


def handle_client(conn, addr):
    print(f'Handles connection from {addr}')
    while True:
        try:
            data = conn.recv(1096)
            if not data:
                break
            print(data)
            # if command
            # elif command
        except Exception:
            break


def main():
    with socket.socket() as s:
        s.bind(('127.0.0.1', 12345))
        s.listen(2)
        while True:
            conn, addr = s.accept()
            t = threading.Thread(target=handle_client, args=(conn, addr))
            t.start()
            connections.append(conn)


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    main()
