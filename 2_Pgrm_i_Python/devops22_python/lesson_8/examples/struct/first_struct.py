import struct


# Prerequisites
# We agree on client and server side that data starts with f'!L3s' followed by a variable message length

# CLIENT PART
message = b"my message"
command = b"7ur"

struct_format = f'!L3s{len(message)}s'
total_size = struct.calcsize(struct_format)
packet_message = struct.pack(struct_format, total_size, command, message)
print(packet_message)

# -------------
# TRANSMITTING!!!! CLIENT -----> SERVER
# -------------

# SERVER PART
fixed_size = struct.calcsize('!L3s')
total_size, = struct.unpack('!L', packet_message[:4])
variable_message_length = total_size - fixed_size
_, command, message = struct.unpack(
    f'!L3s{variable_message_length}s', packet_message[:total_size])
print(command, message)
