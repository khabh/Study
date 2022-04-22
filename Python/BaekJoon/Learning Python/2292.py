num = int(input())

i = 1
group = 1
while i < num:
    i += group*6
    group += 1

print(group)
