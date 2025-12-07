def solve(lines):
    m = len(lines[0])

    beam_columns = {lines[0].index('S')}
    split_count = 0

    for line in lines[1:]:
        for j in range(m):
            if line[j] != '^':
                continue

            if j not in beam_columns:
                continue

            assert 0 < j < (m - 1)

            beam_columns.remove(j)
            beam_columns.add(j - 1)
            beam_columns.add(j + 1)

            split_count += 1

    return split_count


if __name__ == '__main__':
    with open('example_input.txt', 'r') as example_file:
        print(solve(example_file.read().splitlines()))

    with open('input.txt', 'r') as input_file:
        print(solve(input_file.read().splitlines()))
