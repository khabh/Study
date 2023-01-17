x, y = map(int, input().split())
dates = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
dateCount = y
for i in range(1, x):
    dateCount += dates[i]
print(day[int(dateCount % 7)])
