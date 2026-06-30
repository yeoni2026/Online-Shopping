from product import display_info, add_product, remove_product


while True:
    menu = int(input("1. View products 2. Add product 3. Remove product 4. Exit : "))
    
    match(menu):
        case 1:
            display_info()
        case 2:
            name = input("Enter product name : ")
            price = int(input("Enter product price : "))
            add_product(name, price)
        case 3:
            id = input("Enter prodcut id : ")
            if remove_product(id):
                print("Product removed successfully!")
        case 4:
            print("Exiting the program.")
            break
        case _:
            print("Please enter a number between 1 and 3.")
            continue