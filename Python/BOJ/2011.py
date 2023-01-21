import sys

code = list(map(int, input()))
if code[0] == 0:
    print(0)
    sys.exit()
code = [0] + code
result = [0] * (len(code))
result[0] = result[1] = 1
for i in range(2, len(code)):
    if code[i] > 0:
        result[i] = result[i - 1]
    value = code[i] + code[i - 1] * 10
    if 10 <= value <= 26:
        result[i] += result[i - 2]

print(result[-1] % 1000000)
