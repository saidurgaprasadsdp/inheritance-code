class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def display_product_details(self):
        print("Product: {}".format(self.name))
        print("Price: {}".format(self.price))
        

class ElectronicItem(Product):
    pass
class GroceryItem(Product):
    pass
s = ElectronicItem("fan",30,)
s.display_product_details()

e = GroceryItem("milk", 25)
e.display_product_details()