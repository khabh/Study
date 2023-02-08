import sys
from collections import Counter


def count_sum(numbers, number_count):
    result = Counter()
    for i in range(number_count):
        total = 0
        for j in range(i, number_count):
            total += numbers[j]
            result[total] += 1

    return result


def get_total_count(a, b):
    total = 0
    for number in a:
        total += a[number] * b[T - number]

    return total


read = sys.stdin.readline
T = int(read())
n = int(read())
A = count_sum(list(map(int, read().split())), n)
m = int(read())
B = count_sum(list(map(int, read().split())), m)
if len(A) > len(B):
    print(get_total_count(B, A))
else:
    print(get_total_count(A, B))
