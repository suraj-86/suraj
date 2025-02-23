#print no 1to100

for i in range(1,101,1):
    print(i)

#print from 100 to 1

for i in range(100,0,-1):
    print(i)

#print table of n 

n=int(input("enter no to find table "))
for i in range(1,11,1):
    print(n,'x',i,'=',i*n)
