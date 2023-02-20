import sys

read = sys.stdin.readline
N, M = map(int, read().split())
n = []
end = 0
start = 0
for time in list(map(int, read().split())):
    n.append(time)
    end += time
    start = max(start, time)
answer = 0
while start <= end:
    mid = (start + end) // 2
    count = temp = 0
    for i in n:
        if temp + i > mid:
            count += 1
            temp = i
        else:
            temp += i
        if count > M:
            break
    if count < M:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1
print(answer)
