def find(array, target, start, end):
    if start > end:
        return 'no'
    mid = (start+end)//2
    if array[mid] == target:
        return 'yes'
    elif array[mid] > target:
        return find(array, target, start, mid-1)
    else:
        return find(array, target, mid+1, end)


n = int(input())
have = list(map(int, input().split()))
have.sort()

m = int(input())
need = list(map(int, input().split()))

for i in need:
    print(find(have, i, 0, n-1), end=' ')
