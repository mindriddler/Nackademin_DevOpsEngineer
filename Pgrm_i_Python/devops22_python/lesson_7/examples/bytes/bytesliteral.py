# https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals
# any ASCII character except "\" or newline or the quote

a_byte = b'abcdefghiKLMNOPQRSTUVXYZ'
print(a_byte)

# not_valid_bytes_literal = b'abcåäö'

a_string = 'abcåäö'
print(a_string.encode())

# å is represented with two bytes
print(b'\xc3\xa5'.decode())

# Three of hearts need 4 bytes
three_of_hearts = "\U0001F0B3"
print(bytes(three_of_hearts, 'utf-8'))
