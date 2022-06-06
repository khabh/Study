import sys

result = 0
tmp = 0
n = int(sys.stdin.readline())
time = list(map(int, sys.stdin.readline().split()))

time.sort()

for i in time:
    tmp += i
    result += tmp


print(result)
