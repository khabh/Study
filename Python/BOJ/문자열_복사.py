import sys

read = sys.stdin.readline
S = read().rstrip()
P = read().rstrip()
cache = set()
result = 0
for i in range(1, len(S) + 1):
    for j in range(len(S) - i + 1):
        cache.add(S[j:j + i])
index = 0
while index < len(P):
    for i in range(1, len(P) - index + 1):
        if P[index: index + i] not in cache:
            result += 1
            index = index + i - 1
            break
        if index + i == len(P):
            result += 1
            index = len(P)
            break
print(result)

