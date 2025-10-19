def salary(basic, hra, other):
    if basic > 10000 and basic <20000:
        total_salary = basic + hra + other
    else:
        total_salary = basic
    return total_salary

basic_salary = int(input("Enter Basic Salary: "))
hra = int(input("Enter HRA: "))
other= int(input("Enter Other Allowances: "))

final_salary = salary(basic_salary, hra, other)
print(f"Final Calculated Salary: {final_salary}")
