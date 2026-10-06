"""
CP1404/CP5632 - Practical
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

SALES_THRESHOLD = 1000
TIER_1_BONUS = 0.1
TIER_2_BONUS = 0.15

sales = float(input("Enter sales: $"))

if sales < SALES_THRESHOLD:
    bonus = TIER_1_BONUS * sales
else:
    bonus = TIER_2_BONUS * sales

print(f"This is your bonus ${bonus:2f}")

