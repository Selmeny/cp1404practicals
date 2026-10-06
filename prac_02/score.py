"""
CP1404/CP5632 - Practical
Program to determine score status
"""

import random

def main():
    user_score = float(input("Enter user_score: "))
    user_grade = calculate_grade(user_score)
    print_result(True, user_score, user_grade)

    random_score = random.uniform(0.0, 100.0)
    random_grade = calculate_grade(random_score)
    print_result(False, random_score, random_grade)

def calculate_grade(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def print_result(is_user: bool, score, grade):
    if is_user:
        print(f"User score {score:.2f} is {grade}")

        if grade  == "Excellent":
            print("You get a prize!")
    else:
        print(f"Random: {score:.2f} = {grade}")

main()
