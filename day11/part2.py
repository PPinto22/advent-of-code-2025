from functools import cache


class Node:

    def __init__(self, key):
        self.key = key
        self.sources = set()
        self.targets = set()


def solve(lines):
    graph = build_graph(lines)

    # [0] total paths
    # [1] paths passing through dac
    # [2] paths passing through fft
    # [3] paths passing through both dac and fft
    @cache
    def count_paths_from_svr(target_key):
        if target_key == 'svr':
            return 1, 0, 0, 0

        total = 0
        dac = 0
        fft = 0
        dac_and_fft = 0

        for source in graph[target_key].sources:
            source_total, source_dac, source_fft, source_dac_and_fft = count_paths_from_svr(source)

            total += source_total
            dac += source_total if target_key == 'dac' else source_dac
            fft += source_total if target_key == 'fft' else source_fft

            if target_key == 'dac':
                dac_and_fft += source_fft
            elif target_key == 'fft':
                dac_and_fft += source_dac
            else:
                dac_and_fft += source_dac_and_fft

        return total, dac, fft, dac_and_fft

    return count_paths_from_svr('out')[3]


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
    with open('example_input2.txt', 'r') as example_file:
        print(solve(example_file.read().splitlines()))

    with open('input.txt', 'r') as input_file:
        print(solve(input_file.read().splitlines()))
