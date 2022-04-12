alpha = ["c=", "c-", "dz=", 'd-', 'lj', 's=', 'nj', 'z=']
str = input()
for i in alpha:
    str = str.replace(i, "o")

print(len(str))
