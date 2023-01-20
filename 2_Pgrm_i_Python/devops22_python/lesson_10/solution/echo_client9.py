# # Client improvement

# Until now your client has been waiting for input then sending it to the server, afterwards it assume you get a recv. We will use threads to improve the client so it can read and write simultaneously. If you want a perfect user experience[EXTRA] you should probably use your TK GUI, since the terminal doesn't play well when waiting for a input and printing at the same time.

# 1. If you don't have a loop yet in the client. Add a loop so it will:
#     1. Ask for input(with command)
#     2. Send the input to the server
#     3. recv the echo from server
#     4. print the recv message

# 2. Create a function that handles:
#     - recv messages from the server
#     - it prints the message from the server
#     - [Extra] refactor your function into functions with a single responsibility

# 3. Start the recv & print function as a thread.
# 4. [Extra] what happens when the server connection is closed? Does the thread stop without errors?
# 5. [Extra] what happens when you close down your client, does the thread stop?
# 6. Manually test your client:
#     1. Does it work to send message to the server?
#     2. Does it work to recv message from the server?
#     3. Does it work to recv broadcast messages from the server?
#     4. What happens if you recv a message while typing?


import socket
from threading import Thread


def receive(connection):
    return connection.recv(1024)


def print_bytes(byte_msg):
    message = byte_msg.decode()
    print(f"[Server]: {message}")


def recv_and_print(connection):
    while True:
        data = receive(connection)
        if not data:
            break
        print_bytes(data)


def main():
    HOST = '127.0.0.1'    # The remote host
    PORT = 50009              # The same port as used by the server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        Thread(target=recv_and_print, args=(s,)).start()
        while True:
            to_send = input("Text please: ").encode()
            s.sendall(to_send)


if __name__ == '__main__':
    main()
