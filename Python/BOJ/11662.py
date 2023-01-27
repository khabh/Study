import sys


def get_dist(a):
    return (((x1 + deltaX1 * a) - (x3 + deltaX2 * a)) ** 2 + ((y1 + deltaY1 * a) - (y3 + deltaY2 * a)) ** 2) ** 0.5


x1, y1, x2, y2, x3, y3, x4, y4 = map(int, sys.stdin.readline().split())
deltaX1 = x2 - x1
deltaX2 = x4 - x3
deltaY1 = y2 - y1
deltaY2 = y4 - y3
s = 0
e = 1
while abs(e - s) > 1e-9:
    p = (2 * s + e) / 3
    q = (s + 2 * e) / 3
    distP = get_dist(p)
    distQ = get_dist(q)
    if distP > distQ:
        s = p
    else:
        e = q
print("%.16f" % get_dist(e))
