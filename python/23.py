#private(like) attributes

class Person:
    __name="anonymous"

    def __hello(self,name):
        print("Hello ")

    def welcome(self):
        self._Person__hello(self.__name)



p1=Person()
print(p1.welcome())
