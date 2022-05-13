n, m = map(int, input().split())
length = list(map(int, input().split()))
result = []


def cut(array, target, start, end):
    total = 0
    if start > end:
        return
    mid = (start+end)//2
    for i in range(n):
        if array[i] >= mid:
            total += array[i] - mid
    if total == target:
        result.append(mid)
        return
    elif total > target:
        result.append(mid)
        cut(length, target, mid+1, max(length))
    else:
        cut(length, target, start, mid-1)


cut(length, m, 0, max(length))
print(max(result))
