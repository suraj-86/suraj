total_marks = 300

for sem in range(1, 4):
    filename = "bca_sem" + str(sem) + ".txt"
    print("\nEnter data for Semester", sem)
    
    f = open(filename, "w")
    for i in range(1, 61):
        roll = input("Enter Roll No of Student " + str(i) + ": ")
        marks = float(input("Enter Marks out of 300: "))
        percent = (marks / total_marks) * 100
        f.write(roll + "," + str(marks) + "," + "{:.2f}".format(percent) + "%\n")
    f.close()
    
    print("Semester", sem, "data saved in", filename)
