# 1.Calculate the multiplication and sum of two numbers.

a=10
b=5 

sum_result = a + b    # Calculate sum 
product = a * b       # Calculate multiplication

print("Sum =", sum_result)
print("Multiplication =", product)

#2.Declare two variables and print which variable is largest using ternary operator

a = 10
b = 5

largest = a if a > b else b   # Ternary operator to find largest

print("Largest number is:", largest)


#3. Convert temperature in degree Centigrade to Fahrenheit

celsius = 15

fahrenheit = (celsius * 9/5) + 32  

print("Temperature in Fahrenheit:", fahrenheit)

# 4.Find the area of a triangle whose sides are given

import math

a = 15
b = 10
c = 12


s = (a + b + c) / 2  # Calculate semi-perimeter

area = math.sqrt(s * (s - a) * (s - b) * (s - c))   #  formula

print("Area of the triangle:", area)

