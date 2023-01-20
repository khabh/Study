import sys

n = int(input())
if n % 2 == 1:
    print(0)
    sys.exit()
result = [0] * (n // 2)
result[0] = 3
for i in range(1, n // 2):
    result[i] = result[i - 1] * 3 + sum(result[:i - 1]) * 2 + 2
print(result[n // 2 - 1])
