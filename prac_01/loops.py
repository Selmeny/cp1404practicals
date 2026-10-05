"""
CP1404/CP5632 - Practical
Four types of loops
"""

# 1. count in 10s from 0 to 100: 0 10 20 30 40 50 60 70 80 90 100
for i in range(0, 100, 10):
    print(i, end=" ")

# 2. count down from 20 to 1: 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1
for i in range(20, 0, -1):
    print(i, end=" ")

# 3. print number of stars.
number_of_stars = int(input("Enter number of stars: "))

for star in range(number_of_stars):
    print("*", end="")

# 4. print lines of increasing stars.
starting_star = 1
number_of_lines = int(input("Enter number of lines: "))

for line in range(number_of_lines):
    for star in range(starting_star):
        print("*", end="")
    print()
    starting_star = starting_star + 1

