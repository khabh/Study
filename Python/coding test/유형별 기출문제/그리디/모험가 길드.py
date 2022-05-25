from collections import deque

n = int(input())
fear = list(map(int, input().split()))

fear.sort(reverse=True)

fear = deque(fear[:])

group = 0

while fear:
    if len(fear) >= fear[0]:
        group += 1
        for _ in range(fear[0]):
            fear.popleft()

    else:
        break

print(group)
