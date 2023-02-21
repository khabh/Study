import sys

read = sys.stdin.readline
N, M = map(int, read().split())
rides = list(map(int, read().split()))
if N <= M:
    print(N)
    sys.exit()
start = 0
end = sys.maxsize
while start <= end:
    mid = (start + end) // 2
    temp = M
    for ride in rides:
        temp += mid // ride
    if temp < N:
        start = mid + 1
    else:
        end = mid - 1
count = M + 1
for ride in rides:
    count += start // ride
for i in range(M - 1, -1, -1):
    if not start % rides[i]:
        count -= 1
        if N == count:
            print(i + 1)
            break
