#polimorphism

# print(1+2)   #sum
# print("bbau"+" amethi")    #concatinate
# print([1,2,3]+[4,5,6])    #merge


class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    
    def showno(self):
        print(self.real,"i + ",self.img,"j")
    
    def __add__(self,num2):
        newreal=self.real + num2.real
        newimg=self.img + num2.img
        return Complex(newreal,newimg)
    
    def __sub__(self,num2):
        newreal=self.real - num2.real
        newimg=self.img - num2.img
        return Complex(newreal,newimg)
    


num1=Complex(1,3)
num1.showno()

num2=Complex(2,5)
num2.showno()

#a.__add__(b)    #dunder function

num3=num1+num2
num3.showno()

num4=num1-num2
num4.showno()

