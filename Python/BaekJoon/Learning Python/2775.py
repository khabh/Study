def findMem(floor, n):
    if floor == 0:
        return [i for i in range(1, n+1)]

    array = findMem(floor-1, n)

    return [sum(array[0:i]) for i in range(1, n+1)]


case = int(input())

for _ in range(case):
    k = int(input())
    n = int(input())
    result = findMem(k, n)
    print(result[n-1])
