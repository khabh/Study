# import sys
# from collections import deque
#
#
# def bfs():
#     visit = {(0, 1, 0): 1}
#     queue = deque([(0, 1, 0)])
#     count = 0
#     while queue:
#         x, y, direction = queue.popleft()
#         case = visit[(x, y, direction)]
#         x, y = x + 1, y + 1
#         if direction != 1 and 0 <= y < N and home[x - 1][y] == '0':
#             if x == N and y == N - 1:
#                 count += case
#             else:
#                 if (x - 1, y, 0) not in visit:
#                     queue.append((x - 1, y, 0))
#                 visit[(x - 1, y, 0)] = visit.get((x - 1, y, 0), 0) + case
#         if direction and 0 <= x < N and home[x][y - 1] == '0':
#             if y == N and x == N - 1:
#                 count += case
#             else:
#                 if (x, y - 1, 1) not in visit:
#                     queue.append((x, y - 1, 1))
#                 visit[(x, y - 1, 1)] = visit.get((x, y - 1, 1), 0) + case
#         if 0 <= x < N and 0 <= y < N and home[x][y] == '0' and home[x - 1][y] == '0' and home[x][y - 1] == '0':
#             if x == y and x == N - 1:
#                 count += case
#             else:
#                 if (x, y, 2) not in visit:
#                     queue.append((x, y, 2))
#                 visit[(x, y, 2)] = visit.get((x, y, 2), 0) + case
#     return count
#
#
# read = sys.stdin.readline
# N = int(read())
# home = [read().split() for _ in range(N)]
# print(bfs())

import sys

read = sys.stdin.readline
N = int(read())
home = [read().split() for _ in range(N)]
dp = [[[0] * 3 for _ in range(N)] for _ in range(N)]
# 가로 0 세로 1 대각선 2
for i in range(1, N):
    if home[0][i] == '1':
        break
    dp[0][i][0] = 1

for i in range(1, N):
    for j in range(N):
        if home[i][j] == '1':
            continue
        if j:
            if home[i][j - 1] == '0' and home[i - 1][j] == '0':
                dp[i][j][2] = sum(dp[i - 1][j - 1])
            dp[i][j][0] = dp[i][j - 1][0] + dp[i][j - 1][2]
        dp[i][j][1] = dp[i - 1][j][1] + dp[i - 1][j][2]
print(sum(dp[N - 1][N - 1]))
