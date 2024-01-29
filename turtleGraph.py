# Import libraries
import numpy as np

"""
Documentation:
---
The function 'turtleGraph' accepts three mandatory inputs; a string (LindenmayerString) created in 'LindIter', another
string (System) corresponding to 'Koch' or 'Sierpinski', and a number of iterations (N). The approach of repeating
the 'System' and 'N' variables in the function was done to simplify the main-script, and was simpler than
creating global variables across the directory or creating a function that could deduce the systems and #iterations. 
It is necessary to know the system, and #iterations, to insert correct angle of rotation and length of segment.
---
turtleGraph Input(s): String from prev function output (LindIter), system which should be a string, either "Koch" or
                      "Sirpinski", third input should be an integer between 0 and 8, indicating the amount of 
                      iterations of the system.
turtleGraph Output(s): Array of commands (lengths and angles).
- Author(s): Adam F. Rustom, Anders K. Skovborg, Lucas K. Laue; 2022.
"""

def turtleGraph(LindenmayerString, System, N):

    # Making Dictionary for 'Sierpinski' and 'Koch'
    LindenmayerString = "H" + LindenmayerString
    turtleCommands = np.zeros(len(LindenmayerString))
    koch_values = {"H": 0, "S": (1/3)**N, "L": 60, "R": -120}
    sierpinski_values = {"H": 0, "A": (1/2)**N, "B": (1/2)**N, "L": 60, "R": -60}
    p = {}

    # Applying 'Koch' dictionary if System input is corresponding
    if System == "Koch curve":
        p = koch_values

    # Applying 'Sierpinski' dictionary if System input is corresponding
    elif System == "Sierpinski triangle":
        p = sierpinski_values

    # Creating a list of commands alternating between lengths and angles by looping through every other element
    # Switching position of each angle and length value to satisfy the order: length1, angle1, length2, angle2, ... etc
    for i in range(0, len(LindenmayerString), 2):
        turtleCommands[i] = p[LindenmayerString[i+1]]
        turtleCommands[i+1] = p[LindenmayerString[i]]
    return turtleCommands




