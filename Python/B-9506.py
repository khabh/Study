while True:
    a=int(input())
    if a == -1:
        break
    k=[]
    for i in range(1,a):
        if a%i==0:
            k.append(i)


    if sum(k)==a:
        print(a," = "," + ".join(str(i) for i in k),sep="")
    
    else:
        print(a,"is NOT perfect.")
