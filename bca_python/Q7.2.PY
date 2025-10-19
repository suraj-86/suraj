f = open("names.txt", "w")

while True:
    name = input("Enter student name: ")
    f.write(name + "\n")
    
    more = input("Add more? (yes/no): ")
    if more.lower() != 'yes':
        break

f.close()
print("✅ Student names saved to names.txt")
