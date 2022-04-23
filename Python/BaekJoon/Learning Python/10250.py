case = int(input())
for i in range(case):
    h, w, n = map(int, input().split())
    if n % h == 0:
        print('%d%02d' % (h, n//h))
    else:
        print("%d%02d" % (n % h, n//h+1))
