# 메모리 초과
num = int(input())
array = []
move = [[0, 0]]
x = y = cnt = 0
for _ in range(num):
    array.append(list(map(int, input().split())))


def moveLeft(x1, y1):
    global array
    global move
    global cnt
    global num
    if (x1+array[x1][y1]) <= num-1:
        if x1+array[x1][y1] == num-1 and y1 == num-1:
            cnt += 1
        else:
            move.append([x1+array[x1][y1], y1])


def moveDown(x1, y1):
    global array
    global move
    global cnt
    global num
    if (y1+array[x1][y1]) <= num-1:
        if (y1+array[x1][y1]) == num-1 and x1 == num-1:
            cnt += 1
        else:
            move.append([x1, y1+array[x1][y1]])


i = 0

while True:
    moveLeft(move[i][0], move[i][1])
    moveDown(move[i][0], move[i][1])
    if i+1 <= len(move)-1:
        i += 1
    else:
        break

print(cnt)
