"""
CP1404/CP5632 - Practical
Program for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""

def main():
    choice = get_choice()

    while choice != "Q":
        if choice == "C":
            convert_from_celsius()
        elif choice == "F":
            convert_from_fahrenheit()
        else:
            print("Invalid option")

        choice = get_choice()
    print("Thank you.")

def get_choice():
    print(MENU)
    choice = input(">>> ").upper()
    return choice

def convert_from_celsius():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print(f"Result: {fahrenheit:.2f} F")

def convert_from_fahrenheit():
    fahrenheit = float(input("Fahrenheit : "))
    celsius = 5 / 9 * (fahrenheit - 32)
    print(f"Result: {celsius:.2f} C")

main()