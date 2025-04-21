#calculate the DA according to its wage if basic wage is more than or equal to 1 lakh then DA=30% .
#if basic is betweeen 85 thousand and 1 lakh then DA=20% 
#if basic is b/w 85 to 75thousand then DA = 10% and if basic + DA is more than 1 lakh then other allowance =10 thousand
#if less than 1 lakh then other allowance = 5 thousand


salary = int(input("enter salary : "))

if salary >= 100000:
    DA=salary*0.3
elif salary >= 85000:
    DA=salary*0.2
elif salary >= 75000:
    DA=salary*0.1
else:
    DA=0

new_salary=DA+salary
if new_salary>100000:
    allowance=10000
else :
    allowance=5000

new_salary+=allowance

print("total salary = ",new_salary)
