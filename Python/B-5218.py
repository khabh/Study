case = int(input())
for _ in range(case):
    alpha1, alpha2 = map(list, input().split())
    distances = []
    for i in range(len(alpha1)):
        distances.append(ord(alpha2[i])-ord(alpha1[i]))

    print("Distances:", end=" ")
    for j in distances:
        if j < 0:
            j += 26
        print(j, end=" ")

    print()
