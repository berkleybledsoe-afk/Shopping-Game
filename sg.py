item_1 = input("Enter Item 1 Name :")
price_1 = float(input("Enter the price of Item 1:"))
quantity_1 = int(input("Enter the quantity of Item 1: "))

item_2 = input("Enter Item 2 Name:")
price_2 = float(input("Enter the price of Item 2:"))
quantity_2 = int(input("Enter the quantity of Item 2: "))

total = quantity_1 * price_1 + quantity_2 * price_2
print(f"You have bought {quantity_1} {item_1} and {quantity_2} {item_2} for a total price of ${total}")
