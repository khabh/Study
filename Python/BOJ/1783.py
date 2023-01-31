import sys
# 높이 넓이
N, M = map(int, sys.stdin.readline().split())

if N >= 3:
    if M <= 4:
        print(M)
    elif M < 9:
        print(3 + (M - 3) // 2)
    else:
        print(M - 2)
elif N == 2:
    print(min((M - 1) // 2 + 1, 4))
else:
    print(1)
