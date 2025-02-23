class Person:
    name="anonymous"

    # def changename(self,name):
    #     Person.name=name
        #self.__class__.name="Suraj kumar"
    
    @classmethod
    def changename(cls,name):
        cls.name=name


p1=Person()
print(p1.name)
p1.changename("suraj kumar")
print(p1.name)
print(Person.name)
