import sys

while True:
    line = sys.stdin.readline().rstrip('\n')
    if not line:
        break
    l = u = d = s = 0
    for i in line:
        if i.isdigit():
            d += 1
        elif i.islower():
            l += 1
        elif i.isupper():
            u += 1
        else:
            s += 1
    print(l, u, d, s)
