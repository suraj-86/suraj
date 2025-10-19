#TO CREATE FUNCTION

def add_employee():
    f = open("emp.dat", "ab")
    empno = input("Enter Emp No: ")
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    salary = input("Enter Salary: ")
    record = empno + "," + name + "," + dept + "," + salary + "\n"
    f.write(record.encode())
    f.close()
    print("✅ Employee added.")

def modify_employee():
    empno = input("Enter Emp No to modify: ")
    f = open("emp.dat", "rb")
    lines = f.readlines()
    f.close()

    f = open("emp.dat", "wb")
    for line in lines:
        decoded = line.decode()
        if decoded.startswith(empno + ","):
            name = input("New Name: ")
            dept = input("New Department: ")
            salary = input("New Salary: ")
            new_record = empno + "," + name + "," + dept + "," + salary + "\n"
            f.write(new_record.encode())
        else:
            f.write(line)
    f.close()
    print("✅ Record modified.")

def delete_employee():
    empno = input("Enter Emp No to delete: ")
    f = open("emp.dat", "rb")
    lines = f.readlines()
    f.close()

    f = open("emp.dat", "wb")
    for line in lines:
        decoded = line.decode()
        if not decoded.startswith(empno + ","):
            f.write(line)
    f.close()
    print("✅ Record deleted.")
