from ECommerceanagement import ECommerceSystem

echom = ECommerceSystem()

while True:
    print("\n=====E-COMMERCE SYTSTEM =====")
    print("1. Add Product")
    print("2. Display products")
    print("3. Search Product")
    print("4. Add to Cart")
    print("5. View Cart")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        echom.add_product()

    elif choice == "2":
        echom.display_products()

    elif choice == "3":
        echom.search_product()

    elif choice == "4":
        echom.add_to_cart()

    elif choice == "5":
        echom.view_product()

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")


    