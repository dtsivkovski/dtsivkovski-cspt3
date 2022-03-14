# menuy.py - function style menu
# Imports typically listed at top
# each import enables us to use logic that has been abstracted to other files and folders
# import patterns
# import stringy
# import listy
# import loopy
# import mathpy
# from mody import advy
# # abstracted files in a folder (aka module)
# from mody import questy
# from wipy import funcy
# from wipy import prefuncy
# import patterns
import ageswap
import matrix
import pattern
import os


# Main list of [Prompts, Actions]
# Two styles are supported to execute abstracted logic
# 1. file names will be run by exec(open("filename.py").read())
# 2. function references will be executed directly file.function()
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