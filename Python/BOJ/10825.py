import sys

n = int(input())
students = list(sys.stdin.readline().split() for _ in range(n))
for student in sorted(students, key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0])):
    print(student[0])
