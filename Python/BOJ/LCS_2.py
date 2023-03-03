import sys

read = sys.stdin.readline
A = read().rstrip()
B = read().rstrip()
prev = [''] * (len(A) + 1)
for i in range(len(B)):
    cache = [''] * (len(A) + 1)
    for j in range(1, len(A) + 1):
        if A[j - 1] == B[i]:
            cache[j] = prev[j - 1] + B[i]
        else:
            cache[j] = prev[j] if len(prev[j]) > len(cache[j - 1]) else cache[j - 1]
    prev = cache
print(len(prev[-1]))
print(prev[-1])
