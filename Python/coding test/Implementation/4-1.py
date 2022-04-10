# 여행가 A는 N*N 크기의 정사각형 공간 위에 서 있다. 이 공간은 1*1 크기의 정사각형으로 나누어져 있다.
# 가장 왼쪽 좌표는 (1,1)이며, 가장 오른쪽 아래 좌표는 (N,N)에 해당한다.
# 여행가는 상,하,좌,우 방향으로 이동할 수 있으며, 시작 좌표는 항상 (1,1)이다.
# 우리 앞에는 여행가가 이동할 계획이 적힌 계획서가 놓여 있다.

# 계획서에는 하나의 줄에 띄어쓰기를 기준으로 하여 L,R,U,D(왼쪽,오른쪽,위,아래) 중 하나의 문자가 반복적으로 적혀 있다.
# 이때 여행가가 정사각형 공간을 벗어나는 움직임은 무시된다.

num = int(input())
x = y = 1
moving = list(map(str, input().split()))

changeX = [0, 0, -1, 1]
changeY = [-1, 1, 0, 0]
moveType = ['L', 'R', 'U', 'D']

for i in moving:
    nx = x+changeX[moveType.index(i)]
    ny = y+changeY[moveType.index(i)]
    if nx < 1 or ny < 1 or nx > num or ny > num:
        continue
    x = nx
    y = ny

print(x, y)
