import sys

X, Y, W, S = map(int, sys.stdin.readline().split())
if W * 2 <= S:
    result = W * (X + Y)
else:
    result = S * min(X, Y) + W * abs(X - Y)
if (X + Y) % 2:
    print(min(result, (max(X, Y) - 1) * S + W))
else:
    print(min(result, max(X, Y) * S))
