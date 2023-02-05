import sys
from collections import deque


def solve(index, count):
    global answer
    if count == L:
        vowel = not_vowel = 0
        for a in answer:
            if a in vowels:
                vowel += 1
            else:
                not_vowel += 1
        if vowel >= 1 and not_vowel >= 2:
            result.append("".join(answer))
        return

    for i in range(index, C - (L - count) + 1):
        answer.append(alphabet[i])
        solve(i + 1, count + 1)
        answer.pop()


read = sys.stdin.readline
L, C = map(int, read().split())
vowels = {'a', 'e', 'i', 'o', 'u'}
alphabet = sorted(read().split())
answer = deque()
result = deque()
solve(0, 0)
print('\n'.join(result))
