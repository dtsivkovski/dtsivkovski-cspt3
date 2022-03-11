import time

# terminal print commands
ANSI_CLEAR_SCREEN = u"\u001B[2J"
ANSI_HOME_CURSOR = u"\u001B[0;0H\u001B[2"
OCEAN_COLOR = u"\u001B[44m\u001B[2D"
FIRE_COLOR = u"\u001B[31m\u001B[2D"
COMP_COLOR = u"\u001B[0m\u001B[2D"



# print ship with colors and leading spaces
def pattern_print(position):
    print(ANSI_HOME_CURSOR)
    sp = " " * position
    print(FIRE_COLOR)
    print(sp + "                  .----.")
    print(sp + "      .---------. | == |")
    print(sp + '      |.-"""""-.| |----|')
    print(sp + "      ||       || | == |")
    print(sp + "      ||       || |----|")
    print(sp + "      |'-.....-'| |::::|")
    print(sp + '      `"")---(""` |___.|')
    print(sp + '     /:::::::::::' + '\ ' + '" ' +  ' "')
    print(sp + "    /:::=======:::\     ")
    print(sp + '    `"""""""""""""`     ')
    print(COMP_COLOR)







# Pattern function, iterface into this file
def patternfunc():

    # loop control variables
    start = 0  # start at zero
    distance = 100  # how many times to repeat
    step = 1  # count by 2

    # loop purpose is to animate candle moving
    for position in range(start, distance, step):
        pattern_print(position)  # call to function with parameter
        time.sleep(.1)