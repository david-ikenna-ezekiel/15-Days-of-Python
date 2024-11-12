# Taking a dictionary of items and their prices as input from the user
items_input = input("Enter items and prices (item:price) separated by commas: ")
items_list = items_input.split(',')

# Create the dictionary of items and prices
item_prices = {item.split(':')[0].strip(): float(item.split(':')[1].strip()) for item in items_list}

# Getting an item name from the user and printing its price
item_name = input("Enter item name to get its price: ").strip()
price = item_prices.get(item_name, "Item not found")
print("Price:", price)
