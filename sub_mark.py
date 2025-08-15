# Program to accept marks of 5 subjects and display the total value using a while loop

total_marks = 0
subject_count = 0 

while subject_count < 5: 
    subject_count += 1 
    
    marks = float(input(f"Enter marks for Subject {subject_count}: "))
     
    total_marks += marks

print(f"Total marks for 5 subjects: {total_marks}")