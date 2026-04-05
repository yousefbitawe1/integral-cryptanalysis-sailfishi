from original_cipher import round_function


def encrypt_modified(plaintext: int, round_keys: list[int], whitening_keys: list[int], rounds: int) -> int:
    state = plaintext & 0xFFFF
    for r in range(rounds):
        state = round_function(state, round_keys[r])

        # Extra key whitening after each round
        state ^= whitening_keys[r]

    return state