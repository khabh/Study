import sys
case = int(sys.stdin.readline())

for _ in range(case):
    w = b = 0
    n = int(sys.stdin.readline())
    first = list(sys.stdin.readline())
    target = list(sys.stdin.readline())

    for i in range(n):
        if first[i] != target[i]:
            if first[i] == 'W':
                w += 1
            else:
                b += 1

    print(max(w, b))
