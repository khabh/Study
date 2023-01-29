import sys

num = list(map(int, sys.stdin.readline().rstrip()))
if sum(num) % 3:
    print('-1')
else:
    num.sort(reverse=True)
    if num[-1] != 0:
        print('-1')
    else:
        print(''.join(str(x) for x in num))
