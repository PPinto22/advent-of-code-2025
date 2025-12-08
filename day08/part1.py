import heapq

import math


def solve(lines, max_connections):
    positions = [tuple(int(s) for s in line.split(',')) for line in lines]
    circuits = set([frozenset([position]) for position in positions])

    closest_pairs = find_closest_pairs(positions, max_connections)

    for p1, p2 in closest_pairs:
        p1_circuit = next(c for c in circuits if p1 in c)
        p2_circuit = next(c for c in circuits if p2 in c)
        if p1_circuit == p2_circuit:
            continue

        merged_circuit = p1_circuit.union(p2_circuit)

        circuits.remove(p1_circuit)
        circuits.remove(p2_circuit)
        circuits.add(merged_circuit)

    result = 1
    top_3_circuits = list(sorted(circuits, key=lambda c: len(c), reverse=True))[:3]
    for circuit in top_3_circuits:
        result *= len(circuit)

    return result


def find_closest_pairs(positions, max_pairs):
    # Min heap [(-distance, (p1, p2))]
    closest_pairs = []

    for i, p1 in enumerate(positions):
        for p2 in positions[i + 1:]:
            d = distance(p1, p2)

            if len(closest_pairs) < max_pairs:
                heapq.heappush(closest_pairs, (-d, (p1, p2)))
                continue

            heapq.heappushpop(closest_pairs, (-d, (p1, p2)))

    return [(p1, p2) for (d, (p1, p2)) in sorted(closest_pairs, key=lambda x: -x[0])]


def distance(p1, p2):
    (x1, y1, z1) = p1
    (x2, y2, z2) = p2
    return math.sqrt(abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2 + abs(z1 - z2) ** 2)


if __name__ == '__main__':
    with open('example_input.txt', 'r') as example_file:
        print(solve(example_file.read().splitlines(), 10))

    with open('input.txt', 'r') as input_file:
        print(solve(input_file.read().splitlines(), 1000))
