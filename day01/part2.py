def solve(lines):
    position = 50
    zero_count = 0

    for line in lines:
        direction = line[0]
        distance = int(line[1:])

        next_position = ((position + distance) if direction == 'R' else (position - distance)) % 100

        full_rotations = distance // 100
        zero_count += full_rotations

        if direction == 'R':
            if next_position < position:
                zero_count += 1
        elif direction == 'L' and position > 0:
            if next_position > position or next_position == 0:
                zero_count += 1

        position = next_position

    return zero_count


if __name__ == '__main__':
    with open('example_input.txt', 'r') as example_file:
        print(solve(example_file.read().splitlines()))

    with open('input.txt', 'r') as input_file:
        print(solve(input_file.read().splitlines()))
