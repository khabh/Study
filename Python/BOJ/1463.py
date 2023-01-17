# 첫 번째 풀이
def count(number):
    if number == 1:
        return 0
    if number == 2 or number == 3:
        return 1
    if result[number] != 0:
        return result[number]
    min_count = 1000002
    if number % 3 == 0:
        min_count = min(count(int(number / 3)) + 1, min_count)
    if number % 2 == 0:
        min_count = min(count(int(number / 2)) + 1, min_count)
    min_count = min(count(number - 1) + 1, min_count)
    result[number] = min_count
    return min_count


n = int(input())
result = [0 for i in range(1000001)]
print(count(n))


# 두 번째 풀이
n = int(input())
result = [0] * (n + 1)

for i in range(2, n + 1):
    result[i] = result[i - 1] + 1
    if i % 2 == 0:
        result[i] = min(result[i], result[i // 2] + 1)
    if i % 3 == 0:
        result[i] = min(result[i], result[i // 3] + 1)
print(result[n])
