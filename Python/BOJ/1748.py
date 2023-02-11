import sys

N = int(sys.stdin.readline())
count = 9
length = 1
result = 0
while N:
    if N > count:
        result += count * length
        N -= count
    else:
        result += N * length
        break
    count *= 10
    length += 1
print(result)
