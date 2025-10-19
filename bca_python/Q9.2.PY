f = open("sample.txt", "r")
count = 0

print("📄 First 10 lines:")
for line in f:
    print(line.strip())
    count += 1
    if count == 10:
        break

f.close()
