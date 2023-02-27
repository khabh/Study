import sys


def get_flip_count(count, lights):
    for i in range(N - 1):
        if lights[i] != target[i]:
            count += 1
            for j in range(i, min(i + 3, N)):
                lights[j] = '0' if lights[j] == '1' else '1'
    if lights[-1] == target[-1]:
        return count
    return -1


read = sys.stdin.readline
N = int(read())
start = list(read().rstrip())
target = list(read().rstrip())
first_answer = get_flip_count(0, start[:])
for k in range(2):
    start[k] = '0' if start[k] == '1' else '1'
second_answer = get_flip_count(1, start)
if first_answer < 0 and second_answer < 0:
    print('-1')
elif first_answer > -1 and second_answer > -1:
    print(min(first_answer, second_answer))
else:
    print(max(first_answer, second_answer))
