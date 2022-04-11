# 8*8의 자표 평면에서 나이트는 L자 형태로만 이동할 수 있으며 정원 밖으로는 나갈 수 없다.
start = input()
row = int(start[1])
col = (ord(start[0])-97)+1

steps = [(-2, -1), (-2, 1), (2, -1), (2, 1),
         (1, 2), (1, -2), (-1, 2), (-1, -2)]
cnt = 0

for i in steps:
    nRow = row+i[0]
    nCol = col+i[1]

    if nRow >= 1 and nRow <= 8 and nCol >= 1 and nCol <= 8:
        cnt += 1

print(cnt)
