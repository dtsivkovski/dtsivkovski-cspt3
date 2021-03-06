import time

# terminal print commands
ANSI_CLEAR_SCREEN = u"\u001B[2J"
ANSI_HOME_CURSOR = u"\u001B[0;0H\u001B[2"
OCEAN_COLOR = u"\u001B[44m\u001B[2D"
MAGENTA_COLOR = u"\u001b[35;1m"
COMP_COLOR = u"\u001B[0m\u001B[2D"



# print computer moving across screen
def pattern_print(position):
    print(ANSI_CLEAR_SCREEN)
    print(ANSI_HOME_CURSOR)
    os = " " * position
    print(MAGENTA_COLOR)
    print(os + "                  .----.")
    print(os + "      .---------. | == |")
    print(os + '      |.-"""""-.| |----|')
    print(os + "      ||       || | == |")
    print(os + "      ||       || |----|")
    print(os + "      |'-.....-'| |::::|")
    print(os + '      `"")---(""` |___.|')
    print(os + "  " u'\u001B[0m\u001B[2D     /:::::::::::' + '\ ' + u'\u001b[35;1m" ' +  ' "')
    print(os + "  " + u"\u001B[0m\u001B[2D    /:::=======:::\     ")
    print(os + '    `"""""""""""""`     ')
    print(COMP_COLOR)

# Pattern function for the non-animated(static) pattern
def staticpattern():
  pattern_print(0)

# Pattern function for drawing the animated pattern
def patternfunc():

    # Animation Variables
    start = 0  # Start with no offset
    distance = 50  # Number of loops
    step = 1  # Step amount

    # Loop to move the computer to the right
    for position in range(start, distance, step):
        pattern_print(position)  
        time.sleep(.1)