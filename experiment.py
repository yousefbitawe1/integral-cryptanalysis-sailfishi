from original_cipher import encrypt_original
from modified_cipher import encrypt_modified
from utils import generate_plaintexts, xor_sum, is_balanced


ROUND_KEYS = [0x1111, 0x2222, 0x3333, 0x4444, 0x5555, 0x6666, 0x7777]
WHITENING_KEYS = [0x00F0, 0x0F00, 0x00FF, 0xF000, 0xAAAA, 0x5555, 0x1357]


def run_experiment(rounds: int):
    plaintexts = generate_plaintexts()

    original_outputs = [
        encrypt_original(pt, ROUND_KEYS, rounds) for pt in plaintexts
    ]

    modified_outputs = [
        encrypt_modified(pt, ROUND_KEYS, WHITENING_KEYS, rounds) for pt in plaintexts
    ]

    original_xor = xor_sum(original_outputs)
    modified_xor = xor_sum(modified_outputs)

    original_balanced = is_balanced(original_outputs)
    modified_balanced = is_balanced(modified_outputs)

    return {
        "rounds": rounds,
        "original_xor": hex(original_xor),
        "modified_xor": hex(modified_xor),
        "original_balanced": original_balanced,
        "modified_balanced": modified_balanced
    }