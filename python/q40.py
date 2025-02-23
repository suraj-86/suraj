#create a class called order which stores item and its price 
#use dunder function __gt__() to convey that :
#order1>order2 if price order1>price of order2

class Order:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    
    def __gt__(self,price2):
        return self.price>price2.price



order1=Order("chips",10)
order2=Order("kurkure",20)

print(order1<order2)
