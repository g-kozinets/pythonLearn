x = int(480)
h = int(1)
m = int(2)

curr_time = h*60+m
alarm_time = curr_time + x
alarm_h = alarm_time//60
print(alarm_h)
print(alarm_time - alarm_h*60)
