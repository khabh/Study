location = input()
x = ord(location[0])-ord('a')+1
y = int(location[1])

count = 0
steps = [(-1, -2), (-1, 2), (-2, -1), (-2, 1),
         (1, -2), (1, 2), (2, -1), (2, 1)]

for i in steps:
    nx = x + i[0]
    ny = y + i[1]
    if 1 <= nx <= 8 and 1 <= ny <= 8:
        count += 1

print(count)
