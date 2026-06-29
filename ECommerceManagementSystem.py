from ECommerce import Product

class ECommerceSystem:

    def __init__(self):
        self.products = []
        self.cart = []

    def add_product(self):
        product_id = int(input("Enter Product ID: "))
        name = input("Enter your Name: ")
        price = int(input("Enter Product Price: "))

        product = Product(product_id,name,price)
        self.products.append(product)

        print("Product added successfully!")

    def display_products(self):
        if len(self.products) == 0:
            print("No Product Found.")
        else:
            for product in self.products:
                product.display()
    
    def search_product(self):
        product_id = int(input("Enter Product ID: "))

    def add_to_cart(self):
        product_id = int(input("Enter Product ID: "))

    def view_cart(self):
        pass 