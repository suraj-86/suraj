class Biodata:
    def __init__(self):
        self.name= input("Enter your name: ")
        self.age = input("Enter your age: ")
        self.gender = input("Enter your gender: ")
        self.qualification = input("Enter your qualification: ")
        self.hobbies = input("Enter your hobbies : ")
        self.best_friend = input("Enter your best friends name : ")

    def display(self):
        print("\n\n\nBIODATA IS ---")
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Gender: ",self.gender)
        print("Qualification: ",self.qualification)
        print("Hobbies: ",self.hobbies)
        print("Best Friend: ",self.best_friend)


my_biodata = Biodata()
my_biodata.display()