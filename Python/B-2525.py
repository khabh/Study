hour,min=map(int,input().split())
spend=int(input())


time=hour*60+min+spend
hour=time//60
min=time-hour*60

if hour>=24:
    print(hour-24,min)
else:
    print(hour,min)
