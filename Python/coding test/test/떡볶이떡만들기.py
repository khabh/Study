n, m = map(int, input().split())
length = list(map(int, input().split()))


def cut(start, end, length, target):
    while start <= end:
        mid = (start + end) // 2
        total = 0
        for i in length:
            if i > mid:
                total += i - mid

        if total < m:
            end = mid - 1
        else:
            start = mid + 1
            result = mid

    return result


result = cut(0, max(length), length, m)
print(result)
