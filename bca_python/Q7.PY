# Q7: Store 10 employee records in a binary file

f = open("emp.dat", "wb")  # overwrite mode, binary

for i in range(10):
    empno = input("Enter Emp No: ")
    name = input("Enter Name: ")
    post = input("Enter Post: ")
    salary = input("Enter Salary: ")
    record = empno + "," + name + "," + post + "," + salary + "\n"
    f.write(record.encode())

f.close()
print("✅ 10 Employee records stored in binary file: emp.dat")
