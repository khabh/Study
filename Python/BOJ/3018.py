import sys
from collections import deque

read = sys.stdin.readline
N = int(read())
music = deque()
for _ in range(int(read())):
    joined = set(list(map(int, read().split()))[1:])
    if 1 in joined:
        music.append(joined)
        continue
    for i in range(len(music)):
        for n in joined:
            if n in music[i]:
                for new in joined - music[i]:
                    music[i].add(new)
                break
result = music[0]
for i in range(1, len(music)):
    result = result & music[i]
print(*sorted(result), sep='\n')
