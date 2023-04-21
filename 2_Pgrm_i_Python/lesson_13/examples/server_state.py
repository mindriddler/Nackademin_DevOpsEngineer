import socket
from threading import Thread

# ### Multiple clients

# 1. Create a function named recv_and_print with the argument connection
#   1. Add a recv that listen to the connection
#   2. Print the received message
#   3. Loop the receive and print
#   4. Add a break if the received result is the empty byte b''
# 2. Add a loop in your main program that allows socket `accept` to run multiple times.
# 3. Also check the [`listen`](https://docs.python.org/3/library/socket.html#socket.socket.listen) method in docs, you may need to increase this number to allow more clients.
# 4. When a client has been accepted it should start a new Thread that listens to the new connection
# 5. Add prints so it's easy to see when a client was accepted and a new thread created
# 6. Try your new code, you can start multiple terminals and run 1 server and 3 clients.
# 7. Make sure your print out are informative, you should be able to understand which client the text shown in terminal belongs to.

# Echo server program from https://docs.python.org/3/library/socket.html#example


def split_raw_data(b: bytes):
    raw_data = b.decode()
    command = raw_data[:1]
    data = raw_data[1:]
    return command, data


def apply_string_transformation(command: str, data: str):
    if command == 'u':
        return data.upper()
    elif command == 'r':
        return data[::-1]
    elif command.isdigit():
        if (int(command) == 0):
            return "\n"
        return data*int(command)
    return data


def handle_request(data, saved_messages):
    print(f"Server responded: {data}")
    command, data = split_raw_data(data)
    response = apply_string_transformation(command, data)
    if command == 's':
        # Save message
        saved_messages.append(response)
    if command == 'a':
        # Read all messages
        response = " ".join(saved_messages)
    print("command: " + command + " response: " + response)
    return response


def recv_and_print(connection, saved_messages):
    with connection:
        while True:
            data = connection.recv(1024)
            if not data:
                break
            response = handle_request(data, saved_messages)
            connection.sendall(response.encode())


def main():
    HOST = '127.0.0.1'
    PORT = 50008              # Arbitrary non-privileged port
    SAVED_MESSAGES = []
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Avoid (address,port) reuse issue on linux/mac with setsockopt
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(1)
        while True:
            conn, addr = s.accept()
            print('Connected by', addr)
            Thread(target=recv_and_print, args=(conn, SAVED_MESSAGES)).start()


if __name__ == '__main__':
    main()
