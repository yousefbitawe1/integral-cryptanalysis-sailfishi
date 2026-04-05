SBOX = [0xC, 0x5, 0x6, 0xB,
        0x9, 0x0, 0xA, 0xD,
        0x3, 0xE, 0xF, 0x8,
        0x4, 0x7, 0x1, 0x2]

PBOX = [0, 4, 8, 12,
        1, 5, 9, 13,
        2, 6, 10, 14,
        3, 7, 11, 15]


def substitute_nibbles(state: int) -> int:
    result = 0
    for i in range(4):
        nibble = (state >> (i * 4)) & 0xF
        result |= (SBOX[nibble] << (i * 4))
    return result


def permute_bits(state: int) -> int:
    result = 0
    for i in range(16):
        bit = (state >> i) & 1
        result |= (bit << PBOX[i])
    return result


def round_function(state: int, round_key: int) -> int:
    state ^= round_key
    state = substitute_nibbles(state)
    state = permute_bits(state)
    return state


def encrypt_original(plaintext: int, round_keys: list[int], rounds: int) -> int:
    state = plaintext & 0xFFFF
    for r in range(rounds):
        state = round_function(state, round_keys[r])
    return state