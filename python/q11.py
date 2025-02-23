#wap to check if a list contains a palindrome of elements.

a=[1,2,3,2,1]
b=[1,"abc","abc"]
c=a.copy()
c.reverse()
d=b.copy()
d.reverse()

if(a==c):
    print(a," is palindrome")
else:
    print(a," is not palindrome")

if(b==d):
    print(b," is palindrome")
else:
    print(b," is not palindrome")