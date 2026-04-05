from experiment import run_experiment


def main():
    print("Integral Cryptanalysis Experiment")
    print("-" * 50)

    for rounds in range(3, 8):
        result = run_experiment(rounds)

        print(f"Rounds: {result['rounds']}")
        print(f"Original XOR Sum: {result['original_xor']}")
        print(f"Modified XOR Sum: {result['modified_xor']}")
        print(f"Original Balanced: {result['original_balanced']}")
        print(f"Modified Balanced: {result['modified_balanced']}")
        print("-" * 50)


if __name__ == "__main__":
    main()