import socket
import threading


def handle_server_message(conn, stop):
    while not stop.is_set():
        try:
            response = conn.recv(1024)
            if not response:
                stop.set()
                break
            print(f"\nServer responded: {response}")
        finally:
            stop.set()


def main():
    HOST = '127.0.0.1'      # The remote host
    PORT = 50008             # The same port as used by the server
    stop = threading.Event()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        listen_thread = threading.Thread(daemon=False,
                                         target=handle_server_message, args=(
                                             s, stop))
        listen_thread.start()
        while not stop.is_set():
            to_send = input("Send message or q to quit: ")
            if to_send == "q":
                stop.set()
                break
            s.sendall(to_send.encode())


if __name__ == '__main__':
    main()
