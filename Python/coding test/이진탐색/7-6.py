array = [0] * 1000001

n = int(input())
for i in input().split():
    array[i] = 1

m = int(input())
need = list(map(int, input().split()))

for i in need:
    if array[need] == 1:
        print('yes', end=" ")
    else:
        print('no', end=" ")
