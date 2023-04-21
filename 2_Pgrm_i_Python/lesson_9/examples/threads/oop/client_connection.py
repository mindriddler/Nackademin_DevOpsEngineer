import threading


class ClientConnection(threading.Thread):

    def __init__(self, connection, address):
        threading.Thread.__init__(self)
        self.connection = connection
        self.address = address

    def run(self):
        self.running = True
        print(f'Handles connection for {self.address}')
        try:
            while self.running:
                try:
                    data = self.connection.recv(1096)
                    if not data:
                        break
                    self.connection.sendall(data)
                    print(f"Responded with {data}")

                except Exception:
                    break
        finally:
            print(f"Closing connection {self.address}")
            self.connection.close()

    def stop(self):
        self.running = False
        self.connection.close()
