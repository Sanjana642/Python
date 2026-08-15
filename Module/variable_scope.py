# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) - Local -> Enclosed -> Global -> Built-in

# 1. Local scope -
 
# def func1():
#     a = 1
#     print(a)

# def func2():
#     b = 2
#     print(a)   

# func1()
# func2()
# output - print(a) - NameError: name 'a' is not defined

def local1():
    x = 1
    print(x)

def local2():
    x = 2
    print(x)   

local1()
local2()
# output = 1 2

# 2. Enclosed scope- (not used much it is complex)
def enclose1():
    x = 1

    def enclose2():
        print(x)
    enclose2()

enclose1()
#output - 1

# 3. Global scope-
def global1():
    print(x)

def global2():
    print(x)

x = 3

global1()
global2()
# output - 3 3

# 4. Built-in scope-
from math import e
    # print(e)  - 2.72...


def builtin1():
    print(e)

e = 3
builtin1()
#output - 3 according to LEGB version

