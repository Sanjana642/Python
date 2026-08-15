#1. To calculate the circumference of the circle -

import math

radius = float(input("Enter the radius of circle :"))
circumference = 2 * math.pi * radius

print("The circumference is : {circumference}")

#output = Enter the radius of circle : 10.5
# The circumference is : 65.973...

#print("The circumference is : {round(circumference, 2)}cm")
#output = 65.97cm


#2. To calculate the Area of the circle -

import math

radius = float(input("Enter the radius of the circle: "))

area = math.pi * pow(radius, 2)

print(f"The area of the circle is {area}cm")
print(f"The area of the circle is {round(area, 2)}cm^2")

#3. To calculate the hypotenous of the circle - 

import math

a = float("Enter side A :")
b = float("Enter side B :")

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"Side c is : {c}")

#output = enter side a : 3
# enter side b : 4
# side c = 5.0