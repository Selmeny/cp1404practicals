"""
CP1404/CP5632 - Practical
A program to determine the result of a score and print as many stars as the score is.
"""

MENU = """(G)et a valid score (must be 0-100 inclusive)
(P)rint the result
(S)how the stars
(Q)uit"""

def main():
    score = None
    choice = get_choice()

    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            if score is None:
                print("Get a valid score first")
            else:
                result = calculate_result(score)
                print(f"Your grade: {result}")
        elif choice == "S":
            if score is None:
                print("Get a valid score first")
            else:
                print_stars(score)
        else:
            print("Invalid options")
        choice = get_choice()

    print("Thank you")

def get_valid_score():
    """
    Get a valid score from user

    :return: Int value based on user input
    """
    score = int(input("Enter your score: "))

    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter your score: "))

    return score

def calculate_result(score):
    """
    Calculate the result based on user score.

    :param score: Int value
    :return: String value
    """
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def print_stars(score):
    """
    Print as many stars as user score

    :param score: Int value
    :return: None
    """
    print("*" * score)

def get_choice():
    """
    Get a choice from menu

    :return: String value contain user choice
    """
    print(MENU)
    return input(">>> ").upper()

main()




