import sys

result = [0, 1, 1, 1, 2, 2, 3]
for i in range(7, 101):
    result.append(result[i - 1] + result[i - 5])
n = int(input())
for _ in range(n):
    print(result[int(input())])
