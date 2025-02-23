#create student class that takes name & marks of 3 subjects as arguments in constructor.
#then create a method to print average.


class Student:

    def __init__(self,name,marks):
        self.marks=marks
        self.name=name

    def average(self):
        sum=0
        for i in self.marks:
            sum+=i
        print("HI ",self.name,"your average marks is ",sum/len(self.marks))

s1=Student("suraj",[99,98,97])

s1.name="suraj kumar"
s1.marks=[98,99,97,98,99,97]
s1.average()