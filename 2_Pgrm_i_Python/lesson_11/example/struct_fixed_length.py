import struct

print("\n ------------- Prepare Data ----------------- \n")
number_of_bytes = 1495
bytes_to_send = b"a" * number_of_bytes
print(f"Created bytes:{len(bytes_to_send)}")
print("\n ------------- create & pack struct ----------------- \n")

# Create a struct with the
# ! network (big-endian) byte order (https://docs.python.org/3/library/struct.html#byte-order-size-and-alignment)
# s char[] bytes
format_string = "!1500s"
print("format length = ", struct.calcsize(format_string))
struct_message = struct.pack(format_string, bytes_to_send)
# Notice that the length is 1500

print("\n ------------- unpack struct ----------------- \n")

message, = struct.unpack(format_string, struct_message)
print(f"Unpacked length {len(message)}")
# When unpacked its still 1500

# Inspecting the last 10 bytes, notice 5 padding \x00 fills up to 1500
print(f"Last ten bytes {message[-10:]}")
