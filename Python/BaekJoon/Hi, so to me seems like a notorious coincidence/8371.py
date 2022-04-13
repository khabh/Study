case = int(input())
origin = input()
pupil = input()
cnt = 0
for i in range(case):
    if origin[i] != pupil[i]:
        cnt += 1

print(case-cnt)
