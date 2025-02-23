#find armstrong nos

def length(a):
    count=0
    while(a!=0):
        b=a%10
        a//=10
        count+=1
    return count

def armstrong(a):
    for i in range(1,a,1):
        b=length(i)
        sum=0
        original=i
        while i!=0:
            c=i%10
            sum+=(c**b)
            i//=10
        if (sum==original):
            print(original," is armstrong no.")
            #else:
                #print(original," is not armstrong no.")
    
a=int(input("enter no to which ARMSTRONG SHOULD BE PRINTED : "))
armstrong(a)

