import sys
from collections import deque


def bfs():
    global puzzle
    if puzzle == '123456780':
        return 0
    visit = {puzzle}
    zero = puzzle.index('0')
    queue = deque([(puzzle, 0, (zero // 3, zero % 3))])
    delta = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    while queue:
        n, count, (x, y) = queue.popleft()
        prev_zero = x * 3 + y
        for deltaX, deltaY in delta:
            X, Y = deltaX + x, deltaY + y
            if 0 <= X < 3 and 0 <= Y < 3:
                zero = X * 3 + Y
                new_puzzle = list(n)
                new_puzzle[zero], new_puzzle[prev_zero] = new_puzzle[prev_zero], new_puzzle[zero]
                temp = ''.join(new_puzzle)
                if temp not in visit:
                    if temp == '123456780':
                        return count + 1
                    visit.add(temp)
                    queue.append((temp, count + 1, (X, Y)))

    return '-1'


read = sys.stdin.readline
puzzle = ''.join(''.join(read().split()) for _ in range(3))
print(bfs())
