from functools import cache


class Node:

    def __init__(self, key):
        self.key = key
        self.sources = set()
        self.targets = set()


def solve(lines):
    graph = build_graph(lines)

    @cache
    def count_paths_from_you(target_key):
        if target_key == 'you':
            return 1

        return sum(count_paths_from_you(source) for source in graph[target_key].sources)

    return count_paths_from_you('out')


def build_graph(lines):
    graph = {}

    for line in lines:
        node_key, targets_string = line.split(': ')
        target_keys = set(targets_string.split(' '))

        node = graph[node_key] if node_key in graph else Node(node_key)
        node.targets.union(target_keys)
        graph[node_key] = node

        for target_key in target_keys:
            target = graph[target_key] if target_key in graph else Node(target_key)
            target.sources.add(node_key)
            graph[target_key] = target

    return graph


if __name__ == '__main__':
    with open('example_input1.txt', 'r') as example_file:
        print(solve(example_file.read().splitlines()))

    with open('input.txt', 'r') as input_file:
        print(solve(input_file.read().splitlines()))
