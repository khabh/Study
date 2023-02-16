import sys
from collections import deque


def prove():
    if answer[0] != 1:
        return '0'
    queue = deque([1])
    index = 1
    count = 0
    while 1:
        n = queue[0]
        if not graph[n]:
            queue.popleft()
            continue
        while answer[index] in graph[n]:
            count += 1
            graph[answer[index]].remove(n)
            queue.append(answer[index])
            index += 1
            if index == N:
                return '1'
        if count != len(graph[n]):
            return '0'
        else:
            count = 0
            queue.popleft()
    return '1'


read = sys.stdin.readline
N = int(read())
graph = [set() for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, read().split())
    graph[a].add(b)
    graph[b].add(a)
answer = list(map(int, read().split()))
print(prove())
