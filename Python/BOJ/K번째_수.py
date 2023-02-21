import sys

read = sys.stdin.readline
N = int(read())
k = int(read())
start = 1
end = N * N
while start <= end:
    mid = (start + end) // 2
    temp = 0
    for i in range(1, N + 1):
        temp += min(mid // i, N)
    if temp >= k:
        end = mid - 1
    else:
        start = mid + 1
print(start)
