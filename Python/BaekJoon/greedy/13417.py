import sys
from collections import deque
case = int(sys.stdin.readline())

for _ in range(case):
    n = int(sys.stdin.readline())
    str = list(sys.stdin.readline().split())

    result = deque(str[0])

    for i in range(1, n):
        if ord(str[i]) <= ord(result[0]):
            result.appendleft(str[i])
        else:
            result.append(str[i])

    print("".join(result))
