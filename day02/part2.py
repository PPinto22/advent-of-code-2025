def solve(line):
    ranges = line.split(',')
    invalid_sum = 0

    for range_ in ranges:
        [low, high] = [int(s) for s in range_.split('-')]
        for num in range(low, high + 1):
            if is_invalid(num):
                invalid_sum += num

    return invalid_sum


def is_invalid(num):
    num_str = str(num)
    n = len(num_str)

    for subsequence_length in range(1, n // 2 + 1):
        subsequence = num_str[:subsequence_length]

        if all(num_str[i:i + subsequence_length] == subsequence for i in range(0, n, subsequence_length)):
            return True

    return False


if __name__ == '__main__':
    with open('example_input.txt', 'r') as example_file:
        print(solve(example_file.read()))

    with open('input.txt', 'r') as input_file:
        print(solve(input_file.read()))
