import sys

E, S, M = map(int, sys.stdin.readline().split())
i = 0

while True:
    year = S + 28 * i
    if not (year - E) % 15 and not (year - M) % 19:
        result = year
        break
    i += 1
print(result)
