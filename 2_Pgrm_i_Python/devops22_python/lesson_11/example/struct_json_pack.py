import struct
import json

print("\n ------------- Prepare Data ----------------- \n")

# Python dict
cars = {
    "volvo": "yellow",
    "saab": "blue",
    "Vålvå": "RÖda"
}

# Convert car object to json string
cars_as_json = json.dumps(cars)
print(f"json: {cars_as_json} of type: {type(cars_as_json)}")
# We have cars as a json string

# Convert it to a byte with encode
cars_json_as_bytes = cars_as_json.encode()
cars_length = len(cars_json_as_bytes)
print(f"Cars json as bytes {cars_json_as_bytes} with length {cars_length}")

print("\n ------------- create & pack struct ----------------- \n")

# Create a struct with the
# ! network (big-endian) byte order (https://docs.python.org/3/library/struct.html#byte-order-size-and-alignment)
# L unsigned long 4 bytes [0, 4294967295]
# s char[] bytes

prefix_format_string = "!L"
prefix_length = struct.calcsize(prefix_format_string)
format_string = f"{prefix_format_string}{cars_length}s"
print(f"total format_length = {struct.calcsize(format_string)}")
print(f"prefix format length = {prefix_length}")
# print(format_string.encode())

struct_message = struct.pack(format_string, cars_length, cars_json_as_bytes)

print("\n ------------- unpack struct ----------------- \n")

prefix_format_string = "!L"
first_four_bytes = struct_message[:4]
prefix_length, = struct.unpack(prefix_format_string, first_four_bytes)
print(f"Total struct length{prefix_length}")
format_string = f"{prefix_format_string}{prefix_length}s"

format, message = struct.unpack(format_string, struct_message)
print(f"Format: {format}")
print(f"Message: {message}")

print("\n ------------- decode ----------------- \n")

json_str = message.decode()
dict_from_json = json.loads(json_str)
print(f"json: {dict_from_json} of type: {type(dict_from_json)}")
