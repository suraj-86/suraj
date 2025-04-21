friends=[]

for i in range(5):
    name=input(f"Enter name of friend {i+1}: ")
    friends.append(name)

print("\nMy Friends are : ")
for friend in friends:
    print(friend)
