import socket
from client_connection import ClientConnection


class Server:

    def __init__(self):
        self.clients = []
        self.socket = socket.socket()
        self.HOST = '127.0.0.1'
        self.PORT = 12345

    # Not so good code, everything is in one method. See example lesson_9/examples/oop/server_class_without_threads.py
    def start(self):
        try:
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.socket.bind((self.HOST, self.PORT))
            self.socket.listen(1)
            while True:
                conn, addr = self.socket.accept()
                client = ClientConnection(connection=conn, address=addr)
                self.clients.append(client)
                client.start()
        finally:
            self.socket.close()
