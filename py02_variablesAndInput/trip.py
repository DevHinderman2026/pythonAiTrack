# Name: Russell Hinderman
# Date: November 19, 2026
# Program: trip.py
# Description: Figures out gas, cost, and driving time for a road trip.

AVERAGE_SPEED = 55

# Input
destination = input("Destination: ")
distance = float(input("Trip distance in miles: "))
mpg = float(input("Car's miles per gallon: "))
gas_price = float(input("Gas price per gallon: "))
people = int(input("How many people split the cost: "))

# Processing
gallons = distance / mpg
gas_cost = gallons * gas_price
cost_per_person = gas_cost / people
total_minutes = int(distance / AVERAGE_SPEED * 60)
hours = total_minutes // 60
minutes = total_minutes % 60

# Output
print()
print(f"Road Trip to {destination}")
print(f"Gallons of gas: {gallons:.1f}")
print(f"Gas cost: ${gas_cost:.2f}")
print(f"Cost per person: ${cost_per_person:.2f}")
print(f"Driving time: {hours} hours {minutes} minutes")
