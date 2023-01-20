# Echo server program from https://docs.python.org/3/library/socket.html#example
import socket


def split_raw_data(b: bytes) -> tuple:
    raw_data = b.decode()
    command = raw_data[:1]
    data = raw_data[1:]
    return command, data


def apply_command(command: str, data: str) -> str:
    if command == 'u':
        return data.upper()
    elif command == 'r':
        return data[::-1]
    elif command.isdigit():
        if(int(command) == 0):
            return "\n"
        return data*int(command)
    raise Exception("Wrongful command")


def transform_string(b: bytes) -> tuple:
    command, data = split_raw_data(b)
    result = apply_command(command, data)
    return command, result


def main():
    HOST = '127.0.0.1'
    PORT = 50007              # Arbitrary non-privileged port
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(1)
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                command, result = transform_string(data)
                print("command: " + command + " result: " + result)
                conn.sendall(result.encode())


if __name__ == '__main__':
    main()
