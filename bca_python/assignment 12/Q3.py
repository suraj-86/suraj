def family():
    print("Father's Name is : Ranjan Roy")
    print("Mother's Name is : Rima")
    print("Sister's Name is : Hani")

def friends():
    print("Friend Name is : Isha")

a = int(input("Enter 1 for family name and 2 for friend name : "))

if (a==1):
    family()
elif (a==2):
    friends()
else:
    print("Invalid")
