import sys

s = sys.stdin.readline().rstrip()
result = [s]
for i in range(1, len(s)):
    result.append(s[i:])
for i in sorted(result):
    print(i)
