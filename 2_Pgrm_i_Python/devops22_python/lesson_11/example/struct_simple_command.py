import struct


# Client packs a command, 1 or 2
# https://docs.python.org/3/library/struct.html#format-characters
command = struct.pack("!c", b"1")

# This could be sent over a socket connection

# The Server unpack a received command (returns tuple with 1 value)
srv_command, = struct.unpack("!c", command)

if (srv_command == b"1"):
    print("do something")

elif (srv_command == b"2"):
    print("do something else")
