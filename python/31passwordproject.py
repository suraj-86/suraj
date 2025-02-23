#random password


import random
import string

pass_len=8
value=string.punctuation+string.ascii_letters+string.digits
password=""

for i in range(pass_len):
    password+=random.choice(value)

print("Your random password is : ",password)

# password="".join([random.choice(value) for i in range(pass_len)])
# print("Your random password is : ",password)