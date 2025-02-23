#rec fun to cslculate sum of first n natural no

def nsum(a):
    if a==0:
        return 0
    else:
        return a+nsum(a-1)
    
a=int(input("enter no : "))
print("sum of first ",a,"natural no is :",nsum(a))