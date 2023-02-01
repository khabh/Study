from collections import deque


def get_digits(num):
    if num in cache:
        return cache[num]
    result = []
    temp = num
    for _ in range(4):
        temp, mod = divmod(temp, 10)
        result.append(mod)
    cache[num] = result
    return result

def bfs(start):
    if start == B:
        return 0
    queue = deque([start])
    visited = {start: 0}
    while queue:
        n = queue.popleft()
        digit = get_digits(n)
        for num in prime:
            if num not in visited:
                current_digit = get_digits(num)
                cnt = 0
                for i in range(4):
                    if digit[i] != current_digit[i]:
                        cnt += 1
                        if cnt == 2:
                            break
                if cnt == 1:
                    visited[num] = visited[n] + 1
                    if num == B:
                        return visited[num]
                    queue.append(num)
    return "Impossible"

prime = [True] * 10000
for i in range(2, 10000):
    if prime[i]:
        for j in range(i * 2, 10000, i):
            prime[j] = False
prime = [x for x in range(1000, 10000) if prime[x]]
cache = {}
for _ in range(int(input())):
    A, B = map(int, input().split())
    print(bfs(A))
