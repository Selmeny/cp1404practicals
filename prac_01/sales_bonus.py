"""
CP1404/CP5632 - Practical
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales_threshold = 1000
tier_1_bonus = 0.1
tier_2_bonus = 0.15

sales = float(input("Enter sales: $"))

if sales < sales_threshold:
    bonus = tier_1_bonus * sales
else:
    bonus = tier_2_bonus * sales

print(f"This is your bonus ${bonus:2f}")

