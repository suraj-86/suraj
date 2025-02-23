
# f=open("some2.txt","a")
# data=str(f.write(" i am adding some new lines in it. "))
# f.close()


f=open("some2.txt","r")
print(f.read())
print(type(f.read()))
f.close()

f=open("some2.txt","r")
print(f.readline(2))
#print(f.readline())
#print(f.readline())
f.close()

import os
#pip install tensorflow
os.remove("some2.txt")
