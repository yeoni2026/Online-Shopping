class Product:

    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def display_info(self):
        print(f"ID: {self.product_id} | Name: {self.name} | Price: ${self.price:.2f}")

    def update_price(self, new_price):
        if new_price >= 0:
            self.price = new_price
        else:
            print("Error: Price cannot be negative.")

    def get_product_data(self):
        return {
            "product_id": self.product_id,
            "name": self.name,
            "price": self.price,
        }


class ProductManager:

    def __init__(self):
        self.products = {}

    def add_product(self, product):
        if product.product_id not in self.products:
            self.products[product.product_id] = product
        else:
            print(f"Error: Product ID {product.product_id} already exists.")

    def remove_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
        else:
            print(f"Error: Product ID {product_id} not found.")

    def find_product(self, product_id):
        return self.products.get(product_id, None)

    def list_products(self):
        if not self.products:
            print("No products available.")
            return
        for product in self.products.values():
            product.display_info()

    def get_product_count(self):
        return len(self.products)
