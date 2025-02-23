#conditional

#if

age=int(input("enter your age :"))
if(age>=18):
    print("you're eligible for voting")
    #print("you're an adult")
elif(age<0):
    print("you're not born")
else:
    print("you're not eligible for voting")


#nesting

age=int(input("enter your age :"))
if(age>=18):
    if(age>=80):
        print("marja buddhe")
    else:
        print("you're eligible for voting")
else:
    print("you're not eligible for voting")
   
    