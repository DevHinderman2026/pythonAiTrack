# Name: Russell Hinderman
# Date: November 19, 2026
# Program: pizza.py
# Description: Plans how many pizzas to buy for a party and what it costs.

SLICES_PER_PIZZA = 8
PIZZA_PRICE = 12.99
EXTRA_SLICE_PRICE = 2.25

# Input
host = input("Host's name: ")
people = int(input("Number of people: "))
slices_each = int(input("Slices per person: "))

# Processing
total_slices = people * slices_each
whole_pizzas = total_slices // SLICES_PER_PIZZA
extra_slices = total_slices % SLICES_PER_PIZZA
total_cost = whole_pizzas * PIZZA_PRICE + extra_slices * EXTRA_SLICE_PRICE
cost_per_person = total_cost / people

# Output
print()
print(f"Pizza Plan for {host}'s Party")
print(f"Total slices: {total_slices}")
print(f"Whole pizzas: {whole_pizzas}")
print(f"Extra slices: {extra_slices}")
print(f"Total cost: ${total_cost:.2f}")
print(f"Cost per person: ${cost_per_person:.2f}")
