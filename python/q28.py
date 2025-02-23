#factorial using function

def fact(a):
    i=1
    fact=1
    while i<=a:
        fact*=i
        i+=1
    return fact

print(fact(6))
