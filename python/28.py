#@property

class Students:
    def __init__(self,phy,che,math):
        self.phy=phy
        self.che=che
        self.math=math

    # def calcpercentage(self):
    #     self.percentage=str((self.phy+self.che+self.math)/3)+"%"

    @property
    def percentage(self):
        return str((self.phy+self.che+self.math)/3)+"%"
    
        

s1=Students(98,99,97)
print(s1.percentage)

s1.phy=86
print(s1.phy)
print(s1.percentage)
