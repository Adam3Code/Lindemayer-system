# Import libraries
import numpy as np
from Iterate import LindIter
from turtleGraph import turtleGraph
from turtleplot import turtlePlot

"""
Documentation:
---
This is the main-script, which is a combination of a code and two helper functions: 'inputNumber' and
'displayMenu'. These functions provide a selection system (way to select the different parts of the
interface) and the interface itself, respectively. The main-script works in conjunction with the functions:
LindIter, turtleGraph and turtlePlot. Therefore these should be imported. The two helper functions are inspired by:
Mikkel N. Schmidt (contact: mnsc@dtu.dk) and published 2015.
---
- Author(s): Adam F. Rustom, Anders K. Skovborg, Lucas K. Laue; 2022.
"""

# Helper function (1)
# Function by Mikkel N. Schmidt (contact: mnsc@dtu.dk) (publishing: 2015)
# prompts user to input an integer, and provides an error message if invalid input
# Usage: num = inputNumber(prompt)
# repeat until a valid input has been used
# inputNumer input(s): a user input (prompt)
# inputNumber output(s): Either an error message (if user-input is not integer), or the integer inputted by user
def inputNumber(prompt):
    while True:
        try:
            num = int(input(prompt))
            break
        except ValueError:
            print("---------------------------------------")
            print("Error: Enter an integer: ")
            print("---------------------------------------")
            pass
    return num


# Helper function (2)
# Function inspired by Mikkel N. Schmidt (contact: mnsc@dtu.dk) (publishing: 2015)
# Makes it possible to display options and/or choose an interval of options to choose from
# Usage: choice = displayMenu(prompt)
# displayMenu Input(s): inputs options/interval, a prompt and a boolean show_menu(if true menu is shown else not).
# displayMenu Output(s): Either an error message if input not among options else the output is a string of the choice
# made
def displayMenu(options, prompt, show_menu):
    print("---------------------------------------")
    # If show_menu is true, the menu is displayed.
    if show_menu:
        for i in range(len(options)):
            print("[{:d}]: {:s}".format(i, options[i]))
    # menu_choice is initially defined outside the range of any menu option.
    # Loop continues as long as the menu_choice is outside the range of the menu option
    # if user-input is not among options, an error message is displayed
    menu_choice = 69
    while not (np.any(menu_choice == np.arange(len(options)))):
        menu_choice = inputNumber(prompt)
        if menu_choice not in np.arange(len(options)):
            print("---------------------------------------")
            print("Error: Integer out of bound")
            print("---------------------------------------")
    return options[menu_choice]


""" Main script starts from here """
# Global variables only for the main-script
is_system_chosen = False  # Boolean: Used to check if system is chosen

# Prompts the helper functions, and calls the appropriate functions when selected through the input
while True:
    # Defines menu items, if system is not chosen, it is not possible to generate plots
    if not is_system_chosen:
        main_menu = ["Choose Lindenmayer system", "Quit"]
    else:
        main_menu = ["Change Lindenmayer system", "Generate plots", "Quit"]

    # Displays menu options - And the user it asked to choose among the options
    choice = displayMenu(main_menu, "Choose a menu item: ", True)

    # Choose lindenmayer system
    if choice == "Choose Lindenmayer system" or choice == "Change Lindenmayer system":
        systems = ["Koch curve", "Sierpinski triangle"]
        system_type = displayMenu(systems, "Select system: ", True)
        is_system_chosen = True
        # Prompts user to select number of iterations wanted in the interval 0-8
        if is_system_chosen:
            pos_iterations = np.arange(9)
            num_iterations = (displayMenu(pos_iterations, "Iterations: Choose an integer from 0-8: ", False))
    # Generate plots
    elif choice == "Generate plots":
        # Checks if the user has chosen a system, otherwise an error message is outputted
        # Computes the turtle commands, and plots
        if is_system_chosen:
            word = LindIter(system_type, num_iterations)
            LenAng_arr = turtleGraph(word, system_type, num_iterations)
            turtlePlot(LenAng_arr, system_type, num_iterations)
        else:
            print("---------------------------------------")
            print("Error: You must choose a system first: ")
    # Quit
    elif choice == "Quit":
        break