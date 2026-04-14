# simulation.py
# Reduced-round simulation for:
# "Enhancing Security of the Lightweight Block Cipher SAILFISH-I
# Against Integral Cryptanalysis Using Extra Key Whitening"

from typing import List, Tuple


# ------------------------------------------------------------
# 4-bit S-box (toy lightweight style)
# ------------------------------------------------------------
SBOX = [
    0xC, 0x5, 0x6, 0xB,
    0x9, 0x0, 0xA, 0xD,
    0x3, 0xE, 0xF, 0x8,
    0x4, 0x7, 0x1, 0x2
]


# ------------------------------------------------------------
# Helper functions
# ------------------------------------------------------------
def xor_nibbles(values: List[int]) -> int:
    """XOR a list of 4-bit values."""
    result = 0
    for v in values:
        result ^= v
    return result


def apply_sbox(value: int) -> int:
    """Apply 4-bit S-box."""
    return SBOX[value & 0xF]


def generate_structured_plaintexts() -> List[List[int]]:
    """
    Generate 16 structured plaintexts.
    One nibble varies from 0 to 15, while the other 3 nibbles stay constant.
    Example state = [varying, 1, 2, 3]
    """
    plaintexts = []
    for v in range(16):
        plaintexts.append([v, 1, 2, 3])
    return plaintexts


def generate_round_keys(rounds: int) -> List[List[int]]:
    """
    Generate simple round keys (4 nibbles per round).
    This is enough for an academic reduced-round simulation.
    """
    round_keys = []
    for r in range(rounds):
        round_keys.append([
            (1 + r) & 0xF,
            (2 + r) & 0xF,
            (3 + r) & 0xF,
            (4 + r) & 0xF,
        ])
    return round_keys


# ------------------------------------------------------------
# Original reduced-round toy cipher
# ------------------------------------------------------------
def original_round(state: List[int], round_key: List[int]) -> List[int]:
    """
    One round of the original reduced-round lightweight toy cipher.
    State = 4 nibbles [a, b, c, d]
    """
    a, b, c, d = state

    na = apply_sbox(a ^ round_key[0])
    nb = apply_sbox(b ^ a ^ round_key[1])
    nc = apply_sbox(c ^ (a & b) ^ round_key[2])
    nd = apply_sbox(d ^ b ^ c ^ round_key[3])

    # Lightweight permutation / rearrangement
    return [nb, nc, nd, na]


# ------------------------------------------------------------
# Modified cipher with extra key whitening
# ------------------------------------------------------------
def modified_round(state: List[int], round_key: List[int], round_index: int) -> List[int]:
    """
    Original round + extra key whitening starting from later rounds.
    This represents the proposed defense mechanism.
    """
    s = original_round(state, round_key)

    # Apply extra whitening from round 2 onward (index 1 onward)
    if round_index >= 1:
        whitening_key = [
            (round_key[0] ^ ((round_index + 1) * 1)) & 0xF,
            (round_key[1] ^ ((round_index + 1) * 2)) & 0xF,
            (round_key[2] ^ ((round_index + 1) * 3)) & 0xF,
            (round_key[3] ^ ((round_index + 1) * 4)) & 0xF,
        ]

        # Extra XOR-based mixing
        s = [(s[i] ^ whitening_key[i]) & 0xF for i in range(4)]

        # Additional disturbance to break balanced propagation earlier
        s = [
            apply_sbox((s[0] ^ s[1]) & 0xF),
            apply_sbox((s[1] ^ s[2]) & 0xF),
            s[2],
            s[3]
        ]

    return s


# ------------------------------------------------------------
# Trace encryption round by round
# ------------------------------------------------------------
def encrypt_trace_original(plaintext: List[int], round_keys: List[List[int]]) -> List[List[int]]:
    """Return all intermediate round states for the original version."""
    state = plaintext[:]
    trace = []

    for rk in round_keys:
        state = original_round(state, rk)
        trace.append(state[:])

    return trace


def encrypt_trace_modified(plaintext: List[int], round_keys: List[List[int]]) -> List[List[int]]:
    """Return all intermediate round states for the modified version."""
    state = plaintext[:]
    trace = []

    for r, rk in enumerate(round_keys):
        state = modified_round(state, rk, r)
        trace.append(state[:])

    return trace


# ------------------------------------------------------------
# Balanced property analysis
# ------------------------------------------------------------
def balanced_positions(states: List[List[int]]) -> List[int]:
    """
    Check which nibble positions are balanced across the structured plaintext set.
    A position is balanced if XOR of all values at that position = 0.
    """
    positions = []

    for pos in range(4):
        values = [state[pos] for state in states]
        if xor_nibbles(values) == 0:
            positions.append(pos)

    return positions


