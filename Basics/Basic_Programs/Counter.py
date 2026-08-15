#Countdown timer Program-

#1. 3s timer = 
import time

time.sleep(3)
print("TIME'S UP!")

#output - after 3s of time it will print TIME'S UP!


#2. Execute to input timer =
my_time = int(input("Enter the time in seconds: "))

for x in range(0, my_time):
    time.sleep(1)
print("TIME'S UP!")

#output - Enter the time in seconds: 3 after 3s it will print


#3. Execute in a range we have given
my_time = int(input("Enter the time in seconds: "))

for x in range(0, my_time):
    print(x)
    time.sleep(1)
print("TIME'S UP!")

#output - 0 1 2 TIME'S UP!


#4. Execute in reverse order (-1) =
my_time = int(input("Enter the time in seconds: "))

for x in range(my_time, 0, -1):
    time.sleep(1)
print("TIME'S UP!")

#output - 3 2 1  TIME'S UP!


#5. Execute per sec, min, hour timer =
my_time = int(input("Enter the time in seconds: "))

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int (x / 3600) % 24 # 24 for days

    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("TIME'S UP!")

#output - Enter the time in seconds: 11- now each sec it will execute till from 11 to 01 then times up
