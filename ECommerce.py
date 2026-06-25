class Product:
    def __init__(self,product_id,name,price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def display(self):
        print(f"Product ID : {self.product_id}")
        print(f"Name : {self.name}")
        print(f"Price : {self.price}")
        print("-" * 30)
