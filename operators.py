# python program to calculate area of a rectangle
lenghth = float(input("Enter the lenghth: "))
width = float(input("Enter the width: "))
area = lenghth * width
print(f"the area is: {round (area,2)}cm^2")

#a python program to calculate the circumference of a circle 
import math
radius = float(input("Enter the radius of the circle: "))
circumference = 2 * math.pi * radius
print(f"the circumference is: { round(circumference, 2)} cm")

# python program to calculate area of a circle
radius2 = float(input("Enter radius2: "))
area = math.pi * pow(radius2, 2)
print(f"the area is: {round(area,2)}cm^2")

#python program to calculate hypotenuse of a triangle
height = float(input("Enter the height of the triangle:"))
base = float(input("Enter the base of the triangle: "))
hypotenuse = math.sqrt(pow(height,2) + pow(base,2))
print(f"the hypotenuse is: {round(hypotenuse,2)}")
