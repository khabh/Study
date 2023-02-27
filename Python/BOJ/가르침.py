import sys


def count_word():
    global result
    count = 0
    for word in words:
        can_learn = 1
        for alphabet in word:
            if alphabet not in taught:
                can_learn = 0
                break
        if can_learn:
            count += 1
    result = max(result, count)


def dfs(index):
    if len(taught) >= K:
        if len(taught) == K:
            count_word()
        return
    if K - len(taught) > len(new_alpha) - index:
        return
    dfs(index + 1)
    taught.add(new_alpha[index])
    dfs(index + 1)
    taught.remove(new_alpha[index])


read = sys.stdin.readline
N, K = map(int, read().split())
words = []
new_alpha = set()
for _ in range(N):
    word = list(set(read()[4:-5]))
    words.append(word)
    for alphabet in word:
        new_alpha.add(alphabet)
taught = {'a', 'n', 't', 'c', 'i'}
new_alpha = list(new_alpha.difference(taught))
if len(new_alpha) + 5 <= K:
    print(N)
else:
    result = 0
    dfs(0)
    print(result)
