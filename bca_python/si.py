def si(a,b,c):
    interest=(a*b*c)/100
    print("interest is ",interest)
principle=int(input("Enter the principal amount "))
rate=float(input("Enter rate of interest "))
time=int(input("Enter time in years "))
si(principle,rate,time)
