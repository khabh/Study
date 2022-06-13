import sys

fomula = sys.stdin.readline()
add = fomula.split("-")

for i in range (len(add)):
    if len(add[i]) == 1:
        add[i] = int(add[i])
    else:
        add[i] = sum(map(int,add[i].split('+')))
        
result = add[0]
for i in range(1,len(add)):
    result -= add[i]

print(result)