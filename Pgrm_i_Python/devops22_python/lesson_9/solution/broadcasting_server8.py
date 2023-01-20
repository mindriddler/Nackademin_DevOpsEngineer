# Broadcasting
# Add a new command i.e "b" to your server, that sends a echo back to all connected clients (broadcast).
# To accomplish this you can save all client connection sockets to a list when created or you can use enemurate.
# Loop over the list and send the message to all clients.
# When using your client, you can i.e send the letter b as the command to broadcast
# Test that all your clients get the message

import socket
from threading import Thread


def split_raw_data(b: bytes):
    raw_data = b.decode()
    command = raw_data[:1]
    data = raw_data[1:]
    return command, data


def apply_command(command: str, data: str):
    if command == 'u':
        return data.upper()
    elif command == 'r':
        return data[::-1]
    elif command == 'b':
        return data
    elif command.isdigit():
        if (int(command) == 0):
            return "\n"
        return data*int(command)
    return "Command not found!"


def handle_server_response(b: bytes, connection, clients):
    command, data = split_raw_data(b)
    result = apply_command(command, data)
    if command == 'b':
        for client in clients:
            client.sendall(result.encode())
    else:
        print("command: " + command + " result: " + result)
        connection.sendall(result.encode())


def recv_and_print(connection, clients):
    with connection:
        while True:
            data = connection.recv(1024)
            if not data:
                break
            print(f"Server responded: {data}")
            handle_server_response(data, connection, clients)


def close_clients(clients):
    for connection in clients:
        connection.close()


def main():
    HOST = '127.0.0.1'
    PORT = 50008
    clients = []              # Arbitrary non-privileged port
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Avoid (address,port) reuse issue on linux/mac with setsockopt
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(1)
        while True:
            conn, addr = s.accept()
            print('Connected by', addr)
            clients.append(conn)
            Thread(target=recv_and_print, args=(conn, clients)).start()


if __name__ == '__main__':
    main()
