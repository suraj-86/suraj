#dictionary

info={
    "name":"suraj",
    "course":"bca",
    "sem":"1st",
    "subjects":["python","c","cpp"],
    "elective subjects":("english","evs","understanding bharat"),
    "marks":{
        "python":70,
        "c":54,
        "cpp":98
        },
    "age":20,
    "is_adult":True
}

print(type(info))
print(info)
print(info["name"])

#info["age"]=int(input("enter your age : "))
print(list(info.keys()))
print(len(info))


#methods
myinfo={"age":21}

info.keys()
info.values()
info.items()
info.get("keys")
info.update(myinfo)
info.update({"city":"begusarai"})

print(info)
