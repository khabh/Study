line = list(input())
for i in line:
    if i <= 'Z' and i >= 'A':
        print(chr((ord(i)-65+13) % 26+65), end="")
    elif i <= 'z' and i >= 'a':
        print(chr((ord(i)-97+13) % 26+97), end="")
    else:
        print(i, end="")
