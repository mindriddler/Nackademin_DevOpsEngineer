

def print_bin(num):
    print(
        f"integer {num}\t binary: {num:08b}\t total bits{num.bit_length()}",
        f"\tbig-endian: {(num).to_bytes(4, byteorder='big')}\tlittle-endian: {(num).to_bytes(4, byteorder='little')}"
    )


print_bin(1)
print_bin(2)
print_bin(16)
print_bin(255)
print_bin(256)
# 0000 0001
#

print("256 in 4 bytes with big- vs little-endian")
print((256).to_bytes(4, byteorder="big"))
print((256).to_bytes(4, byteorder="little"))
