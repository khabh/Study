case=int(input())
for i in range (case):
    student=list(map(int,input().split()))
    del student[0]
    student.sort()
    gap=[]
    for j in range (len(student)-1):
        gap.append(student[j+1]-student[j])
    print("Class %d"%(i+1))
    print("Max %d, Min %d, Largest gap %d"%(max(student),min(student),max(gap)))