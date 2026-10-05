"""
CP1404/CP5632 - Practical
Calculator for a small shop
"""

price = 0

number_of_items = int(input("Number of items: "))

while number_of_items < 0:
    print("Invalid number of items")
    number_of_items = int(input("Number of items: "))
    
for item in range(number_of_items):
   price = price + float(input(f"Price of item {item + 1}: "))

if price > 100:
    total_price = price - (price * 0.1)
else:
    total_price = price

print(f"${total_price:.2f}")

