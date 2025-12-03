def solve(lines):
    max_joltage = 0

    for line in lines:
        best_12 = []

        for digit in (int(c) for c in reversed(line)):
            if len(best_12) < 12:
                best_12.insert(0, digit)
                continue

            if digit >= best_12[0]:
                removal_i = 0
                while removal_i < 11 and best_12[removal_i] >= best_12[removal_i + 1]:
                    removal_i += 1
                del best_12[removal_i]
                best_12.insert(0, digit)

        max_joltage += int(''.join(str(d) for d in best_12))

    return max_joltage


if __name__ == '__main__':
    with open('example_input.txt', 'r') as example_file:
        print(solve(example_file.read().splitlines()))

    with open('input.txt', 'r') as input_file:
        print(solve(input_file.read().splitlines()))
