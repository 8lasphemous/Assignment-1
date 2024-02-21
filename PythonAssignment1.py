import csv
import time

class Product:
    def __init__(self, id, name, price, category):
        self.id = id
        self.name = name
        self.price = price
        self.category = category

products = []

def load_products(product_data):
    with open(product_data, newline='') as product_file:
        reader = csv.reader(product_file)
        for line in reader:
            try:
                id, name, price_str, category = line
                if price_str:
                    price = float(price_str)
                else:
                    price = 0.0
                products.append(Product(id, name.strip(), price, category))
            except ValueError:
                print(f"Invalid data in line: {line}")

def print_products():
    for product in products:
        print(f"ID: {product.id}, Name: {product.name}, Price: {product.price}, Category: {product.category}")

def add_product():
    new_product_id = input("Enter the product ID: ")
    for product in products:
        if product.id == new_product_id:
            print("Product ID already exists!")
            return
    
    new_product_name = input("Enter the product name: ")
    new_product_price = float(input("Enter the product price: "))
    new_product_category = input("Enter the product category: ")
    
    products.append(Product(new_product_id, new_product_name, new_product_price, new_product_category))
    print_products()
    print("\nNew product added successfully!")

def update_product():
    product_id = input("Enter the ID of the product to update: ")
    for product in products:
        if product.id == product_id:
            product.name = input("Enter the new product name: ")
            product.price = float(input("Enter the new product price: "))
            product.category = input("Enter the new product category: ")
            
            print_products()
            print("\nProduct updated successfully!")
            
            return
    print("Product not found!")

def delete_product():
    product_id = input("Enter the ID of the product to delete: ")
    for i, product in enumerate(products):
        if product.id == product_id:
            del products[i]
            print_products()
            print("\nProduct deleted successfully!")
            
            return
    print("Product not found!")

def search_product():
    search_key = input("Enter the key attribute to search for (id or name): ")
    search_value = input("Enter the value to search for: ")
    
    found_products = []
    
    if search_key.lower() == "id":
        found_products = [product for product in products if str(product.id) == search_value]
    elif search_key.lower() == "name":
        found_products = [product for product in products if product.name.lower() == search_value.lower()]
    
    if found_products:
        print("Search results:")
        for product in found_products:
            print(f"ID: {product.id}, Name: {product.name}, Price: {product.price}, Category: {product.category}")
    else:
        print("No products found!")

#Implementing quick sort

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2].price
    left = [product for product in arr if product.price < pivot]
    middle = [product for product in arr if product.price == pivot]
    right = [product for product in arr if product.price > pivot]
    return quick_sort(left) + middle + quick_sort(right)

load_products("product_data.txt")

start_time_best = time.time()
products_sorted_best = quick_sort(products)
end_time_best = time.time()

products_reversed = products[::-1]
start_time_worst = time.time()
products_sorted_worst = quick_sort(products_reversed)
end_time_worst = time.time()

import random
random.shuffle(products)
start_time_average = time.time()
products_sorted_average = quick_sort(products)
end_time_average = time.time()

print("\nSorted Product Data (Best Case):")
print_products()
print(f"\nExecution Time (Best Case): {end_time_best - start_time_best} seconds")

print("\nSorted Product Data (Worst Case):")
for product in products_sorted_worst:
    print(f"ID: {product.id}, Name: {product.name}, Price: {product.price}, Category: {product.category}")
print(f"\nExecution Time (Worst Case): {end_time_worst - start_time_worst} seconds")

print("\nSorted Product Data (Average Case):")
for product in products_sorted_average:
    print(f"ID: {product.id}, Name: {product.name}, Price: {product.price}, Category: {product.category}")
print(f"\nExecution Time (Average Case): {end_time_average - start_time_average} seconds")

while True:
    print("\nData Manipulation Operations:")
    print("1. Add a new product")
    print("2. Update an existing product")
    print("3. Delete a product")
    print("4. Search for a product")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == "1":
        add_product()
    elif choice == "2":
        update_product()
    elif choice == "3":
        delete_product()
    elif choice == "4":
        search_product()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice, try again.")

