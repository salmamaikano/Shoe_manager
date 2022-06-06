# creating a class Shoe
class Shoe():
    
    # constructor that allows us to set the properties of the shoe
    # as instance variables
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        
    # method for returning the product
    def get_product(self):
        return self.product
        
    # method for returning the cost
    def get_cost(self):
        return self.cost 
    
    # method for returning the quantity as an integer
    def get_quantity(self):
        return int(self.quantity)
    
    # method with a parameter for setting new quantity
    def set_quantity(self, number):
        self.quantity = number 
           
    # string method for controlling the appearances of the class objects
    def __str__(self):
        return f"Country: {self.country}\nCode: {self.code}\nProduct: {self.product}\nCost: {str(self.cost)}"\
               f"\nQuantity: {str(self.quantity)}"
