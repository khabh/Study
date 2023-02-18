import sys

read = sys.stdin.readline
N = int(read())
value = {}
for _ in range(N):
    word = list(read().rstrip())
    for index, alphabet in enumerate(word[::-1]):
        value[alphabet] = value.get(alphabet, 0) + 10 ** index
result = 0
num = 9
for count in sorted((x[1] for x in value.items()), reverse=True):
    result += num * count
    num -= 1
print(result)
