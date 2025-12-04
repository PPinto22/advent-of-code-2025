import itertools

adjacency_vectors = [v for v in itertools.product([-1, 0, 1], [-1, 0, 1]) if v != (0, 0)]


def solve(grid):
    mutable_grid = [[c for c in row] for row in grid]
    result = 0

    while True:
        removals = iterate(mutable_grid)
        if removals == 0:
            break
        result += removals

    return result


def iterate(grid):
    n = len(grid)
    m = len(grid[0]) if grid else 0
    removals = 0

    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell != '@':
                continue

            adjacent_cells = [grid[i + di][j + dj] for (di, dj) in adjacency_vectors
                              if (0 <= (i + di) < n) and (0 <= (j + dj) < m)]
            adjacent_rolls_qty = sum((1 if c == '@' else 0) for c in adjacent_cells)
            if adjacent_rolls_qty < 4:
                removals += 1
                grid[i][j] = '.'

    return removals


if __name__ == '__main__':
    with open('example_input.txt', 'r') as example_file:
        print(solve(example_file.read().splitlines()))

    with open('input.txt', 'r') as input_file:
        print(solve(input_file.read().splitlines()))
