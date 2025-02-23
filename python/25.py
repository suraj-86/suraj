#multiple inheritence

class A:
    varA="welcome to class A"
class B:
    varB="welcome to class B"
class C:
    varC="welcome to class C"
class D(A,B,C):
    varD="welcome to class D"

c1=D()

print(c1.varA)
print(c1.varB)
print(c1.varC)
print(c1.varD)


