import sys


def calculate(a, b, command):
    if command == '+':
        return a + b
    elif command == '-':
        return a - b
    else:
        return a * b


def dfs(index, can_merge):
    global result
    if index == N:
        temp_number = [number[0]]
        temp_operator = ['']
        index = 1
        while index < len(operator):
            if operator[index] == '*':
                temp_number[-1] *= number[index]
            else:
                temp_number.append(number[index])
                temp_operator.append(operator[index])
            index += 1
        answer = temp_number[0]
        for i in range(1, len(temp_operator)):
            answer = calculate(answer, temp_number[i], temp_operator[i])
        result = max(answer, result)
        return
    current_num = int(formula[index + 1])
    number.append(current_num)
    operator.append(formula[index])
    dfs(index + 2, True)
    number.pop()
    operator.pop()
    if can_merge:
        temp = number[-1]
        number[-1] = calculate(temp, current_num, formula[index])
        dfs(index + 2, False)
        number[-1] = temp


read = sys.stdin.readline
result = -2 ** 31 - 1
N = int(read())
formula = read().rstrip()
number = [int(formula[0])]
operator = ['']
dfs(1, 1)
print(result)
