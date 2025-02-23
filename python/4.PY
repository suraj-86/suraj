#string

a="my name is suraj"
b=' i am 20 years old'
c=''' i am studying python'''
d="this is a string.\nwe are creating it in python\n"
#print(d,a+b+c)
final_string=a+" "+b+" "+c
print(final_string)
print(len(final_string))
print(len(d))

#ch=d[3]
print(d[3])

#slicing
print(d[5:9])

#stringfunctions

print(d.endswith("on"))
print(d.capitalize())
print(d.replace("a","b"))
print(d.find("we"))
print(d.count("python"))




