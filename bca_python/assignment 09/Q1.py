# Assignment 9

# Q: WAP to create a dictionary of 5 employees through input & print all keys, items, post,
# and remove all the items from dictionary 2 & 5 and find length of dictionary 1 and 4.

emp1 = {}
emp2 = {}
emp3 = {}
emp4 = {}
emp5 = {}

for i in range(1, 6):
    name = input("Enter name: ")
    salary = int(input("Salary: "))
    post = input("Post: ")
    
    emp = {
        "name": name,
        "salary": salary,
        "post": post
    }
    
    if i == 1:
        emp1 = emp
    elif i == 2:
        emp2 = emp
    elif i == 3:
        emp3 = emp
    elif i == 4:
        emp4 = emp
    elif i == 5:
        emp5 = emp

print(emp1.keys())
print(emp2.keys())
print(emp3.keys())
print(emp4.keys())
print(emp5.keys())

print(emp1.items())
print(emp2.items())
print(emp3.items())
print(emp4.items())
print(emp5.items())

print(emp1.get("post"))
print(emp2.get("post"))
print(emp3.get("post"))
print(emp4.get("post"))
print(emp5.get("post"))

emp2.clear()
emp5.clear()

print(len(emp1))
print(len(emp4))
