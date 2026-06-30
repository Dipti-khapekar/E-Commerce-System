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

        for product in self.products:
            if self.product_id == product_id:
                print("\nProduct found.")
                product.display()
                return
            
        print("Product Not found.")

    def add_to_cart(self):
        product_id = int(input("Enter Product ID: "))

        for product in self.products:
            if self.product_id == product_id:
                self.cart.append(product)
                print("Product Added To Cart successfully!")
                return
            
        print("Product Not found.")

    def view_cart(self):
        if len(self.products) == 0:
            print("Cart is Empty.")
        else:
            total = 0

            print("\nItems in cart")
            print("-" * 30)

            for product in self.cart:
                print(f"{product.name} - ₹{product.price}")
                totla += product.price

                print("-" * 30)
                print("Total Amount: ",total)