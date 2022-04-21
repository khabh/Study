num = int(input())
i = 0
group = 0

while i < num:
    i += group+1
    group += 1

startPoint = i-group+1

if group % 2 == 0:
    print("%d/%d" % (num-startPoint+1, group-(num-startPoint)))
else:
    print("%d/%d" % (group-(num-startPoint), num-startPoint+1))
