def solve(lines):
    max_joltage = 0

    for line in lines:
        max_digit = None
        max_line_joltage = 0

        for digit in (int(c) for c in reversed(line)):
            if max_digit is None:
                max_digit = digit
                continue

            max_line_joltage = max(max_line_joltage, digit * 10 + max_digit)
            max_digit = max(max_digit, digit)

        max_joltage += max_line_joltage

    return max_joltage


if __name__ == '__main__':
    with open('example_input.txt', 'r') as example_file:
        print(solve(example_file.read().splitlines()))

    with open('input.txt', 'r') as input_file:
        print(solve(input_file.read().splitlines()))
