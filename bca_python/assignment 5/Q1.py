#wap to calculate compound interest if interest are -
#5% if (5%<interest <10%)
#10% if (10%<interest <15%)

p=int(input("enter principle : "))
r=int(input("enter rate : "))
t=int(input("enter time : "))

if(r>=5) and (r<=10):
    a=p*(1+5/100)**t
elif(r>=10) and (r<=15):
    a=p*(1+10/100)**t
else:
    print("out of range")

print("interest is : ",a-p)

