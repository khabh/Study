import sys


def first():
    global answer
    if N < 3:
        return
    for i in range(1, N - 1):
        for j in range(i + 1, N):
            a, b = sum(row[:i]), sum(row[i:j])
            result = a * b * (total - a - b)
            if answer < result:
                answer = result


def second():
    global answer
    if M < 3:
        return
    for i in range(1, M - 1):
        for j in range(i + 1, M):
            a, b = sum(column[:i]), sum(column[i:j])
            result = a * b * (total - a - b)
            if answer < result:
                answer = result


def third():
    global answer
    if N < 2 or M < 2:
        return
    for i in range(1, N):
        for j in range(1, M):
            a, b = sum(sum(x[:j]) for x in num[:i]), sum(column[j:])
            c, d = sum(sum(x[j:]) for x in num[:i]), sum(column[:j])
            result = max(a * b * (total - a - b), c * d * (total - c - d))
            if answer < result:
                answer = result


def fourth():
    global answer
    if N < 2 or M < 2:
        return
    for i in range(1, N):
        for j in range(1, M):
            a, b = sum(sum(x[:j]) for x in num[:i]), sum(row[i:])
            c, d = sum(sum(x[:j]) for x in num[i:]), sum(row[:i])
            result = max(a * b * (total - a - b), c * d * (total - c - d))
            if answer < result:
                answer = result

N, M = map(int, sys.stdin.readline().split())
num = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
row = [sum(num[x]) for x in range(N)]
column = [sum(x[i] for x in num) for i in range(M)]
total = sum(row)
answer = 0

first()
second()
third()
fourth()
print(answer)