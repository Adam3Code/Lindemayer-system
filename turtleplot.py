# Import libraries
import matplotlib.pyplot as plt
import numpy as np

"""
Documentation:
---
The function 'turtlePlot' accepts three mandatory inputs; the turtleCommands created in the turtleGraph function, 
the (System) corresponding to 'Koch' or 'Sierpinski', and a number of iterations (N). The approach of repeating
the 'System' and 'N' variables in the function was done to simplify the main-script, and was simpler than
creating global variables across the directory or creating a function that could deduce the systems and #iterations. 
It is necessary to know the system, and #iterations, to make the correct title, which depends on system and #iterations.
---
turtlePlot Input(s): List of commands from prev function output (TurtleGraph), should be an array of the format:
                     length, angle, length2, angle2, etc.. And system which should be a string, either "Koch" or 
                     "Sirpinski", third input should be an integer between 0 and 8, indicating the amount of 
                     iterations of the system.
turtlePlot Output(s): Plot showing the Lindenmayer System
- Author(s): Adam F. Rustom, Anders K. Skovborg, Lucas K. Laue; 2022
"""

def turtlePlot(turtleCommands, System, N):

    # Defining start position and direction of graph/plot
    coordinate = np.array([0, 0])
    position_vector = np.array([1, 0])
    x = np.array([0])
    y = np.array([0])

    # Finds length and angle of line segments, inputs angle to rotation matrix to find new position vector,
    # then calculates location of next coordinate based on the length of the line and the direction of position vector.
    # Finally, it splits the coordinate array into an array of x and an array of y coordinates.
    for i in range(0, len(turtleCommands), 2):
        length = np.array([turtleCommands[i]])
        angle = np.radians(turtleCommands[i + 1])

        c, s = np.cos(angle), np.sin(angle)
        rotation_matrix = np.array([(c, -s), (s, c)])

        position_vector = np.dot(rotation_matrix, position_vector)

        coordinate = coordinate + length * position_vector

        x, y = np.append(x, (coordinate[0])), np.append(y, (coordinate[1]))

    # Plots the coordinates and changes settings for the plot. Title depends on which system, and #iterations chosen.
    if System == "Sierpinski triangle":
        title = "Plot showing the " + str(System) + " after " + str(N) + " iterations"
        plt.plot(x, y, color='olivedrab')

    else:
        title = "Plot showing the " + str(System) + " after " + str(N) + " iterations"
        plt.plot(x, y, color='brown')
    plt.title(title, fontname='Comic Sans MS')
    plt.rcParams['font.size'] = 12
    ax = plt.gca()
    ax.set_facecolor('whitesmoke')
    plt.xlabel('Length - x', fontname='Comic Sans MS', fontsize=11)
    plt.ylabel('Height - y', fontname='Comic Sans MS', fontsize=11)
    plt.axis('square')

    plt.show()  # Reveal masterpiece!


if __name__ == "__main__":
    print("")
