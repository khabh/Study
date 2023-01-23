import sys

n = int(sys.stdin.readline())
result = ''

if n == 0:
    print('0')
    sys.exit()

while n != 0:
    if n % -2:
        result = '1' + result
        n = n // -2 + 1
        continue
    result = '0' + result
    n = n // -2

print(result)
