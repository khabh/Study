n, m = map(int, input().split())

if n == 1:
    # 세로 길이가 1일 때는 4가지 움직임 중 어떤 것도 수행할 수 없다
    result = 1
elif n == 2:
    # 세로 길이가 2인 경우에는 2,3번 움직임만 수행할 수 있기 때문에 이동횟수가 4를 넘으면 안 된다
    result = min((m-1)//2+1, 4)
elif m <= 6:
    # 세로 길이가 3이상이기 때문에 세로 움직임에는 제약이 없다
    # 항상 오른쪽으로 이동해야 하므로 1 +2 + 2 + 1은 6 즉 가로 길이가 6 이하일 경우 이동횟수는 최대 4번
    # 이동횟수가 4번을 넘지 않는 경우는 오른쪽으로 한 칸씩만 이동 -> 가로 길이가 이동횟수
    result = min(4, m)
else:
    # 이 경우 이동횟수는 4 이상이기 때문에 4가지 움직임을 모두 수행해야 한다
    # 세로 움직임의 경우 위,아래로 이동이 모두 가능하기 때문에 제약이 없다
    # 반면 가로의 경우 오른쪽으로만 이동해야 하기 때문에 오른쪽으로 이동하는 칸을 최소화해야 한다 -> 1번 혹은 4번으로
    # 2,3번 움직임에서 두 칸을 낭비하기 때문에 최종적으로 방문한 칸은 가로 길이 -2
    result = m - 2

print(result)