"""
CP1404/CP5632 - Practical
Program to select a prepared menu
"""

menu = "(H)ello\n(G)oodbye\n(Q)uit"

name = input("Enter name: ")
print(menu)
selected_menu = input(">>> ").upper()

while selected_menu != "Q":
    if selected_menu == "H":
        print(f"Hello {name}")
    elif selected_menu == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")

    print(menu)
    selected_menu = input(">>> ").upper()

print("Finished")




