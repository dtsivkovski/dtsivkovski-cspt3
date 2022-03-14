import time

# terminal print commands
ANSI_CLEAR_SCREEN = u"\u001B[2J"
ANSI_HOME_CURSOR = u"\u001B[0;0H\u001B[2"
OCEAN_COLOR = u"\u001B[44m\u001B[2D"
RED_COLOR = u"\u001B[31m\u001B[2D"
COMP_COLOR = u"\u001B[0m\u001B[2D"



# print computer moving across screen
def pattern_print(position):
    print(ANSI_CLEAR_SCREEN)
    print(ANSI_HOME_CURSOR)
    os = " " * position
    print(RED_COLOR)
    print(os + "                  .----.")
    print(os + "      .---------. | == |")
    print(os + '      |.-"""""-.| |----|')
    print(os + "      ||       || | == |")
    print(os + "      ||       || |----|")
    print(os + "      |'-.....-'| |::::|")
    print(os + '      `"")---(""` |___.|')
    print(os + '     /:::::::::::' + '\ ' + '" ' +  ' "')
    print(os + "    /:::=======:::\     ")
    print(os + '    `"""""""""""""`     ')
    print(COMP_COLOR)

def staticpattern():
  pattern_print(0)

# Pattern function, iterface into this file
def patternfunc():

    # Animation Variables
    start = 0  # Start with no offset
    distance = 100  # Number of loops
    step = 1  # Step amount

    # Loop to move the computer to the right
    for position in range(start, distance, step):
        pattern_print(position)  
        time.sleep(.1)