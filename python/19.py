
# f = open("some.txt","w")
# data=f.write("i am learning python on "
# "virtual studio code")
# print(data)
# print(type(data))
# f.close()

# f=open("some.txt","r")
# print(f.read())
# f.close()

# f = open("some.txt","a")
# data=str(f.write(" i am a good boy "))
# print(data)
# print(type(data))
# f.close()


# f=open("some.txt","r")
# print(f.read())
# print(type(f.read()))
# f.close()

try:
    with open("some.txt","r") as f:
        data=f.read()
        print(data)
except FileNotFoundError:
    print("khojo")