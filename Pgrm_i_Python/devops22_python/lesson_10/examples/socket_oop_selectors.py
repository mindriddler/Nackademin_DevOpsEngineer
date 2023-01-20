import socket
import selectors
import signal
import sys
import time


class Connection:
    BUF_SIZE = 4096

    def __init__(self, conn, selector):
        self.conn = conn
        self.selector = selector
        self.outgoing = []

    def activate(self):
        self.__register_selectors(self.conn, events=selectors.EVENT_READ | selectors.EVENT_WRITE, data=self)

    def __register_selectors(self, fileobj, events=selectors.EVENT_READ, data=None):
        self.selector.register(fileobj, events, data)

    def close(self):
        self.selector.unregister(self.conn)

    def read(self):
        try:
            data = self.conn.recv(Connection.BUF_SIZE)
            if data == b'':
                self.close()
                return
            if (data):
                self.outgoing.append(data)

        except Exception as e:
            print(e)
            self.close()
            return
        else:
            print(str(data))

    def write(self):
        try:
            if (len(self.outgoing)):
                print("writing")
                self.conn.sendall(self.outgoing.pop())
        except Exception as e:
            print(e)


class ChatSocket:

    def __init__(self, sock=None, selector=None):
        self.port = 50010
        self.selector = selector
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.selector.unregister(self.sock)
        self.sock.close()

    def listen(self):
        self.__init_socket()
        self.__register_selectors(self.sock, data="accept")

    def __init_socket(self):
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(("127.0.0.1", self.port))
        self.sock.setblocking(False)
        self.sock.listen()

    def __register_selectors(self, fileobj, events=selectors.EVENT_READ, data=None):
        self.selector.register(fileobj, events, data)

    def accept_connection(self):
        conn, addr = self.sock.accept()
        conn.setblocking(False)
        print(f"Accepted connection from {addr}")
        return conn


def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    sys.exit(0)


def setup_signal_handler():
    signal.signal(signal.SIGINT, signal_handler)


def main():
    setup_signal_handler()
    sel = selectors.DefaultSelector()
    with ChatSocket(selector=sel) as chatSocket:
        chatSocket.listen()

        try:
            while True:
                events = sel.select(timeout=1.0)
                time.sleep(0.1)  # Slow down
                for key, mask in events:
                    if (key.data == "accept"):
                        conn = chatSocket.accept_connection()
                        Connection(conn, sel).activate()
                    if (isinstance(key.data, Connection) and mask & selectors.EVENT_READ):
                        key.data.read()
                    if (mask & selectors.EVENT_WRITE):
                        key.data.write()

        except Exception as e:
            print("end program")
            print(e)


if __name__ == "__main__":
    main()
