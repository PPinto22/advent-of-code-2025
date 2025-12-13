def solve(lines):
    red_tiles = [tuple(int(x) for x in line.split(',')) for line in lines]
    max_area = 0

    for i, p1 in enumerate(red_tiles):
        for p2 in red_tiles[i + 1:]:
            area = (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)
            max_area = max(area, max_area)

    return max_area


if __name__ == '__main__':
    with open('example_input.txt', 'r') as example_file:
        print(solve(example_file.read().splitlines()))

    with open('input.txt', 'r') as input_file:
        print(solve(input_file.read().splitlines()))
