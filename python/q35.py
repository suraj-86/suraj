#from a file containing nos separated by comma, print the count of even nos.



# with open("nos.txt","w") as f :
#     int(f.write("1,2,3,4,5,6,7,8,9,10"))

count=0
with open("nos.txt","r") as f :
    data=f.read()
    nums=data.split(",")
    for i in nums:
        if (int(i)%2==0):
            count+=1
        
print(count)
