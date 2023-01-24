time_now = input().split()
time_ing = int(input())

# 14 * 60 + 30 # 870
# 870 // 60 = 14 # 몫
# 870 - (870 // 60 * 60) = 30 # 나머지

time_now_min = int(time_now[0]) * 60 + int(time_now[1]) # 14 * 60 + 30 = 870
time_end_min = time_now_min + time_ing
time_end = []
if time_end_min // 60 <24:
    time_end.append(time_end_min // 60)
    time_end.append(time_end_min - (time_end[0] * 60))
else:
    time_end.append((time_end_min - 1440)//60) # 24 * 60 = 1440
    time_end.append(time_end_min - 1440 - (time_end[0] * 60))

print(*time_end)