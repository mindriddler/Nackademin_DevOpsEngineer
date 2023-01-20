import sys
import threading
import signal
from client_connection import ClientConnection
from server import Server


def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    for thread in threading.enumerate():
        if isinstance(thread, ClientConnection):
            thread.stop()
            thread.join()
    sys.exit(0)


def main():
    server = Server()
    server.start()


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    main()
