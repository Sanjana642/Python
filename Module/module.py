# module = a file containing code you want to include in your program 
# use 'import' to include a module (built-in your own)
# useful to breakup a large program reusable separate files
# files- example.py and main.py

# print(help("modules")) - list will print of modules in terrminal

# import math
# print(math.pi)

# import math as m
# print(m.pi)

from math import e

a,b,c,d,e = 1,2,3,4,5

print(e ** a)
print(e ** b)
print(e ** c)
print(e ** d)
print(e ** e)
#output - 2.718281828459045
# 7.3890560989306495
# 20.085536923187664
# 54.59815003314423

# now when we add e then the output will - 
# 5
# 25
# 125
# 625

# now we need to import math first then -
import math

a,b,c,d,e = 1,2,3,4,5

print(math.e ** a)
print(math.e ** b)
print(math.e ** c)
print(math.e ** d)
print(math.e ** e)
# outpt+ut = 2.718281828459045
# 7.3890560989306495
# 20.085536923187664
# 54.59815003314423