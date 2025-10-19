def save_employees():
    f = open("employees.dat", "ab")
    while True:
        eid = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        post = input("Enter Post: ")
        salary = input("Enter Salary: ")
        record = eid + "," + name + "," + post + "," + salary + "\n"
        f.write(record.encode())
        
        more = input("Add more? (yes/no): ")
        if more.lower() != "yes":
            break
    f.close()
    print("✅ Employee data saved in binary file: employees.dat")
