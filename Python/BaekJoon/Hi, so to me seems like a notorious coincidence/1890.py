num = int(input())
array = []
for _ in range(num):
    array.append(list(map(int, input().split())))


def moveRight(x, y):
    global array
    if (x+array[x][y]) <= 3:
        dx = x+array[x][y]
