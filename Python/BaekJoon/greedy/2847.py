import sys
n = int(sys.stdin.readline())
level = [0] * n
result = 0
for i in range(n):
    level[i] = int(sys.stdin.readline())

for j in range(n-2, -1, -1):
    if level[j] >= level[j+1]:
        result += level[j] - level[j+1] + 1
        level[j] = level[j+1]-1

print(result)
