def find_target(start, end, target, data):
    while start <= end:
        mid = (start + end)//2
        if data[mid] == target:
            return 'yes'
        if data[mid] > target:
            end = mid - 1
        else:
            start = mid+1

    return 'no'


n = int(input())
data = list(map(int, input().split()))
m = int(input())
find = list(map(int, input().split()))

data.sort()

for target in find:
    print(find_target(0, n-1, target, data), end=' ')
