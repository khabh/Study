from sys import stdin


def bfs(start):
    global result
    members = [start]
    n = start
    while True:
        visited[n] = True
        n = graph[n]
        if visited[n]:
            if n in members:
                result += members.index(n)
                return
            result += len(members)
            return
        else:
            members.append(n)


read = stdin.readline
for _ in range(int(read())):
    N = int(read())
    graph = [0]
    visited = [0] * (N + 1)
    result = 0
    for a in map(int, read().split()):
        graph.append(a)
    for i in range(1, N + 1):
        if not visited[i]:
            bfs(i)
    print(result)


