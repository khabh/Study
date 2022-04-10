# 문제

# 코레스코 콘도에 있는 방은 NxN의 정사각형모양으로 생겼다.
# 방 안에는 옮길 수 없는 짐들이 이것저것 많이 있어서 영식이의 누울 자리를 차지하고 있었다.
# 영식이는 이 열악한 환경에서 누울 수 있는 자리를 찾아야 한다.
# 영식이가 누울 수 있는 자리에는 조건이 있다.
# 똑바로 연속해서 2칸 이상의 빈 칸이 존재하면 그 곳에 몸을 양 옆으로 쭉 뻗으면서 누울 수 있다.
# 가로로 누울 수도 있고 세로로 누울 수도 있다.
# 누울 때는 무조건 몸을 쭉 뻗기 때문에 반드시 벽이나 짐에 닿게 된다.
# (중간에 어정쩡하게 눕는 경우가 없다.)

N = int(input())
room = []
rowCnt = colCnt = 0
for _ in range(N):
    room.append(list(input()))

# 가로로 누울 수 있는 경우의 수 구하기
for i in room:
    cnt = 0
    for j in i:
        if j == '.':
            cnt += 1
        else:
            if cnt >= 2:
                rowCnt += 1
                cnt = 0
            else:
                cnt = 0
if cnt >= 2:
    rowCnt += 1


# 세로로 누울 수 있는 경우의 수 구하기
for i in range(N):
    cnt = 0
    for j in range(N):
        if room[j][i] == '.':
            cnt += 1
        else:
            cnt = 0
        if cnt == 2:
            colCnt += 1
            break

print(rowCnt, colCnt)
