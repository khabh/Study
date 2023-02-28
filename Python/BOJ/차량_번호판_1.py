import sys

plate = sys.stdin.readline().rstrip()
answer = 26 if plate[0] == 'c' else 10
for i in range(1, len(plate)):
    if plate[i] == 'c':
        if plate[i - 1] == 'c':
            answer *= 25
        else:
            answer *= 26
    if plate[i] == 'd':
        if plate[i - 1] == 'd':
            answer *= 9
        else:
            answer *= 10
print(answer)
