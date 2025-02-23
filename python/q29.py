#waf to convert usd to inr

def usdtoinr(a):
    inr=83*a
    return inr

usd=int(input("enter usd amount : "))
print("amount in inr : ",usdtoinr(usd))