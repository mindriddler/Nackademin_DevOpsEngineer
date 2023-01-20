import socket


class Server:

    def __init__(self) -> None:
        self.addr = ("127.0.0.1", 12345)
        self.socket = socket.socket()
        self.clients = []

    # Make your own context manager
    def __enter__(self):
        return self

    # Make your own context manager
    def __exit__(self, exc_type, exc_val, exc_tb):
        for client in self.clients:
            client.close()
        self.shutdown()

    def start(self):
        self.socket.bind(self.addr)
        self.socket.listen(5)

    def accept(self):
        with self.socket as s:
            conn, addr = s.accept()
            print(f"Connected: {addr}")
            client = ClientHandler(conn)
            self.clients.append(client)
            return client

    def shutdown(self):
        self.socket.close()


class ClientHandler():
    def __init__(self, conn) -> None:
        self.conn = conn

    def start_communcation(self):
        while True:
            data = self.conn.recv(4096)
            if not data:
                break
            print(data.decode())

    def close(self):
        print("Closing down connection for client")
        self.conn.close()


def main():
    with Server() as server:
        server.start()
        while True:
            try:
                client = server.accept()
            except OSError:
                break
            client.start_communcation()


if __name__ == '__main__':
    main()
