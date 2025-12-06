def solve(lines):
    worksheet = [line.split() for line in lines]
    n = len(worksheet)
    m = len(worksheet[0])
    result = 0

    for j in range(m):
        operation = worksheet[-1][j]
        column_result = 1 if operation == '*' else 0

        for i in range(n - 1):
            if operation == '*':
                column_result *= int(worksheet[i][j])
            else:
                column_result += int(worksheet[i][j])

        result += column_result

    return result


if __name__ == '__main__':
    with open('example_input.txt', 'r') as example_file:
        print(solve(example_file.read().splitlines()))

    with open('input.txt', 'r') as input_file:
        print(solve(input_file.read().splitlines()))
