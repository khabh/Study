# n = int(input())
# numbers = list(map(int, input().split()))
# result = [1] * n
# for i in range(n - 1):
#     for j in range(i + 1, n):
#         if numbers[j] > numbers[i]:
#             result[j] = max(result[j], result[i] + 1)
# print(max(result))

n = int(input())
result = [0] * 1001
for i in map(int, input().split()):
    result[i] = max(result[:i]) + 1
print(max(result))
