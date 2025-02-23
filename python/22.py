#oops


class Student:
    college_name="bbau"
    name="Anonymous" #class attr    with less priority

    #default constructors
    def __init__(self):
        pass
    
    #parameterized constructors
    def __init__(self,fullname,marks,age):
        self.marks=marks
        self.age=age
        self.name=fullname     #object attr      with high priority
    
    #methods
    @staticmethod              #decorator
    def hello():
        print("welcome to bbau")
    
    def get_marks(self):
        return self.marks
    


s1=Student("suraj kumar",98,20)
s1.hello()
print(s1.name,s1.marks,s1.age,s1.college_name)

print("marks is ",s1.get_marks())