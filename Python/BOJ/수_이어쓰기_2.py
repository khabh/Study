import sys

N, k = map(int, sys.stdin.readline().split())
count = 1
while 1:
    length = 9 * 10 ** (count - 1) * count
    if k > length:
        k -= length
        count += 1
    else:
        break
a, b = divmod(k, count)
result = 10 ** (count - 1) + a - 1
if b:
    result += 1
if result > N:
    print('-1')
else:
    print(str(result)[b - 1])
