def area_ci(a):
    area = a*a*3.14
    return area

def area_tri(a,b):
    area = 0.5*a*b
    return area

def vol_cube(a):
    volume = a*a*a
    return volume

s = int(input("Enter side of cube:"))
r = int(input("Enter radius of circle:"))
b = int(input("Enter base of triangle:"))
h = int(input("Enter height of triangle:"))

print("Area of triangle =", area_tri(b,h))
print("Area of circle =", area_ci(r))
print("Volume of cube", vol_cube(s))
