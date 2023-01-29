import sys

result = []
for i in range(1, 6):
    if sys.stdin.readline().find('FBI') != -1:
        result.append(str(i))

if len(result) == 0:
    print('HE GOT AWAY!')
else:
    print(' '.join(result))
