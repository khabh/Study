import sys
n = int(sys.stdin.readline())
rope = [0] * n
result = 0
for i in range(n):
    rope[i] = int(sys.stdin.readline())
rope.sort(reverse=True)

for j in range(1, n+1):
    result = max(result, rope[j-1] * j)

print(result)
