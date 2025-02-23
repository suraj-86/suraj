#search of a no in tuple using loop

t=(1,4,9,16,25,36,49,64,81,100)
i=0
y=False
x=int(input("ENTER THE NO TO SEARCH "))
while i<len(t) :
    if(t[i]==x):
        print(x,"found on ",i)
        break
    else:
        print("searching")
        y=True
    i+=1
