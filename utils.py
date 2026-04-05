def generate_plaintexts(base: int = 0x1230) -> list[int]:
    plaintexts = []
    for active_nibble in range(16):
        pt = (base & 0xFFF0) | active_nibble
        plaintexts.append(pt)
    return plaintexts


def xor_sum(values: list[int]) -> int:
    result = 0
    for v in values:
        result ^= v
    return result


def is_balanced(values: list[int]) -> bool:
    return xor_sum(values) == 0