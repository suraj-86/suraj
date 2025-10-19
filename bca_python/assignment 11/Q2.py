# Program to store 30 student records and print them in descending order of marks

students = {}

for i in range(30):
    print(f"\nEnter details for Student {i+1}:")
    roll_no = input("Roll No: ")
    name = input("Name: ")
    student_class = input("Class: ")
    year = input("Year: ")
    marks = float(input("Marks: "))

    students[roll_no] = {
        'Name': name,
        'Class': student_class,
        'Year': year,
        'Marks': marks
    }

sorted_students = sorted(students.items(), key=lambda x: x[1]['Marks'], reverse=True)

print("\nStudent Records in Decreasing Order of Marks:\n")
for roll_no, details in sorted_students:
    print(f"Roll No: {roll_no}, Name: {details['Name']}, Class: {details['Class']}, Year: {details['Year']}, Marks: {details['Marks']}")
