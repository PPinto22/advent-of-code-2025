import re

import scipy


def solve(lines):
    machines = [parse_line(line) for line in lines]
    return sum(min_button_presses_to_turn_on_machine(machine) for machine in machines)


def min_button_presses_to_turn_on_machine(machine):
    buttons, target_joltage_counters = machine

    buttons_per_joltage_counter_matrix = [[1 if counter_i in button else 0 for button in buttons]
                                          for counter_i in range(len(target_joltage_counters))]

    optimisation_result = scipy.optimize.linprog(
        c=[1 for _ in buttons],
        A_eq=buttons_per_joltage_counter_matrix,
        b_eq=target_joltage_counters,
        integrality=1  # Integer variables
    )
    optional_buttons_presses = [int(presses) for presses in optimisation_result.x]

    return sum(optional_buttons_presses)


def parse_line(line):
    match = re.search(r'\[(.+)] (.*) {(.*)}', line)

    buttons = []
    for button in match.group(2).split(' '):
        buttons.append([int(d) for d in (button[1:-1]).split(',')])

    joltage_counters = [int(c) for c in match.group(3).split(',')]

    return buttons, joltage_counters


if __name__ == '__main__':
    with open('example_input.txt', 'r') as example_file:
        print(solve(example_file.read().splitlines()))

    with open('input.txt', 'r') as input_file:
        print(solve(input_file.read().splitlines()))
