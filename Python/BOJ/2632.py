import sys


def solve(pizza, piece_count):
    sum_pizza = sum(pizza)
    result = [1] + [0 for _ in range(K)]
    if sum_pizza <= K:
        result[sum_pizza] += 1
    for i in range(piece_count):
        total = pizza[i]
        if K >= total:
            result[total] += 1
        else:
            continue
        for j in range(i + 1, piece_count + i - 1):
            total += pizza[j % piece_count]
            if K >= total:
                result[total] += 1
            else:
                break
    return result


read = sys.stdin.readline
K = int(read())
m, n = map(int, read().split())
A = list(int(read()) for _ in range(m))
B = list(int(read()) for _ in range(n))
case = [solve(A, m), solve(B, n)]
count = 0
for i in range(K + 1):
    count += case[0][i] * case[1][K - i]
print(count)
