import sys


def prove():
    if answer[0] != 1:
        return '0'
    stack = [1]
    index = 1
    while stack:
        n = stack[-1]
        if not len(graph[n]):
            stack.pop()
            continue
        if answer[index] in graph[n]:
            graph[n].remove(answer[index])
            graph[answer[index]].remove(n)
            stack.append(answer[index])
            index += 1
            if index == n:
                return '1'
        else:
            return '0'
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
