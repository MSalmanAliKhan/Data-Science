# In the laptop class, give an option to reduce the price by a specific percentage.
class Laptop:
    def __init__(self,brand_name,model_name,price):
        self.brand_name=brand_name
        self.model_name=model_name
        self.price=int(price)
        self.laptop_name=brand_name+""+model_name
    def apply_discount(self,percentage):
        return (self.price-self.price*int(percentage)/100)


l1= Laptop('Dell','i5 5th generation','50000')
print(l1.apply_discount(40))
print(Laptop.apply_discount(l1,60))

