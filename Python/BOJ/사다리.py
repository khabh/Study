import sys
import math

x, y, c = map(float, sys.stdin.readline().split())
start = 0
end = min(x, y)
while end - start >= 10e-4:
    mid = (end + start) / 2
    a = mid / (y ** 2 - mid ** 2) ** 0.5 * c + mid / (x ** 2 - mid ** 2) ** 0.5 * c
    if mid >= a:
        start = mid
    else:
        end = mid
print('%.3f' % round(end, 3))
