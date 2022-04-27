n = int(input())

person = []
for _ in range(n):
    person.append(list(map(int, input().split())))

for i in range(n):
    cnt = 1

    for j in range(n):
        if i == j:
            continue
        else:
            if person[j][0] > person[i][0] and person[j][1] > person[i][1]:
                cnt += 1

    print(cnt, end=" ")
