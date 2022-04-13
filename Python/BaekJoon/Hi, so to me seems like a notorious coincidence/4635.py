# Bill and Ted are taking a road trip.
# But the odometer in their car is broken, so they don't know how many miles they have driven.
# Fortunately, Bill has a working stopwatch, so they can record their speed and the total time they have driven. Unfortunately, their record keeping strategy is a little odd,
# so they need help computing the total distance driven.
# You are to write a program to do this computation.

while True:
    case = int(input())
    if case == -1:
        break

    result = 0
    calTime = 0
    for i in range(case):
        mile, time = map(int, input().split())

        if i != 0:
            result += mile*(time-calTime)
        else:
            result += mile*time

        calTime = time

    print(result, "miles")
