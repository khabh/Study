import sys

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))
for i in sorted(graph, key=lambda a: (a[0], a[1])):
    print(*i)
