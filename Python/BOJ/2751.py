import sys

input = sys.stdin.readline
n = int(input())
numbers = []
for _ in range(n):
    numbers.append(int(input()))
for i in sorted(numbers):
    print(i)
