#lists and tuples

marks = [94.4,34.5,87.5,56.7,48.6]
print(marks)
print(type(marks))

print(marks[3])
print(len(marks))

student=["karan",96.5,19,"patna"]
print(student)
print(student[0])
student[0]="suraj"
print(student)

# print(marks[1:4])


#list methods

marks.append(40)
marks.sort()
marks.sort(reverse=True)
marks.reverse()
#marks.insert()
marks.remove(34.5)
marks.pop(3)
marks.insert(3,34)
print(marks)



