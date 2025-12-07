def solve(lines):
    m = len(lines[0])

    timelines = {j: (1 if lines[0][j] == 'S' else 0) for j in range(m)}

    for line in lines[1:]:
        for j in range(m):
            if line[j] != '^':
                continue

            assert 0 < j < (m - 1)
            assert lines[j - 1] != '^'
            assert lines[j + 1] != '^'

            timelines[j - 1] += timelines[j]
            timelines[j + 1] += timelines[j]
            timelines[j] = 0

    return sum(timelines.values())


if __name__ == '__main__':
    with open('example_input.txt', 'r') as example_file:
        print(solve(example_file.read().splitlines()))

    with open('input.txt', 'r') as input_file:
        print(solve(input_file.read().splitlines()))
