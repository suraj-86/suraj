#wap to find sum of first n nos

# n=int(input("enter no to which sum is required : "))
# sum=0
# for i in range(n+1):
#     sum+=i
# print(sum)

#using while

n=int(input("enter no to which sum is required : "))
sum=0
i=1
while i<=n:
    sum=(sum+i)
    i+=1

print(sum)