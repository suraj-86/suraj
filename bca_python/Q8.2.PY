search_name = input("Enter name to search: ")

f = open("names.txt", "r")
found = False

for line in f:
    if search_name.lower() == line.strip().lower():
        found = True
        break

f.close()

if found:
    print("✅ Name found in file.")
else:
    print("❌ Name not found.")
