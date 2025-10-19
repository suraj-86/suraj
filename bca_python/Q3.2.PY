def store_students():
    f = open("students.dat", "ab")
    while True:
        roll = input("Enter Roll No: ")
        name = input("Enter Name: ")
        course = input("Enter Course: ")
        record = roll + "," + name + "," + course + "\n"
        f.write(record.encode())
        
        more = input("Add more? (yes/no): ")
        if more.lower() != "yes":
            break
    f.close()
    print("✅ Student data stored in binary file.")

def read_students():
    f = open("students.dat", "rb")
    print("📄 Student Records:")
    for line in f:
        print(line.decode().strip())
    f.close()

# Example usage
# store_students()
# read_students()
