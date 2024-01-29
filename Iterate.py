"""
Documentation:
LindIter Input(s): a string 'Koch' or 'Sierpinski'; a positive integer N corresponding to iterations.
LindIter Output(s): a string of letters corresponding to 'Koch' or 'Sierpinski' after N iterations.
- Author(s): Adam F. Rustom, Anders K. Skovborg, Lucas K. Laue; 2022.
"""

def LindIter(System, N):

    # Rule(s) for Koch (KR1) and Rule(s) for Sierpinski (SR1 and SR2)
    KR1 = "SLSRSLS"
    SR1 = "yRxRy"
    SR2 = "ALBLA"
    LindenmayerString = ""

    # If Koch is chosen, the letters are replaced by strings according to the Sierpinski rules
    if System == "Koch curve":
        string = "S"
        if N > 0:
            for i in range(N):
                string = string.replace("S", KR1)
                LindenmayerString = string
        else:
            LindenmayerString = string    # When zero iterations is chosen, output will be 'S'

    # If Sierpinski is chosen, the letters are replaced by strings according to the Sierpinski rules
    elif System == "Sierpinski triangle":
        string = "A"
        if N > 0:
            for i in range(N):
                string = string.replace("A", SR1)
                string = string.replace("B", SR2)
                string = string.replace("x", "A")
                string = string.replace("y", "B")
                LindenmayerString = string
        else:
            LindenmayerString = string     # When zero iterations is chosen, output will be 'S'
    return LindenmayerString

