def byte_xor(byte_1, byte_2):
    # A simple 2 bytes type XOR operator
    return bytes([_a ^ _b for _a, _b in zip(byte_1, byte_2)])


def int_to_hex(value):
    # Convert the INT value to HEX value and String
    return f'{value:02x}'
