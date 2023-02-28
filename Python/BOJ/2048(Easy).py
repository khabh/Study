import sys
from collections import deque
import copy


def move_left(blocks):
    for i in range(N):
        temp = []
        prev = 0
        for j in range(N):
            if blocks[i][j]:
                if prev == blocks[i][j]:
                    temp[-1] *= 2
                    prev = 0
                else:
                    prev = blocks[i][j]
                    temp.append(blocks[i][j])
        while len(temp) < N:
            temp.append(0)
        blocks[i] = temp
    return blocks


def move_right(blocks):
    for i in range(N):
        temp = deque([])
        prev = 0
        for j in range(N - 1, -1, -1):
            if blocks[i][j]:
                if prev == blocks[i][j]:
                    temp[0] *= 2
                    prev = 0
                else:
                    prev = blocks[i][j]
                    temp.appendleft(blocks[i][j])
        while len(temp) < N:
            temp.appendleft(0)
        blocks[i] = temp
    return blocks


def move_down(blocks):
    for i in range(N):
        temp = deque([])
        prev = 0
        for j in range(N - 1, -1, -1):
            if blocks[j][i]:
                if prev == blocks[j][i]:
                    temp[0] *= 2
                    prev = 0
                else:
                    prev = blocks[j][i]
                    temp.appendleft(blocks[j][i])
        while len(temp) < N:
            temp.appendleft(0)
        for j in range(N):
            blocks[j][i] = temp[j]
    return blocks


def move_up(blocks):
    for i in range(N):
        temp = []
        prev = 0
        for j in range(N):
            if blocks[j][i]:
                if prev == blocks[j][i]:
                    temp[-1] *= 2
                    prev = 0
                else:
                    prev = blocks[j][i]
                    temp.append(blocks[j][i])
        while len(temp) < N:
            temp.append(0)
        for j in range(N):
            blocks[j][i] = temp[j]
    return blocks


def dfs(blocks, count):
    global result
    result = max(max(max(block) for block in blocks), result)
    if count == 5:
        return
    dfs(move_left(copy.deepcopy(blocks)), count + 1)
    dfs(move_right(copy.deepcopy(blocks)), count + 1)
    dfs(move_up(copy.deepcopy(blocks)), count + 1)
    dfs(move_down(copy.deepcopy(blocks)), count + 1)


read = sys.stdin.readline
N = int(read())
graph = [list(map(int, read().split())) for _ in range(N)]
result = 0
dfs(graph, 0)
print(result)
