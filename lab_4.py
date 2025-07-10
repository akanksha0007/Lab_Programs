
# 1. Check Leap Year
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")


print("--------------------------------\n")

#2. Find the Largest Among Three Numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

largest = max(a, b, c)
print("The largest number is:", largest)


print("--------------------------------\n")

#3. Check if Number is Positive, Negative, or Zero
num = float(input("Enter a number: "))
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")


print("--------------------------------\n")

#4. Toy Vendor Discount Calculator
product_code = int(input("Enter product code (1-Battery, 2-Key, 3-Electrical): "))
order_amount = float(input("Enter order amount: "))

if product_code == 1 and order_amount > 1000:
    discount = 0.10
elif product_code == 2 and order_amount > 100:
    discount = 0.05
elif product_code == 3 and order_amount > 500:
    discount = 0.10
else:
    discount = 0.0

net_amount = order_amount - (order_amount * discount)
print("Net amount to be paid: Rs.", round(net_amount, 2))


print("--------------------------------\n")

#5. Transport Company Fare Calculator
distance = float(input("Enter distance in Km: "))

if distance <= 50:
    rate = 8
elif distance <= 100:
    rate = 10
else:
    rate = 12

fare = distance * rate
print("Total fare: Rs.", round(fare, 2))
