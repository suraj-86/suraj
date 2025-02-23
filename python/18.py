#palindrome no find

def palindrome(a):
    for i in range(1,a,1):
        original=i
        rev=0
        while i!=0:
            b=i%10
            rev=rev*10+b
            i//=10
        if rev==original:
            print (rev," is a palindrome no ")
        
a=int(input("enter no to which we have to find palindrome : "))
palindrome(a)
