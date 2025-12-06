def solve(lines):
    ranges = parse_input(lines)
    merged_ranges = merge_ranges(ranges)

    return sum(r[1] - r[0] + 1 for r in merged_ranges)


def parse_input(lines):
    ranges = []

    for line in lines:
        if line == '':
            break
        (low, high) = (int(s) for s in line.split('-'))
        ranges.append((low, high))

    return ranges


def merge_ranges(ranges):
    sorted_ranges = sorted(ranges, key=lambda pair: pair[0])
    merged_ranges = []

    previous_range = None
    for range_ in sorted_ranges:
        if not previous_range:
            previous_range = range_
            continue

        if previous_range[1] >= range_[0]:
            previous_range = (previous_range[0], max(previous_range[1], range_[1]))
        else:
            merged_ranges.append(previous_range)
            previous_range = range_

    merged_ranges.append(previous_range)
    return merged_ranges


if __name__ == '__main__':
    with open('example_input.txt', 'r') as example_file:
        print(solve(example_file.read().splitlines()))

    with open('input.txt', 'r') as input_file:
        print(solve(input_file.read().splitlines()))
