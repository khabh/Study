import sys

n = int(sys.stdin.readline())
num = 1
result = 0
for i in range(2, n + 1):
    num *= i
while num % (10 ** (result + 1)) == 0:
    result += 1
print(result)
