from io import BytesIO


# Small size just to prove the concept
bufsize = 8

# Test string
test_bytes = b"abcdefghijklmnopqrstuvwxyz"

# Total bytes to be read
bytes_to_read = len(test_bytes)

# BytesIO to simulate recv stream
test_bytes = BytesIO(test_bytes)


def read_in_chunks():
    data = b""
    while len(data) < bytes_to_read:
        data += test_bytes.read(bufsize)
    return data


result = read_in_chunks()
print(f"Received {len(result)} bytes, msg: {result.decode()}")
