import sys


def get_swap():
    global numbers
    for i in range(N - 2, -1, -1):
        if numbers[i] < numbers[i + 1]:
            for j in range(N - 1, 0, -1):
                if numbers[i] < numbers[j]:
                    numbers[i], numbers[j] = numbers[j], numbers[i]
                    return ' '.join(map(str, numbers[:i + 1] + sorted(numbers[i + 1:])))
    return '-1'


read = sys.stdin.readline
N = int(read())
numbers = list(map(int, read().split()))
print(get_swap())
