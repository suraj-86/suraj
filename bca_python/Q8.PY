f = open("myfile.info", "r")
while True:
    ch = f.read(1)
    if not ch or ch == 'O':
        break
    print(ch, end="")
f.close()
