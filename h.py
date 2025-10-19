gandu ={}
for i in range (3):
    name = input("naem")
    roll= int(input("roll"))
    cpp = int (input("marks of cpp"))
    py = int(input("py"))
    dm= int (input("dm"))

    gandu[roll]={
        "name ":name,
        "cpp": cpp,
        "py": py,
        "dm":dm
    }

print(gandu)