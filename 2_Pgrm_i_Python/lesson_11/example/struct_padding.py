import struct

print("\n ------------- Prepare Data ----------------- \n")
number_of_bytes = 13
bytes_to_send = b"a" * number_of_bytes
print(f"Created bytes:{len(bytes_to_send)}")
print("\n ------------- create & pack struct ----------------- \n")

# Create a struct with the
# ! network (big-endian) byte order (https://docs.python.org/3/library/struct.html#byte-order-size-and-alignment)
# s char[] bytes
format_string = "!15s"
print("format length = ", struct.calcsize(format_string))
struct_message = struct.pack(format_string, bytes_to_send)
# Notice that the format length is 15

print("\n ------------- unpack struct ----------------- \n")

message, = struct.unpack(format_string, struct_message)
print(f"Unpacked length {len(message)}")
# When unpacked its still 15

# Inspecting the last 5 bytes, notice 2 padding \x00 , 13 + 2 = 15
print(f"Last five bytes {message[-5:]}")

print("\n ------------- decode ----------------- \n")
print(f"decoded message: {message.decode()}")

# THe padded bytes are ignored
