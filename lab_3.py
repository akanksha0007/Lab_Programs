# 1. Take one number and check if it is even or odd using ternary operator

num = 5

result = "Even" if num % 2 == 0 else "Odd"   # Ternary operator
print("The number is", result)

print("\n")

#2.Take two numbers and swap them
a = 12
b = 15

a, b = b, a     # Swapping

print("After swapping:")
print("First number a  =", a)
print("Second number b =", b)

print("\n")

#3. Convert Kilometers to Miles

km = 10.0

miles = km * 0.621371      # 1 kilometer = 0.621371 miles

print("Distance in miles:", miles)

print("\n")

# 4. Find Simple Interest on Rs. 200 for 5 years at 5% per year

P = 200  # Principal
T = 5    # Time in years
R = 5    # Rate per annum

SI = (P * T * R) / 100   # Formula

print("Simple Interest is:", SI)


