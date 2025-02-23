#armstrong check

def length(a):
    count=0
    while(a!=0):
        b=a%10
        a//=10
        count+=1
    return count

def armstrong(a):
    original=a
    b=length(a)
    sum=0
    while a!=0:
        c=a%10
        sum+=(c**b)
        a//=10
    if (sum==original):
        print(original," is armstrong no.")
    else:
        print(original," is not armstrong no.")

a=int(input("enter no : "))
armstrong(a)

