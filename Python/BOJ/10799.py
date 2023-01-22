import sys


n = sys.stdin.readline().rstrip().replace('()', '0')
count = 0
result = 0
for i in n:
    if i == '(':
        result += 1
        count += 1
    elif i == ')':
        count -= 1
    else:
        result += count
print(result)
