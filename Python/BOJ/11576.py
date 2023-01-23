import sys
from collections import deque

a, b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
sum = 0
result = deque()

for i in map(int, sys.stdin.readline().split()):
    m -= 1
    sum += i * (a ** m)

while sum != 0:
    result.appendleft(sum % b)
    sum //= b

print(*result, sep=' ')

# 더 빠른 풀이
from sys import stdin

A, B = map(int, stdin.readline().split())
m = int(stdin.readline())
ls = list(map(int, stdin.readline().split()))
ls = ls[::-1]
sum = 0

for i in range(m):
    sum += ls[i] * (A ** i)

ans = []
while sum:
    ans.append(sum % B)
    sum //= B

print(*ans[::-1])
