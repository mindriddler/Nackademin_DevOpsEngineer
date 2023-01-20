
# Do the following steps:

# 1. Create a struct format
# 2. Create a test data byte e.g

#    ```python
#    "hello world".encode() # b'hello world'
# #    b"a"*10 # b'aaaaaaaaaa'
#    ```

# 3. Pack the struct
# 4. Inspect the struct with the debugger or print
# 5. Unpack the struct

# For the following types:

import struct

# 1. A command of 1 char

format_one = '!c'
data_one = b"a"
packed_one = struct.pack(format_one, data_one)
print(packed_one)
unpacked_one, = struct.unpack(format_one, packed_one)
print(unpacked_one)


# 2. A string with maximum 100 chars

format_two = '!100s'
data_two = "a"*100

if len(data_two) <= 100:
    packed_two = struct.pack(format_two, data_two.encode())
    print(packed_two)
    unpacked_two, = struct.unpack(format_two, packed_two)
    print(unpacked_two)


# 3. A command of 1 char followed by a string of maximum 100 chars

format_three = '!c100s'
char_three = b"c"
data_three = "a"*100

if len(data_three) <= 100:
    packed_three = struct.pack(format_three, char_three, data_three.encode())
    print(packed_three)
    unpacked_char, unpacked_three = struct.unpack(format_three, packed_three)
    print(unpacked_char, unpacked_three)


# 4. A longer string with maximum 3000 chars

format_four = '!3000s'
data_four = "d"*3000

if len(data_four) <= 3000:
    packed_four = struct.pack(format_four, data_four.encode())
    print(packed_four)
    unpacked_four, = struct.unpack(format_four, packed_four)
    print(unpacked_four)

# 5. A command of 1 char followed by a integer

format_five = '!ci'
char_five = b"a"
int_five = 97
packed_five = struct.pack(format_five, char_five, int_five)
print(packed_five)
unpacked_char, unpacked_int = struct.unpack(format_five, packed_five)
print(unpacked_char.decode(), unpacked_int)
