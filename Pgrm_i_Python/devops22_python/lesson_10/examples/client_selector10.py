# Echo client program from https://docs.python.org/3/library/socket.html#example

import socket
import selectors
import queue
from threading import Thread, Event
from time import sleep


def user_input(to_write_queue, stop):
    data = ""
    try:
        while not stop.is_set():
            # small hack.. hopefully the server respond before asking for input
            sleep(0.5)
            data = input("Write message [q to quit]: ")
            if data == "q":
                break
            to_write_queue.put(data)
    finally:
        stop.set()


def main():
    HOST = "127.0.0.1"
    PORT = 50010
    sel = selectors.DefaultSelector()
    to_write_queue = queue.Queue()
    stop = Event()

    with socket.socket() as s:
        s.connect((HOST, PORT))
        s.setblocking(False)
        # Register socket READ, incoming connections
        sel.register(s, selectors.EVENT_READ | selectors.EVENT_WRITE)

        a = Thread(target=user_input, args=(to_write_queue, stop))
        a.start()

        try:
            while not stop.is_set():
                events = sel.select(timeout=1.0)
                for key, mask in events:
                    if mask == selectors.EVENT_READ:
                        data = key.fileobj.recv(1024)
                        if not data:
                            stop.set()
                            continue
                        print(f"[Server]: {data.decode()}")
                    elif mask == selectors.EVENT_WRITE:
                        if not to_write_queue.empty():
                            send_msg = to_write_queue.get()
                            key.fileobj.sendall(send_msg.encode())
                            print(f"[Client]: {send_msg}")
        finally:
            sel.unregister(s)
            s.close()
            stop.set()


if __name__ == '__main__':
    main()
