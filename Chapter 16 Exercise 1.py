# Create a laptop class
class Laptop:
    def __init__(self,brand_name,model_name,price):
        self.brand_name=brand_name
        self.model_name=model_name
        self.price=price
        self.laptop_name=brand_name+""+model_name

l1= Laptop('Dell','i5 5th generation','50000')
l2= Laptop('HP','i7 7th generation','150000')
print(l1.model_name)
print(l2.price)
print(l1.laptop_name)