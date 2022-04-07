word=input()
for i in word:
    if i<'a':
        print(chr(ord(i)+32),end="")
    else:
        print(chr(ord(i)-32),end="")