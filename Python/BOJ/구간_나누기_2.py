import sys

read = sys.stdin.readline
N, M = map(int, read().split())
n = []
start = 0
min_num = sys.maxsize
max_num = 0
for num in map(int, read().split()):
    n.append(num)
    if num < min_num:
        min_num = num
    if num > max_num:
        max_num = num
end = max_num - min_num
while start <= end:
    mid = (start + end) // 2
    count = 1
    min_num = max_num = n[0]
    for num in n:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num
        if max_num - min_num > mid:
            count += 1
            if count > M:
                break
            min_num = max_num = num
    if count > M:
        start = mid + 1
    else:
        end = mid - 1
print(start)
