employees = {}

for i in range(5):
    print(f"\nEnter details for employee {i+1}:")
    code = input("Employee Code: ")
    name = input("Name: ")
    dept = input("Department: ")
    salary = float(input("Salary: "))
    
    employees[code] = {
        'Name': name,
        'Department': dept,
        'Salary': salary
    }

print("\nEmployees with salary greater than 10,000 and less than 20,000:\n")
for code, details in employees.items():
    if 10000 < details['Salary'] < 20000:
        print(f"Code: {code}, Name: {details['Name']}, Dept: {details['Department']}, Salary: {details['Salary']}")
