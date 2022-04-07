case=int(input())
for _ in range (case):
    line=list(input())
    if line[0]>'Z':
        line[0]=chr(ord(line[0])-32)
    for i in line:
        print(i,end="")
    print()
    