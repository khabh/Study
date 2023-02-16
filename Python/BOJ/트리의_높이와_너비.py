import sys


def solve(levels):
    max_level = -1
    max_width = 0
    for level, location in sorted(levels.items()):
        width = location[-1] - location[0] + 1
        if max_width < width:
            max_level = level
            max_width = width
    print(max_level, max_width)


def dfs(start):
    result = {}
    stack = [(start, 1)]
    index = 1
    while stack:
        n, level = stack[-1]
        left, right = graph[n]
        if left != -1:
            stack.append((left, level + 1))
            graph[n][0] = -1
            continue
        cache = result.get(level, [])
        cache.append(index)
        result[level] = cache
        index += 1
        stack.pop()
        if right != -1:
            stack.append((right, level + 1))
            graph[n][1] = -1

    solve(result)


read = sys.stdin.readline
child = set()
N = int(read())
graph = [0] * (N + 1)
for _ in range(N):
    a, b, c = map(int, read().split())
    child.add(b)
    child.add(c)
    graph[a] = [b, c]
for i in range(1, N + 1):
    if i not in child:
        dfs(i)
        break
