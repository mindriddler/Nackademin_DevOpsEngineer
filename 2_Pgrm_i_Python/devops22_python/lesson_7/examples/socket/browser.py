import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 80))

http_get = """GET / HTTP/1.1
Host: localhost
Accept: text/html

"""
print(http_get)

s.send(http_get.encode())
response = s.recv(4096)
print(response)

s.close()
