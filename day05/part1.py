def solve(lines):
    ranges, ingredients = parse_input(lines)
    fresh_count = 0

    for ingredient in ingredients:
        if any(r[0] <= ingredient <= r[1] for r in ranges):
            fresh_count += 1

    return fresh_count


def parse_input(lines):
    ranges = []
    ingredients = []

    lines_iter = iter(lines)
    for line in lines_iter:
        if line == '':
            break
        (low, high) = (int(s) for s in line.split('-'))
        ranges.append((low, high))

    for line in lines_iter:
        ingredients.append(int(line))

    return ranges, ingredients


if __name__ == '__main__':
    with open('example_input.txt', 'r') as example_file:
        print(solve(example_file.read().splitlines()))

    with open('input.txt', 'r') as input_file:
        print(solve(input_file.read().splitlines()))
