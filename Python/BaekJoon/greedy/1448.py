import sys

n = int(sys.stdin.readline())
side = [0] * n
result = -1

for j in range(n):
    side[j] = int(sys.stdin.readline())
side.sort(reverse=True)

for i in range(n-2):
    sides = side[i+2] + side[i+1]
    if side[i] < sides:
        result = side[i] + sides
        break
        
print(result)