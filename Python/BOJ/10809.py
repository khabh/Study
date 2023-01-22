import sys

result = [-1] * 26
index = 0
for i in map(lambda x: ord(x) - 97, sys.stdin.readline().rstrip()):
    if result[i] == -1:
        result[i] = index
    index += 1
print(*result)
