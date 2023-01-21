import sys

n = int(input())
members = list(sys.stdin.readline().split() for _ in range(n))
for member in sorted(members, key=lambda x: int(x[0])):
    print(*member)