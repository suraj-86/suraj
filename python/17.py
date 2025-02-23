#palindrome check

def palindrome(a):
    original=a
    c=0
    while a!=0:
        b=a%10
        c=c*10+b
        a=a//10
    if c==original:
        print (original," is a palindrome no ")
    else:
        print (original," is not a palindrome no ")

a=int(input("enter no to check : "))
palindrome(a)

