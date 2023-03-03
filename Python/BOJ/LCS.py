import sys

read = sys.stdin.readline
A = read().rstrip()
B = read().rstrip()
prev = [0] * (len(A) + 1)
for i in range(len(B)):
    cache = [0] * (len(A) + 1)
    for j in range(1, len(A) + 1):
        if A[j - 1] == B[i]:
            cache[j] = prev[j - 1] + 1
        else:
            cache[j] = max(prev[j], cache[j - 1])
    prev = cache
print(max(prev))
