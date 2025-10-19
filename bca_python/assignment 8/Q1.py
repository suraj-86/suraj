# Assignment 08

branches = ["CS", "Electronics", "IT", "BCA", "MCA"]
print("Available branches:", branches)

branch = input("Enter your branch: ")
if branch not in branches:
    print("Invalid")
else:
    num_stu = 60
    num_sub = 5

    names = [""] * num_stu
    totals = [0] * num_stu
    percentages = [0] * num_stu
    grades = [""] * num_stu
    honors_of = [False] * num_stu

    for i in range(num_stu):
        print(f"\nEnter student {i+1}'s details")
        names[i] = input("Name: ")
        total = 0
        honors = False

        for subject in range(num_sub):
            marks = float(input(f"Enter marks in Subject {subject + 1}: "))
            if marks > 75:
                honors = True
            total += marks

        percent = total / num_sub

        if percent >= 65:
            grade = "A"
        elif percent >= 50:
            grade = "B"
        elif percent >= 40:
            grade = "C"
        elif percent >= 30:
            grade = "D"
        else:
            grade = "Fail"

        totals[i] = total
        percentages[i] = percent
        grades[i] = grade
        honors_of[i] = honors

    for i in range(num_stu):
        print("\nName:", names[i])
        print("Branch:", branch)
        print("Total:", totals[i])
        print("Percentage:", percentages[i])
        print("Grade:", grades[i])
        print("Honors:", "Yes" if honors_of[i] else "No")
