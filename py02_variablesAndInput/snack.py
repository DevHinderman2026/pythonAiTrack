# Name: Russell Hinderman
# Date: November 19, 2026
# Program: snack.py
# Description: Takes a snack bar order and prints a receipt with tax.

TAX_RATE = 0.07

# Input
customer = input("Customer name: ")
item = input("Item: ")
price = float(input("Price: "))
quantity = int(input("Quantity: "))

# Processing
subtotal = price * quantity
tax = subtotal * TAX_RATE
total = subtotal + tax

# Output
print()
print(f"Receipt for {customer}")
print(f"Item: {item}")
print(f"Quantity: {quantity}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")
