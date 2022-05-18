# from functions import *

the_menu = {"T" : "Total grade",
    "L" : "List",
    "A" : "Add",
    "U" : "Update",
    "D" : "Delete",
    "S" : "Save the data",
    "R" : "Restore data from file",
    "Q" : "Quit this program"}
opt = None

while True:
    # print_main_menu(the_menu) # TODO 2: uncomment, define the function, and call with the menu as an argument
    opt = input("::: Enter a menu option\n> ")
    opt = opt.upper() # to allow us to input lower- or upper-case letters

    if opt not in the_menu.keys():
        print(f"WARNING: {opt} is an invalid menu option.\n")
        continue

    print(f"You selected option {opt} to > {the_menu[opt]}.")

    if opt == "Q":
        print("Goodbye!\n")
        break # exit the main `while` loop

    input("::: Press Enter to continue")

print("See you next time!")