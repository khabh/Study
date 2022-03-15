hour,min=input().split()
hour=int(hour)
min=int(min)

if hour==0:
    hour=hour+24

time=hour*60+min-45
hour=time//60
min=time-hour*60
print(hour,min)
