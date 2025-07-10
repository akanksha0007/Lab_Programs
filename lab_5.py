#WAP to accept a choice from the user and create a calculator 

def calculator():
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter choice : ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result = ", num1 + num2)
        elif choice == '2':
            print("Result = ", num1 - num2)
        elif choice == '3':
            print("Result = ", num1 * num2)
        elif choice == '4':
            if num2 != 0:
                print("Result = ", num1 / num2)
            else:
                print("Error: Division by zero!")
    else:
        print("Invalid choice")

# Call the calculator function
calculator()

print("---------------------------------\n")
#WAP to accept student name , roll no ,marks of 5 subje t and calculate percentage and grade  
def student_result():
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    
    marks = []
    total_subjects = 5

    for i in range(1, total_subjects + 1):
        mark = float(input(f"Enter marks for subject {i}: "))
        marks.append(mark)

    total = sum(marks)
    percentage = total / total_subjects

    if percentage >= 90:
        grade = 'A+'
    elif percentage >= 75:
        grade = 'A'
    elif percentage >= 60:
        grade = 'B'
    elif percentage >= 50:
        grade = 'C'
    elif percentage >= 35:
        grade = 'D'
    else:
        grade = 'F'

    print("\n--- Student Result ---")
    print("Name       :", name)
    print("Roll Number:", roll_no)
    print("Total Marks:", total)
    print("Percentage :", percentage, "%")
    print("Grade      :", grade)

# Call the result function
student_result()
