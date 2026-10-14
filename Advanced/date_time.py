# date and time -

import datetime

date = datetime.date(2026, 1, 2)  # 2026-01-02
today = datetime.date.today()

time = datetime.time(9, 30, 0)

now = datetime.datetime.now()
now = now.strftime("%H:%M:%S %d-%m-%Y") # hour-min-sec (strftime means string-format time method)

target_datetime = datetime.datetime(2020, 1, 2, 12, 30, 1)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target date has passed")
else:
    print("Target date has NOT passed")

# output -Target date has NOT passed - 2030 in target_datetime
# output -Target date has passed - 2020 in target_datetime

print(date) # 2026-01-02
print(time) # 09:30:00
print(now)  # 20:20:02 
print(now)  # 20:20:37 09 26 2026