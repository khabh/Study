# # 최소 칸의 개수 -> bfs
# n, m = map(int, input().split())
# d = []
# for i in range(n):
#     d.append(list(map(int, input())))


# def bfs(x, y):
#     # if d[x][y] == 0:
#     #     return

#     # 상 하 좌 우
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]

#     queue = [(x, y)]
#     while queue:
#         v = queue.pop(0)
#         for i in range(4):
#             nx = v[0]+dx[i]
#             ny = v[1]+dy[i]
#             if 0 <= nx < n and 0 <= ny < m:
#                 if d[nx][ny] == 1:
#                     d[nx][ny] += d[v[0]][v[1]]
#                     queue.append([nx, ny])


# bfs(0, 0)
# print(d[n-1][m-1])


from collections import deque
# 최소 칸의 개수 -> bfs
n, m = map(int, input().split())
d = []
for i in range(n):
    d.append(list(map(int, input())))


def bfs(x, y):
    # if d[x][y] == 0:
    #     return

    # 상 하 좌 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if d[nx][ny] == 1:
                    d[nx][ny] += d[x][y]
                    queue.append((nx, ny))


bfs(0, 0)
print(d[n-1][m-1])
