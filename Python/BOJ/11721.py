value = input()
count = len(value)
i = 0
while i + 10 <= count:
    print(value[i: i + 10])
    i += 10
print(value[i:])
