import sys

n, m = map(int, sys.stdin.readline().split())
result = 1
temp = 1
count = 0
for i in range(m + 1, n + 1):
    result *= i
for i in range(2, m + 1):
    temp *= i
result //= temp
while result % (10 ** (count + 1)) == 0:
    count += 1
print(count)


# 다른 풀이
n, m = map(int, input().split())


def two_count(n):
    two = 0
    while n != 0:
        n = n // 2
        two += n
    return two

def five_count(n):
    five = 0
    while n != 0:
        n = n // 5
        five += n
    return five

print(min(two_count(n) - two_count(n - m) - two_count(m), five_count(n) - five_count(n - m) - five_count(m)))