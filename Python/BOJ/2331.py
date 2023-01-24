from sys import stdin

read = stdin.readline
A, P = map(int, read().split())
result = {}
count = 0
while A not in result:
    result[A] = count
    A = sum(map(lambda x: int(x) ** P, str(A)))
    count += 1
print(result[A])
