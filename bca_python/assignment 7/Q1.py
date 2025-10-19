# Assignment Q1
# Calculate the salary of 5 employees (Basic: 5000, DA: 10%, HRA: 20%)

employee_names = []
basic_salary = 5000
da = basic_salary * 0.10
hra = basic_salary * 0.20
net_salary = basic_salary + da + hra

for i in range(5):
    name = input(f"Enter name of employee {i+1}: ")
    employee_names.append(name)

for i in range(5):
    print(f"Name: {employee_names[i]}, Net Salary: ₹{net_salary}")
