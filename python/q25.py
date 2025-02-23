#factorial


n=int(input("enter no to which sum is required : "))
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)
