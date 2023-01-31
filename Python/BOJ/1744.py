import sys

N = int(sys.stdin.readline())
positive = []
negative = []
for _ in range(N):
    n = int(sys.stdin.readline())
    if n > 0:
        positive.append(n)
    else:
        negative.append(n)
positive.sort(reverse=True)
negative.sort()
result = 0
for i in range(0, len(negative) - 1, 2):
    result += negative[i] * negative[i + 1]
if len(negative) % 2:
    result += negative[-1]
index = -1
for i in range(0, len(positive) - 1, 2):
    result += positive[i] * positive[i + 1]
    if positive[i + 1] == 1:
        index = i + 1
        break
if index != -1:
    result += len(positive) - index
elif len(positive) % 2:
    result += positive[-1]
print(result)
