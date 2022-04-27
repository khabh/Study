import math
case = int(input())
for _ in range(case):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = math.sqrt((x1-x2)**2+(y1-y2)**2)  # 원점 사이 거리
    rTotal = r1+r2  # 반지름의 합

    if distance == 0 and r1 == r2:
        print(-1)
    elif distance == rTotal or abs(r1-r2) == distance:
        print(1)
    elif abs(r1-r2) < distance < (r1+r2):
        print(2)
    else:
        print(0)
