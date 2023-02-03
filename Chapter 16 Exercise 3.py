# To count how many times a class is called.
class Laptop:
    count_instance=0
    def __init__(self,brand_name,model_name,price):
        self.brand_name=brand_name
        self.model_name=model_name
        self.price=int(price)
        self.laptop_name=brand_name+""+model_name
        Laptop.count_instance+=1

L1 = Laptop('Dell','i5 5th generation','50000')
L2 = Laptop('HP','i7 7th generation','150000')

print(Laptop.count_instance)
