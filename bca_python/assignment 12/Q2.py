def celtof(a):
    fahr=((a*9/5)+32)
    return fahr
degree=float(input("Enter degree in celcius "))
fahr=celtof(degree)
print("degree in fahrenheit is ",f"{fahr:.2f}")