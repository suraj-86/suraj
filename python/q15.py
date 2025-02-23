#wap to enter marks of 3 subjects fro user and store in dict.
#start with empty dict and add one by one

marks={}

input1={
    input("enter subject "):int(input("enter marks "))
}
input2={
    input("enter subject "):int(input("enter marks "))
}
input3={
    input("enter subject "):int(input("enter marks "))
}
marks.update(input1)
marks.update(input2)
marks.update(input3)

print(marks)