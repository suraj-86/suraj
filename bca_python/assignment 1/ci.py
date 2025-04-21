def ci(a,b,c,d):
    amount=(a*(1+b/c)**(c*d))
    #interest=amount-a
    print("Final Amount is ",round(amount,2))
    print("compound interest calculated = ",round(amount-a,2))

principle=float(input("Enter the principal amount "))
rate=float(input("Enter rate of interest "))
time=float(input("Enter time in years "))
period=float(input("Enter no of times interest applied per time period "))
rate=rate/100
ci(principle,rate,period,time)
