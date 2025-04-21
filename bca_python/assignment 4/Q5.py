#print the table from 2 to 20 using range and determine if its even or odd.

for i in range(2,21):
    for j in range(1,11):
        if((i*j)%2==0):
            print(j,"X",i,"=",i*j,"is even")
        else:
            print(j,"X",i,"=",i*j,"is odd")
    print("\n")