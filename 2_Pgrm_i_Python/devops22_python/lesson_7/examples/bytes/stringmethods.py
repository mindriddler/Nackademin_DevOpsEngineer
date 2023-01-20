a_byte = b'somedata'

# https://docs.python.org/3/library/stdtypes.html#string-methods
print(a_byte[::-1])
print(a_byte.upper())

# String methods do not work as you might think
another_byte = bytes('abcåäö', 'utf-8')
print(another_byte)
print(another_byte.upper())
print(another_byte.decode().upper())
