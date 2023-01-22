import sys

n1 = list(sys.stdin.readline().rstrip())
n2 = []
for _ in range(int(sys.stdin.readline())):
    command = list(sys.stdin.readline().split())
    if command[0] == 'L':
        if n1:
            n2.append(n1.pop())
    elif command[0] == 'D':
        if n2:
            n1.append(n2.pop())
    elif command[0] == 'B':
        if n1:
            n1.pop()
    else:
        n1.append(command[1])

n1.extend(reversed(n2))
print(*n1, sep='')


# 첫번째 풀이

n = list(sys.stdin.readline().rstrip())
maxIndex = len(n)
cursor = maxIndex
for _ in range(int(sys.stdin.readline().rstrip())):
    command = sys.stdin.readline()
    if command[0] == 'P':
        n.insert(cursor, command[2])
        maxIndex += 1
        cursor += 1
        continue
    elif command[0] == 'L':
        cursor -= 1
    elif command[0] == 'D':
        cursor += 1
    if cursor != 0:
        n.pop(cursor - 1)
        cursor -= 1
print(*n, sep='')

