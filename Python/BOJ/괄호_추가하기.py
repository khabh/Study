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
        answer = number[0]
        for i in range(1, len(operator)):
            answer = calculate(answer, number[i], operator[i])
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
