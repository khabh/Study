import sys

target = sys.stdin.readline().rstrip()
start = list(sys.stdin.readline().rstrip())
while len(start) > len(target):
    if start.pop() == 'B':
        start.reverse()
if ''.join(start) != target:
    print('0')
else:
    print('1')
    