# Q3: Accept roll, name, marks and store in a binary file

f = open("students.dat", "ab")  # append in binary mode

while True:
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")
    
    line = roll + "," + name + "," + marks + "\n"
    f.write(line.encode())  # convert string to bytes
    
    more = input("Add more? (yes/no):")
    if more.lower() != 'yes':
        break

f.close()
print("✅ Data stored in binary file: students.dat")
