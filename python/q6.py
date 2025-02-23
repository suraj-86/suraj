#grade based on marks

marks=int(input("enter your marks"))
grade=str()
if(marks>=90):
    grade="a"
elif(marks>=80 and marks<90):
    grade="b"
elif(marks>=70 and marks<80):
    grade="c"
else:
    grade="d"
print("your grade is : ",grade)