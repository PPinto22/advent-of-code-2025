def solve(lines):
    position = 50
    zero_count = 0

    for line in lines:
        direction = line[0]
        distance = int(line[1:])

        position = ((position + distance) if direction == 'R' else (position - distance)) % 100

        if position == 0:
            zero_count += 1

    return zero_count


if __name__ == '__main__':
    with open('example_input.txt', 'r') as example_file:
        print(solve(example_file.read().splitlines()))

    with open('input.txt', 'r') as input_file:
        print(solve(input_file.read().splitlines()))
