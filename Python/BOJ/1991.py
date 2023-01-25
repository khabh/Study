import sys


def preorder():
    visited = {key: False for key in graph.keys()}
    stack = ['A']
    result = 'A'
    while stack:
        left, right = graph[stack[-1]]
        if left != '.' and not visited[left]:
            visited[left] = True
            result += left
            stack.append(left)
            continue
        if right != '.' and not visited[right]:
            visited[right] = True
            result += right
            stack.append(right)
        else:
            stack.pop()
    print(result)


def inorder():
    visited = {key: False for key in graph.keys()}
    visited['A'] = True
    stack = ['A']
    result = ''
    while stack:
        n = stack[-1]
        left, right = graph[n]
        if left != '.' and not visited[left]:
            visited[left] = True
            stack.append(left)
            continue
        result += stack.pop()
        if right != '.' and not visited[right]:
            visited[right] = True
            stack.append(right)
            continue
    print(result)


def postorder():
    visited = {key: False for key in graph.keys()}
    visited['A'] = True
    stack = ['A']
    result = ''
    while stack:
        n = stack[-1]
        left, right = graph[n]
        if left != '.' and not visited[left]:
            visited[left] = True
            stack.append(left)
            continue
        if right != '.' and not visited[right]:
            visited[right] = True
            stack.append(right)
            continue
        result += stack.pop()
    print(result)


read = sys.stdin.readline
N = int(read())
graph = {}
for _ in range(N):
    a, b, c = read().split()
    graph[a] = [b, c]
preorder()
inorder()
postorder()