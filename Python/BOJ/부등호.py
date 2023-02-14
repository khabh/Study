import sys


def dfs(count, index):
    global result
    if count == N:
        if not result[1]:
            result[1] = ''.join(map(str, answer))
        else:
            result[0] = ''.join(map(str, answer))
        return
    if sign[count] == '>':
        for i in range(index):
            if not visit[i]:
                visit[i] = True
                answer.append(i)
                dfs(count + 1, i)
                visit[i] = False
                answer.pop()
    else:
        for i in range(index + 1, 10):
            if not visit[i]:
                visit[i] = True
                answer.append(i)
                dfs(count + 1, i)
                visit[i] = False
                answer.pop()


read = sys.stdin.readline
N = int(read())
sign = list(read().split())
visit = [False] * 10
answer = []
result = ['', '']
for i in range(10):
    visit[i] = True
    answer.append(i)
    dfs(0, i)
    answer.pop()
    visit[i] = False
print('\n'.join(result))