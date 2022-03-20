{% include navbar.html %}

# Data Structures Project


### Repl Links

{% include repl_embed.html %}

[Repl Menu Link](https://replit.com/@DanielTsivkovsk/dtsivkovski-cspt3#.replit)

### Code Snippets

### Week 1

InfoDb Lists
```python
def print_data(n):
    print(InfoDb[n]["FirstName"], InfoDb[n]["LastName"])  # using comma puts space between values
    print("\t", "Tech: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["Owns_Tech"]))  # join allows printing a string list with separator
    print()

def list_finder():
  num = int(input("Which index do you want to search (0-" + str(len(InfoDb)-1) +"): "))
  print("-" * 25)
  try:
    # Prints all info of the given index
    print(InfoDb[num]["FirstName"] + " "+ InfoDb[num]["LastName"])
    print("Residence: " + InfoDb[num]["Residence"])
    print("Owns Tech: ")
    for i in range (0, len(InfoDb[num]["Owns_Tech"])):
      print("  - " + InfoDb[num]["Owns_Tech"][i])
  except:
    # Prints this if the index is not in the list
    print("Invalid index given.")
```

InfoDb Loops
```python
# for loop iterates on length of InfoDb
def for_loop():
    print("=" * 25)
    print("For loop")
    print("-" * 25)
    for n in range(len(InfoDb)):
        print_data(n)

# while loop contains an initial n and an index incrementing statement (n += 1)
def while_loop(n):
    print("=" * 25)
    print("While loop")
    print("-" * 25)
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return

def while_loop_run():
    while_loop(0)

# recursion simulates loop incrementing on each call (n + 1) until exit condition is met
def recursive_loop(n):
    if n < len(InfoDb):
        print_data(n)
        recursive_loop(n + 1)
    return # exit condition

def recursive_loop_run():
    print("=" * 25)
    print("Recursive loop")
    print("-" * 25)
    recursive_loop(0)
    print("=" * 25)
```

Fibonacci
```python 
# Hack 3: Fibonacci.  Write a recursive program to create a fibonacci sequence including error handling(with try/except) for invalid input
def recur_fibonacci(n,h,i,j):
    if h == 0:
        return n
    else:
        # adds previous two values together, assign new values
        n = i + j
        i = j
        j = n
        # print the value 
        print(n)
        return recur_fibonacci(n,h-1,i,j)

# Tester for the recursive fibonacci function with try/except
def recur_fibonacci_tester():
  num = int(input("Enter a number for fibonacci: "))
  print("-" * 25)
  if num < 0:
      print("Sorry, fibonacci does not exist for negative numbers.")
  else:
    try:
        result = recur_fibonacci(0, num, 0, 1)
        print(MAGENTA_COLOR)
        print("The result of fibonacci", num, "times is", result)
        print(COMP_COLOR)
    except:
        print("Error - Invalid Input")
        print(COMP_COLOR)
```

### Week 0

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
