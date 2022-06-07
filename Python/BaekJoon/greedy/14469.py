import sys
case = int(sys.stdin.readline())
times = []

for _ in range(case):
    times.append(
        list(map(int, sys.stdin.readline().split())))

times.sort()
result = sum(times[0])


for time in times[1:]:
    if time[0] >= result:
        result = time[0] + time[1]
    else:
        result += time[1]

print(result)
