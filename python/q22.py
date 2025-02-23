#search of x in tuple using for 

tup=(1,4,9,16,25,36,49,64,81,100)
x=int(input("enter element to search "))
for i in tup:
    if(i==x):
        print("found")
        break
    else:
        print("searching")