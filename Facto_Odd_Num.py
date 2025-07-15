# Q1) WAP to accept a number from the user and find out the factorial

num = int(input("Enter a non-negative integer: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    factorial = 1
    i = 1
    while i <= num:
        factorial *= i  # Equivalent to factorial = factorial * i
        i += 1          # Equivalent to i = i + 1
    print(f"The factorial of {num} is {factorial}")


print("--------------------------------------------------------------")


#Q2) WAP to accept a min and max number from the user and display all the odd numbers
    
    # Accept min and max from user
min_num = int(input("Enter the minimum number: "))
max_num = int(input("Enter the maximum number: "))

# Initialize i with min_num
i = min_num

# Loop using while
print("Odd numbers between", min_num, "and", max_num, "are:")
while i <= max_num:
    if i % 2 != 0:
        print(i)
    i += 1

