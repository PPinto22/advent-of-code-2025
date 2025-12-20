import math
import re


def solve(lines):
    machines = [parse_line(line) for line in lines]
    return sum(min_button_presses_to_turn_on_machine(machine) for machine in machines)


def min_button_presses_to_turn_on_machine(machine):
    target_lights, buttons = machine
    result = math.inf

    # (button index, button presses, turned on lights)
    queue = [(0, 0, set())]
    while queue:
        button_i, button_presses, lights = queue.pop()

        if lights == target_lights:
            result = min(result, button_presses)
            continue

        if button_i >= len(buttons):
            continue

        # press button
        queue.append((button_i + 1, button_presses + 1, lights ^ buttons[button_i]))

        # skip button
        queue.append((button_i + 1, button_presses, lights))

    return result


def parse_line(line):
    match = re.search(r'\[(.+)] (.*) {', line)

    lights = {i for i, light in enumerate(match.group(1)) if light == '#'}

    buttons = []
    for button in match.group(2).split(' '):
        buttons.append({int(d) for d in (button[1:-1]).split(',')})

    return lights, buttons


if __name__ == '__main__':
    with open('example_input.txt', 'r') as example_file:
        print(solve(example_file.read().splitlines()))

    with open('input.txt', 'r') as input_file:
        print(solve(input_file.read().splitlines()))
