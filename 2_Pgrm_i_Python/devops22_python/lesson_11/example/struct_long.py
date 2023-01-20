import struct

# Example if you mix format, DON'T DO IT
# pack signed l
fmt = "!l"
negative_number = -10
packed = struct.pack(fmt, negative_number)

# unpacked unsigned L instead of l
unpacked,  = struct.unpack("!L", packed)
print(unpacked)  # 4294967286
