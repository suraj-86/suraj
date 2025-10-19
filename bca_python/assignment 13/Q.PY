def total(marks):
    return sum(marks.values())

def percentage(total_marks, max_marks):
    return (total_marks / max_marks) * 100

def grade(percentage):
    if percentage >= 75:
        return 'A'
    elif 60 <= percentage < 75:
        return 'B'
    elif 50 <= percentage < 60:
        return 'C'
    elif 40 <= percentage < 50:
        return 'D'
    else:
        return 'F'

students = []
num = 60
subjects = ['Python', 'DM', 'Office', 'OOPS']
max=400

for i in range(1, num + 1):
    print(f"\nEnter marks for Student {i}:")
    marks = {}
    for subject in subjects:
        mark = float(input(f"  {subject}: "))
        marks[subject] = mark
    
    total = total(marks)
    percentage = percentage(total, max)
    grade = grade(percentage)
    
    students.append({
        'Student_ID': i,
        'Marks': marks,
        'Total': total,
        'Percentage': percentage,
        'Grade': grade
    })

print("\n--- Marksheet ---")
for student in students:
    print(f"\nStudent {student['Student_ID']}")
    for subject, mark in student['Marks'].items():
        print(f"  {subject}: {mark}")
    print(f"  Total Marks: {student['Total']} / {max}")
    print(f"  Percentage: {student['Percentage']:.2f}%")
    print(f"  Grade: {student['Grade']}")
