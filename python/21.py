#oop

class Student:
    #default constructors
    def __init__(self):
        pass
    
    #parameterized constructors
    def __init__(self,fullname,marks,age):
        self.marks=marks
        self.age=age
        self.name=fullname
        # print("adding new student to database")
    

s1=Student("suraj kumar",98,20)
print(s1.name,s1.marks,s1.age)
#print(s1.name)

s2=Student("isha raj",95,18)
print(s2.name,s2.marks,s2.age)

# class Car:
#     color="blue"
#     brand="mercedes"

# car1=Car()
# print(car1.color)
