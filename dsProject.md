{% include navbar.html %}

# Data Structures Project


### Repl Links

{% include repl_embed.html %}

[TT0 - Python Menu](https://replit.com/@DanielTsivkovsk/dtsivkovski-cspt3#.replit)

### Code Snippets

Menu and Patterns Submenu
```python
main_menu = [
    ["Age Swap", ageswap.ageswap_run],
    ["Matrix", matrix.matrix_tester],
]

patterns_sub_menu = [
    ["Animated Pattern", pattern.patternfunc],
    ["Static Pattern", pattern.staticpattern],
]

# Menu banner and formatted borders
thinborder = "-" * 25
border = "=" * 25
banner = f"\n{thinborder}\nPlease Select An Option\n{border}"


def menu():
    title = f"{border}\n" + "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Pattern", patterns_submenu])
    buildMenu(title, menu_list)

def patterns_submenu():
    title = f"{border}\n" + "Patterns Submenu" + banner
    buildMenu(title, patterns_sub_menu)

def buildMenu(banner, options):
    # header for menu
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '-', value[0])

    # get user choice
    choice = input("Type your choice - ")

    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            os.system("clear")
            return
        try:
            # try as function
            os.system("clear")
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # NAN error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # All other errors covered here
        print(f"Invalid choice: {choice}")
    # end validation try

    buildMenu(banner, options)  # recursion, start menu over again


if __name__ == "__main__":
    menu()
```

Matrix Print w/ Custom Input
```python
def matrixfunc(list):
    for i in list:
        # prints all elements in each list i 
        print(*i)
    return(list)

def matrix_tester():
    # Asks for an integer of how many rows
    rowcount = int(input("How many rows? (integer input) - "))
    matrix = []
    # Loop for finding values for each row, splitting each value by the comma
    for row in range(0, rowcount):
      s = input("Input values separated by commas for Row #" + str(row) + " - ")
      rowvalue = s.split(",")
      matrix.append(rowvalue)
    # Prints matrix and formatted
    print("=" * 25)
    print("Your original matrix is: ")
    print(matrix)
    print("=" * 25)
    print("Your formatted matrix is: ")
    matrixfunc(matrix)
```

Static and Animated Patterns
```python
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
```

Ageswap Function
```python
def ageswap(age1, age2):
    if (int(age1) > int(age2)):
        # swapping age by assigning one of them to a temp variable
        temp = age1
        age1 = age2
        age2 = temp
    return(age1, age2)

def ageswap_run():
    age1 = input("What is the first age? - ")
    age2 = input("What is the second age? - ")
    print("=" * 25)
    print("Original: ", age1, age2)
    age1, age2 = ageswap(age1, age2)
    print("Final: ", age1, age2)
    print("=" * 25)
```

### Github links

- [Week 0 Items](https://github.com/dtsivkovski/dtsivkovski-cspt3/issues/1)
