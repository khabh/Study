import sys


def get_dist(a, b):
    k1, k2, k3 = a
    k4, k5, k6 = b
    return ((k1 - k4) ** 2 + (k2 - k5) ** 2 + (k3 - k6) ** 2) ** 0.5


x1, y1, z1, x2, y2, z2, x3, y3, z3 = map(int, sys.stdin.readline().split())
start = (x1, y1, z1)
end = (x2, y2, z2)
c = (x3, y3, z3)
answer = sys.maxsize
while 1:
    mid = ((start[0] + end[0]) / 2, (start[1] + end[1]) / 2, (start[2] + end[2]) / 2)
    mid_dist = get_dist(mid, c)
    if abs(mid_dist - answer) < 10e-7:
        break
    if mid_dist < answer:
        answer = mid_dist
    if get_dist(start, c) > get_dist(end, c):
        start = mid
    else:
        end = mid
print('%.10f' % answer)
