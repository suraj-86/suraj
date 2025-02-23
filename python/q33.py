#create a new file "praxctice.txt" using py using given data 
#waf that replaces all occurences of "java" with "python" in the file
#search if "learning" exists in file

with open("Practice.txt","w") as f :
    f.write(" Hi everyone \n we are learning file I/O \n using Java.\n I like programming in Java")
          
with open("Practice.txt","r") as f:
    data=f.read()

new_data=data.replace("Java","Python")
print(new_data)


#search if learning exists in file

with open("Practice.txt","r") as f:
    data=f.read()
    if(data.find("learning")!=-1):
        print("found")
    else:
        print("not found")
