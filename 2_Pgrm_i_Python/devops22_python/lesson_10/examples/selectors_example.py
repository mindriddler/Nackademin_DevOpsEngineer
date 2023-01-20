import selectors
import socket


class Connection:
    def __init__(self, conn, addr):
        self.conn = conn
        self.addr = addr


def main():
    addr = ("127.0.0.1", 50010)
    sel = selectors.DefaultSelector()
    print(type(sel))  # The implementation may differ depending on your OS
    with socket.socket() as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(addr)
        s.listen(5)
        # Change to non blocking
        s.setblocking(False)
        # Register socket READ, incoming connections
        sel.register(s, selectors.EVENT_READ, "socket")

        while True:
            events = sel.select(timeout=1.0)
            print(f"got events {len(events)} events: {events}")
            for key, mask in events:
                print(f"{key} - {mask}")
                # If the event is the listening socket
                if key.data == "socket":
                    conn, addr = key.fileobj.accept()
                    print(f"Accepted connections from {addr}")
                    sel.register(conn, selectors.EVENT_READ, "connection")
                # If the event is a Connection
                elif key.data == "connection" and mask == selectors.EVENT_READ:
                    data = key.fileobj.recv(1024)
                    if data:
                        print(data)
                        upper = data.decode().upper()
                        key.fileobj.sendall(upper.encode())
                    else:
                        # If the connection is closed, unregister the fileobj
                        sel.unregister(key.fileobj)


if __name__ == "__main__":
    main()
