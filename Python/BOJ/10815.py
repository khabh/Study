import sys

read = sys.stdin.readline
N = read().rstrip()
card = {}
for i in read().split():
    card[i] = 0
M = read()
print("".join('1 ' if x in card else '0 ' for x in read().split()))