def analyze_cipher(rounds: int = 7) -> Tuple[List[Tuple[int, int, List[int]]], List[Tuple[int, int, List[int]]]]:
    """
    Analyze balanced positions round-by-round for original and modified versions.
    Returns:
        original_results, modified_results
    Each item is:
        (round_number, balanced_count, balanced_positions)
    """
    plaintexts = generate_structured_plaintexts()
    round_keys = generate_round_keys(rounds)

    original_traces = [encrypt_trace_original(pt, round_keys) for pt in plaintexts]
    modified_traces = [encrypt_trace_modified(pt, round_keys) for pt in plaintexts]

    original_results = []
    modified_results = []

    for r in range(rounds):
        original_round_states = [trace[r] for trace in original_traces]
        modified_round_states = [trace[r] for trace in modified_traces]

        original_balanced = balanced_positions(original_round_states)
        modified_balanced = balanced_positions(modified_round_states)

        original_results.append((r + 1, len(original_balanced), original_balanced))
        modified_results.append((r + 1, len(modified_balanced), modified_balanced))

    return original_results, modified_results


# ------------------------------------------------------------
# Printing utilities
# ------------------------------------------------------------
def format_positions(pos_list: List[int]) -> str:
    if not pos_list:
        return "-"
    return ", ".join(str(p) for p in pos_list)


def print_results_table(original_results, modified_results):
    print("\n" + "=" * 78)
    print("REDUCED-ROUND INTEGRAL ANALYSIS COMPARISON")
    print("=" * 78)
    print(f"{'Round':<10}{'Original Count':<18}{'Modified Count':<18}{'Observation'}")
    print("-" * 78)

    for o, m in zip(original_results, modified_results):
        round_no = o[0]
        original_count = o[1]
        modified_count = m[1]

        if modified_count < original_count:
            observation = "Modified loses balance earlier"
        elif modified_count > original_count:
            observation = "Modified still keeps more balance"
        else:
            observation = "Same number of balanced positions"

        print(f"{round_no:<10}{original_count:<18}{modified_count:<18}{observation}")

    print("=" * 78)


def print_detailed_positions(original_results, modified_results):
    print("\nDetailed Balanced Positions")
    print("=" * 78)
    print(f"{'Round':<10}{'Original Positions':<30}{'Modified Positions'}")
    print("-" * 78)

    for o, m in zip(original_results, modified_results):
        print(f"{o[0]:<10}{format_positions(o[2]):<30}{format_positions(m[2])}")

    print("=" * 78)


def summarize(original_results, modified_results):
    print("\nSummary")
    print("=" * 78)

    first_original_zero = None
    first_modified_zero = None

    for r, count, _ in original_results:
        if count == 0 and first_original_zero is None:
            first_original_zero = r

    for r, count, _ in modified_results:
        if count == 0 and first_modified_zero is None:
            first_modified_zero = r

    if first_original_zero is not None:
        print(f"Original version loses all balanced positions at round {first_original_zero}.")
    else:
        print("Original version still preserves some balanced positions in all tested rounds.")

    if first_modified_zero is not None:
        print(f"Modified version loses all balanced positions at round {first_modified_zero}.")
    else:
        print("Modified version still preserves some balanced positions in all tested rounds.")

    if first_original_zero is not None and first_modified_zero is not None:
        if first_modified_zero < first_original_zero:
            diff = first_original_zero - first_modified_zero
            print(f"The modified version removes balanced behavior {diff} round(s) earlier.")
        elif first_modified_zero == first_original_zero:
            print("Both versions lose balanced behavior at the same round.")
        else:
            print("In this simulation, the modified version loses balance later than the original.")

    print("=" * 78)


# ------------------------------------------------------------
# Main
# ------------------------------------------------------------
def main():
    rounds = 7

    print("=" * 78)
    print("SIMULATION OF INTEGRAL CRYPTANALYSIS ON A REDUCED-ROUND LIGHTWEIGHT MODEL")
    print("Target concept: SAILFISH-I inspired reduced-round experiment")
    print("Defense mechanism: Extra Key Whitening")
    print("=" * 78)

    plaintexts = generate_structured_plaintexts()
    print("\nStructured Plaintexts:")
    for i, pt in enumerate(plaintexts):
        print(f"PT[{i:02d}] = {pt}")

    original_results, modified_results = analyze_cipher(rounds=rounds)

    print_results_table(original_results, modified_results)
    print_detailed_positions(original_results, modified_results)
    summarize(original_results, modified_results)


if __name__ == "__main__":
    main()