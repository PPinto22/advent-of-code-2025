class CompactMatrix:
    _adjacency_vectors = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1)
    ]

    def __init__(self, points):
        self.xs = sorted({p[0] for p in points})
        self.ys = sorted({p[1] for p in points})

        self.width = len(self.xs)
        self.height = len(self.ys)

        self.x_sizes = []
        for i in range(self.width - 1):
            self.x_sizes.append(self.xs[i + 1] - self.xs[i])
        self.x_sizes.append(1)

        self.y_sizes = []
        for i in range(self.height - 1):
            self.y_sizes.append(self.ys[i + 1] - self.ys[i])
        self.y_sizes.append(1)

        self.points = [(self.xs.index(x), self.ys.index(y)) for (x, y) in points]
        points_set = set(self.points)

        self.matrix = [['?'] * self.width for _ in range(self.height)]
        for y in range(self.height):
            for x in range(self.width):
                if (x, y) in points_set:
                    self.matrix[y][x] = '#'

        self._trace_outline()
        self._fill_outer_space()
        self._fill_inner_space()

    def _trace_outline(self):
        for i in range(len(self.points)):
            (x1, y1) = self.points[i]
            (x2, y2) = self.points[(i + 1) % len(self.points)]

            assert x1 == x2 or y1 == y2

            if x1 == x2:
                for y in range(min(y1, y2) + 1, max(y1, y2)):
                    self.matrix[y][x1] = '.'
            else:
                for x in range(min(x1, x2) + 1, max(x1, x2)):
                    self.matrix[y1][x] = '.'

    def _fill_outer_space(self):
        for x in range(self.width):
            self._flood_fill((x, 0), '?', ' ')
            self._flood_fill((x, self.height - 1), '?', ' ')
        for y in range(self.height):
            self._flood_fill((0, y), '?', ' ')
            self._flood_fill((self.width - 1, y), '?', ' ')

    # Assuming outer space has already been filled
    def _fill_inner_space(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.matrix[y][x] == '?':
                    self.matrix[y][x] = '.'

    def _flood_fill(self, point, from_char, to_char):
        queue = [point]
        while queue:
            (x, y) = queue.pop()
            if self.matrix[y][x] != from_char:
                continue

            self.matrix[y][x] = to_char

            for (dx, dy) in CompactMatrix._adjacency_vectors:
                (nx, ny) = (x + dx, y + dy)
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    queue.append((nx, ny))

    def print(self):
        for y in range(self.height):
            for x in range(self.width):
                print(self.matrix[y][x], end='')
            print()

    def is_completely_filled_between(self, corner_1, corner_2):
        (x1, y1) = (min(corner_1[0], corner_2[0]), min(corner_1[1], corner_2[1]))
        (x2, y2) = (max(corner_1[0], corner_2[0]), max(corner_1[1], corner_2[1]))

        return all(self.matrix[y][x] in '#.' for x in range(x1, x2 + 1) for y in range(y1, y2 + 1))

    def real_area_between(self, corner_1, corner_2):
        (x1, y1) = (min(corner_1[0], corner_2[0]), min(corner_1[1], corner_2[1]))
        (x2, y2) = (max(corner_1[0], corner_2[0]), max(corner_1[1], corner_2[1]))

        real_width = sum(self.x_sizes[x] for x in range(x1, x2)) + 1
        real_height = sum(self.y_sizes[y] for y in range(y1, y2)) + 1
        return real_width * real_height


def solve(lines):
    red_tiles = [tuple(int(x) for x in line.split(',')) for line in lines]
    matrix = CompactMatrix(red_tiles)
    # matrix.print()

    max_area = 0

    for i, p1 in enumerate(matrix.points):
        for p2 in matrix.points[i + 1:]:
            top_left = min(p1, p2)
            bottom_right = max(p1, p2)
            if matrix.is_completely_filled_between(top_left, bottom_right):
                area = matrix.real_area_between(top_left, bottom_right)
                max_area = max(area, max_area)

    return max_area


if __name__ == '__main__':
    with open('example_input.txt', 'r') as example_file:
        print(solve(example_file.read().splitlines()))

    with open('input.txt', 'r') as input_file:
        print(solve(input_file.read().splitlines()))
