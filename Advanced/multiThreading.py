# multi-threading = Used to perform multiple tasks concurrently (multitasking) 
#       Good for I/O bound tasks like reading files or fetching data from APIs
#       Not good for CPU bound tasks like heavy calculations (use multiprocessing instead)
#       Thread(target = my_function)

import threading
import time

def walk_dog(first, last):
    time.sleep(8)
    print(f"You finish walking the {first} {last}")

def take_out_trash():
    time.sleep(3)
    print("You take out the trash")

def get_mail():
    time.sleep(5)
    print("You get the mail")


chore1 = threading.Thread(target=walk_dog, args=("Scooby", "Doo"))   
# args is used to pass arguments to the target function also we use 
# tuple to pass multiple arguments use , to know it is a tuple
chore1.start()

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()

chore1.join()
chore2.join()
chore3.join()
print("All chores have complete!")

# output - (with order of time.sleep)
# You take out the trash  - 3 secs
# You get the mail        - 5 secs
# You finish walking the dog    - 8 secs

# You finish walking the Scooby Doo 
# All chores have complete! 