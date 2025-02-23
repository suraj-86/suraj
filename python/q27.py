#waf to print elements of a list

def prlist(list):
    for item in list:
        print(item,end=" ")

names=["hi","i","am","suraj","kumar"]

print(prlist(names))