import sys


read = sys.stdin.readline
K, N = map(int, read().rstrip().split())
LAN = [int(read()) for _ in range(K)]
start = 1
end = sum(LAN) // N
while start <= end:
    mid = (end + start) // 2
    if sum([x // mid for x in LAN]) >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)
