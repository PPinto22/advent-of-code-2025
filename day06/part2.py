def solve(lines):
    worksheet = parse_worksheet(lines)
    result = 0

    for [numbers, operation] in worksheet:
        if operation == '+':
            result += sum(numbers)
        else:
            assert operation == '*'
            sub_result = 1
            for number in numbers:
                sub_result *= number
            result += sub_result

    return result


def parse_worksheet(lines):
    m = len(lines[0])

    columns = []
    column_start = 0
    j = 0

    while j < m:
        column = []
        for line in lines[:-1]:
            while j < m and line[j] != ' ':
                j += 1

        for line in lines[:-1]:
            column.append(line[column_start:j])

        j += 1
        column_start = j
        columns.append(column)

    operations = lines[-1].split()
    worksheet = []

    for j, column in enumerate(columns):
        sub_problem = []
        for k in range(len(column[0])):
            sub_problem.append(int(''.join(number[k] for number in column if number[k] != ' ')))
        worksheet.append([sub_problem, operations[j]])

    return worksheet


if __name__ == '__main__':
    with open('example_input.txt', 'r') as example_file:
        print(solve(example_file.read().splitlines()))

    with open('input.txt', 'r') as input_file:
        print(solve(input_file.read().splitlines()))
