import sys


def dfs(count):
    if count == len(blank):
        return True
    a, b = blank[count]
    able_numbers = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
    temp_a, temp_b = a // 3 * 3, b // 3 * 3
    for i in range(temp_a, temp_a + 3):
        for j in range(temp_b, temp_b + 3):
            if graph[i][j] in able_numbers:
                able_numbers.remove(graph[i][j])
    for i in range(9):
        if graph[a][i] in able_numbers:
            able_numbers.remove(graph[a][i])
        if graph[i][b] in able_numbers:
            able_numbers.remove(graph[i][b])
    for _ in range(len(able_numbers)):
        number = able_numbers.pop()
        graph[a][b] = number
        if dfs(count + 1):
            return True
    graph[a][b] = '0'


graph = [sys.stdin.readline().split() for _ in range(9)]
blank = []
for x in range(9):
    for y in range(9):
        if graph[x][y] == '0':
            blank.append((x, y))
dfs(0)
print('\n'.join(' '.join(x) for x in graph))
