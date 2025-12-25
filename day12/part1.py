# This solution is specific to the puzzle input, where:
# - every present has size 3x3
# - fitting presents together is not necessary
#
# This means the shape of the presents is irrelevant; they can all be treated as 3x3 squares.
# Knowing this, the problem becomes simple: a tree can fit N presents if its area contains at least N 3x3 squares.


class Tree:
    def __init__(self, width, height, presents):
        self.width = width
        self.height = height
        self.presents = presents


def solve(lines):
    trees = parse_input(lines)
    result = 0

    for tree in trees:
        tree_presents_count = sum(tree.presents)
        tree_regions_of_size_3x3 = (tree.width // 3) * (tree.height // 3)
        if tree_regions_of_size_3x3 >= tree_presents_count:
            result += 1

    return result


def parse_input(lines):
    line_i = 0

    # skip ahead to trees section, since the presents shape is irrelevant
    for line_i, line in enumerate(lines):
        if 'x' in line:
            break

    trees = []
    for line in lines[line_i:]:
        dimensions_str, presents_str = line.split(': ')
        width, height = (int(d) for d in dimensions_str.split('x'))
        present_indexes = [int(i) for i in presents_str.split(' ')]
        trees.append(Tree(width, height, present_indexes))

    return trees


if __name__ == '__main__':
    with open('input.txt', 'r') as input_file:
        print(solve(input_file.read().splitlines()))
