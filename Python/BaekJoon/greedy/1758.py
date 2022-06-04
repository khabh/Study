import sys
n = int(sys.stdin.readline())
tip = [0] * n
result = 0
for i in range(n):
    tip[i] = int(sys.stdin.readline())

tip.sort(reverse=True)

for j in range(n):
    result += max(tip[j]-j, 0)

print(result)
