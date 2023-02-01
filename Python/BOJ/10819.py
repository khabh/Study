def bfs(cnt):
    global result
    if cnt == N:
        sum = 0
        for i in range(N - 1):
            sum += abs(place[i] - place[i + 1])
        if result < sum:
            result = sum
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            place.append(num[i])
            bfs(cnt + 1)
            place.pop()
            visited[i] = False


N = int(input())
result = 0
num = list(map(int, input().split()))
visited = [False] * N
place = []
bfs(0)
print(result)
