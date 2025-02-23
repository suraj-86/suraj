#warf to print all elements in list 

name=["suraj","kumar","is","my","name"]

def plist(list,x=0):
    if x ==len(list):
        return 0
    else:
        print(list[x] , end=" ")
        plist(list,x+1)
    
plist(name)

