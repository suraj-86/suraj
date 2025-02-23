#define an employee class with attributes role,department,and salary.this class also has the shodetails() method


class Employee:
    def __init__(self,role,department,salary):
        self.role=role
        self.department=department
        self.salary=salary
    
    def showdetails(self):
        print("role is : ",self.role)
        print("department is : ",self.department)
        print("salary is : ",self.salary)

e1=Employee("teacher","cs department",150000)
e1.showdetails()

#create an engineer class that inherits properties from employee & has additional attributes : name and age 


class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("engineer","IT","120000")

eng1=Engineer("suraj",20)
eng1.showdetails()